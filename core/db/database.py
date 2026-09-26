from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import local_dotenv 

local_dotenv()
db_url = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_async_engine(
    
)