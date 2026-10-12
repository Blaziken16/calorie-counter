from fastapi import APIRouter, status, Depends
from core.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from core.api.services.user_services import create_user, get_user_by_id, delete_user,update_user
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.database import get_db

User_router = APIRouter()

@User_router.post(
    "",
    response_model= UserResponse,
    status_code = status.HTTP_201_CREATED,
)
async def create_user_endpoint(user:UserCreate, db:Annotated[AsyncSession, Depends(get_db)]):
    new_user = await create_user(user = user, db = db)
    return new_user

@User_router.get(
    "/{user_id}",
    response_model= UserResponse,
)
async def get_user_by_id_endpoint(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    user = await get_user_by_id(user_id, db)
    return user

@User_router.patch(
        "/{user_id}",
        response_model= UserResponse
)
async def update_user_endpoint( user_update: UserUpdate , user_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    user = await update_user(user_update, user_id, db)
    return user


@User_router.delete(
    "/{user_id}",
    status_code= status.HTTP_204_NO_CONTENT,
)
async def delete_user_endpoint(user_id:int, db: Annotated[AsyncSession, Depends(get_db)]):
    await delete_user(user_id, db)