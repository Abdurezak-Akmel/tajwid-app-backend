from sqlalchemy import String, ForeignKey, Integer, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from datetime import datetime

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.users.models import User
    from app.modules.courses.models import Course

class AccessRequest(Base):
    """
    SQLAlchemy model for Course Access Requests.
    """
    __tablename__ = "access_requests"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float, default=0.0)
    receipt_file_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    receipt_file_size: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="pending")  # pending, approved, rejected
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="access_requests")
    course: Mapped["Course"] = relationship("Course", back_populates="access_requests")
