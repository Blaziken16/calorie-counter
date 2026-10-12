from fastapi import HTTPException, status 
from core.models.user_log import Logs
from core.models.user_model import User
from core.schemas.logs_schema import LogUpdate, LogCreate, LogResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone

async def create_log(log: LogCreate, db: AsyncSession) -> Logs:
    result = await db.execute(
        select(User).where(User.id == log.user_id)
    )
    user = result.scalars().first()
    if not user: 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="user not found")

    new_log = Logs(
        food_name = log.food_name,
        calories = log.calories,
        user_id = log.user_id,
        logged_at = datetime.now(timezone.utc)
    )
    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log

async def get_log_by_id(log_id: int, db: AsyncSession)-> Logs:
    result = await db.execute(
        select(Logs).where(log_id == Logs.id)
    )
    log = result.scalars().first()
    if not log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log was not found.")
    return log


async def update_logs_full(db: AsyncSession, log_id: int, log_update: LogCreate)-> Logs:
    result = await db.execute(
        select(Logs).where(Logs.id == log_id)
    )
    log = result.scalars().first()
    if not log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log was not found.")
    if log_update.user_id != log.user_id:
        result = await db.execute(
            select(User).where(User.id == log_update.user_id)
        )
        user = result.scalars().first()
        if not user: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "user not found.")
        
    log.food_name = log_update.food_name
    log.calories = log_update.calories
    log.logged_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(log)
    return log

async def update_log_partial(log_id: int,db: AsyncSession, log_update: LogUpdate)->Logs:
    result = await db.execute(
        select(Logs).where(Logs.id == log_id)
    )
    log = result.scalars().first()

    if not log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "log not found")
    update_data = log_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(log, field, value)

    await db.commit()
    await db.refresh(log)
    return log

async def delete_log_by_id(log_id: int, db: AsyncSession):
    log = await get_log_by_id(log_id, db)

    await db.delete(log)
    await db.commit()
    