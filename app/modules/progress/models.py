from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.users.models import User

class Progress(Base):
    """
    SQLAlchemy model for tracking User Progress.
    """
    __tablename__ = "progress"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    course_progress: Mapped[float] = mapped_column(Float, default=0.0)
    chapter_progress: Mapped[float] = mapped_column(Float, default=0.0)
    quiz_progress: Mapped[float] = mapped_column(Float, default=0.0)
    total_progress: Mapped[float] = mapped_column(Float, default=0.0)

    # Relationship back to User
    user: Mapped["User"] = relationship("User", back_populates="progress")
