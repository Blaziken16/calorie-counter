from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.database import Base
from core.models.enums import Plan



class User(Base):
    __tablename__ = "user"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, index= True, unique=True)
    name:Mapped[str] = mapped_column(String(50),nullable=False, unique=True)
    weight:Mapped[str] = mapped_column(String(10),nullable=False)
    height:Mapped[str] = mapped_column(String(10), nullable= False)
    plan_selected:Mapped[Plan] = mapped_column(default= Plan.MAINTAIN)

    logs: Mapped[list["Logs"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    
