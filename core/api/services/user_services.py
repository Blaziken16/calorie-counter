from fastapi import Depends, HTTPException, status 
from typing import Annotated
from models.user_model import User
from core.schemas.user_schema import UserCreate, UserUpdate
from core.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def create_user(user: UserCreate,db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(User).where(User.name == user.name),
    )
    existing_user = result.scalars().first()
    if(existing_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "user name already exists",
        )
    new_user = user(
        name = user.name,
        weight = user.weight,
        height = user.height,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user_by_id(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    user = result.scalars().first()
    if(user):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found.")

async def update_user(user_update: UserUpdate, user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(User).where(User.id == user_id)
    )
    user = result.scalars().first()
    if(not user):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "user not found.")

    if(user_update.name is not None and user_update.name != User.name):
        result = await db.execute(
            select(User).where(user_update == User.name)
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


    