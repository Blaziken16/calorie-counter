from fastapi import APIRouter, HTTPException,status,Depends
from core.schemas.user_schema import UserCreate, UserResponse
from core.schemas.logs_schema import LogCreate,LogResponse
from core.api.services.user_services import create_user, get_user_by_id
from core.api.services.log_services import get_all_logs_by_user
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.database import get_db



router = APIRouter()


@router.get(
    "/{user_id}/logs",
    response_model=LogResponse,
)
async def handles_get_logs_by_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    logs = get_all_logs_by_user(db, user_id)
    return logs