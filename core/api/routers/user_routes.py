from fastapi import APIRouter, HTTPException,status,Depends
from core.schemas.user_schema import UserCreate, UserResponse
from core.schemas.logs_schema import logCreate,logResponse
from core.api.services.user_services import create_user, get_user_by_id, get_user_logs
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.database import get_db

router = APIRouter()

@router.post(
    "",
    response_model= UserCreate,
    status_code = status.HTTP_201_CREATED,
)
async def handles_create_user(user:UserCreate, db:Annotated[AsyncSession, Depends(get_db)]):
    new_user = await create_user(user = user, db = db)
    return new_user

@router.get(
    "/{user_id}",
    response_model= UserResponse,
)
async def handles_get_user_id(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    user = get_user_by_id(user_id, db)
    return user

@router.get(
    "/{user_id}/logs",
    response_model=logResponse,
)
async def handles_get_logs_by_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    logs = get_user_logs(user_id, db)
    return logs