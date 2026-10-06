from fastapi import Depends, HTTPException, status 
from typing import Annotated
from models.user_log import Logs
from models.user_model import User
from core.schemas.logs_schema import LogUpdate, LogCreate, LogResponse
from core.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone

async def crete_log(log: LogCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(User).where(User.id == log.user_id)
    )
    user = result.scalars().first()
    if not user: 
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="user not found")

    new_log = Logs(
        foodName = log.foodName,
        calories = log.calories,
        user_id = log.user_id,
        loggedAt = datetime.now(timezone.utc)
    )
    await db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log