from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import Annotated
from core.db.database import get_db, engine, Base
from core.api.routers import user_routes, log_routes

@asynccontextmanager
async def lifespan(_app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose() 

app = FastAPI(lifespan=lifespan)

app.include_router(user_routes.router, prefix="api/user", tags=["users"])
app.include_router(log_routes.router, prefix="api/log", tags=["logs"])





