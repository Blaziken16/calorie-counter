from fastapi import Depends, HTTPException, status 
from typing import Annotated
from models.user_model import User
import core.models.user_log
from core.schemas.user_schema import UserCreate
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

async def get_user_logs(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(User.logs).where(User.id == user_id)
    )
    logs = result.scalars().all()
    return logs
