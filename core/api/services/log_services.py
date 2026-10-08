from fastapi import HTTPException, status 
from core.models.user_log import Logs
from core.models.user_model import User
from core.schemas.logs_schema import LogUpdate, LogCreate, LogResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from datetime import datetime, timezone

async def create_log(log: LogCreate, db: AsyncSession) ->Logs:
    result = await db.execute(
        select(User).where(User.id == log.user_id)
    )
    user = result.scalars().first()
    if not user: 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="user not found")

    new_log = Logs(
        foodName = log.food_name,
        calories = log.calories,
        user_id = log.user_id,
        logged_at = datetime.now(timezone.utc)
    )
    await db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log

async def get_all_logs_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(Logs).where(user_id == Logs.user_id).options(selectinload(Logs.user))
    )
    logs = result.scalars().all()
    return logs
