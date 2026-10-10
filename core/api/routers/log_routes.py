from fastapi import APIRouter,status,Depends
from core.schemas.logs_schema import LogCreate,LogResponse, LogUpdate
from core.api.services.log_services import get_log_by_id, create_log, update_logs_full,update_log_partial
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.database import get_db



Log_router = APIRouter()


@Log_router.get(
    "/{log_id}",
    response_model= LogResponse
)
async def get_log_endpoint(log_id: int, db:Annotated[AsyncSession, Depends(get_db)]):
    log = await get_log_by_id(log_id,db)
    return log

@Log_router.post(
    "",
    response_model= LogResponse,
    status_code= status.HTTP_201_CREATED
)
async def create_log_endpoint(log: LogCreate, db:Annotated[AsyncSession, Depends(get_db)]):
    new_log = await create_log(log, db)
    return new_log

@Log_router.put(
    "/{log_id}",
    response_model=LogResponse
)
async def update_log_full_endpoint(log_id: int, log_update: LogCreate, db:Annotated[AsyncSession, Depends(get_db)]):
    updated_log = await update_logs_full(db,log_id,log_update)
    return updated_log

@Log_router.patch(
    "/{log_id}",
    response_model=LogResponse
)
async def update_log_partialy_endpoint(log_id: int, log_update: LogUpdate, db:Annotated[AsyncSession, Depends(get_db)]):
    updated_log = await update_log_partial(log_id, db, log_update)
    return updated_log

