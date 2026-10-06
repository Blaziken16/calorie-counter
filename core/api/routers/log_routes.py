from fastapi import APIRouter, HTTPException,status,Depends
from core.schemas.user_schema import UserCreate, UserResponse
from core.schemas.logs_schema import logCreate,logResponse
from core.api.services.user_services import create_user, get_user_by_id, get_user_logs
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.database import get_db



router = APIRouter()


@router.get(
    "/{user_id}/logs",
    response_model=logResponse,
)
async def handles_get_logs_by_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    logs = get_user_logs(user_id, db)
    return logs