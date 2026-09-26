from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import local_dotenv 

local_dotenv()
db_url = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_async_engine(
    db_url,
    connect_args={"check_same_thread": False},
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncEngine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session