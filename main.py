from fastapi import FastAPI, HTTPException, Request, status
from contextlib import asynccontextmanager
from core.db.database import  engine, Base
from core.api.routers import user_routes, log_routes
from starlette.exceptions import HTTPException as StarletteHTTPException


@asynccontextmanager
async def lifespan(_app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose() 

app = FastAPI(lifespan=lifespan)

app.include_router(user_routes.router, prefix="/api/user", tags=["users"])
app.include_router(log_routes.router, prefix="/api/log", tags=["logs"])






