from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.db.database import Base
from datetime import UTC, datetime


class Logs(Base):
    __tablename__ = "userLogs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False, index=True)
    food_name: Mapped[str] = mapped_column(String(100), nullable=False)
    calories: Mapped[str] = mapped_column(String(30), nullable=False)

    logged_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
    user: Mapped["User"] = relationship(back_populates="logs") 
    



