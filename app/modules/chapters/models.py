from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.courses.models import Course
    from app.modules.videos.models import Video
    from app.modules.quizzes.models import Quiz

class Chapter(Base):
    """
    SQLAlchemy model for the Chapter entity.
    """
    __tablename__ = "chapters"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    ch_title: Mapped[str] = mapped_column(String(255), nullable=False)
    ch_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationships
    course: Mapped["Course"] = relationship("Course", back_populates="chapters")
    videos: Mapped[List["Video"]] = relationship("Video", back_populates="chapter")
    quizzes: Mapped[List["Quiz"]] = relationship("Quiz", back_populates="chapter")
