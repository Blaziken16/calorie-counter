from fastapi import HTTPException, status 
from core.models.user_model import User
from core.schemas.user_schema import UserCreate, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def create_user(user: UserCreate,db: AsyncSession)-> User:
    result = await db.execute(
        select(User).where(User.name == user.name),
    )
    existing_user = result.scalars().first()
    if(existing_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "user name already exists",
        )
    new_user = User(
        name = user.name,
        weight = user.weight,
        height = user.height,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user_by_id(user_id: int, db: AsyncSession) -> User:
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    user = result.scalars().first()
    if(not user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found.")
    return user
    
async def update_user(user_update: UserUpdate, user_id: int, db: AsyncSession)-> User:
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    user = result.scalars().first()
    if(not user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "user not found.")

    if(user_update.name is not None and user_update.name != user.name):
        result = await db.execute(
            select(User).where(user_update.name == user.name)
        )
        existing_user = result.scalars().first()
        if(existing_user):
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Username already exists.")

    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)

    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(user_id: int, db: AsyncSession):
    user = await get_user_by_id(user_id, db)
    await db.delete(user)
    await db.commit()