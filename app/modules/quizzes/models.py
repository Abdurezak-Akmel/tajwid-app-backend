from sqlalchemy import String, Text, ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.courses.models import Course
    from app.modules.chapters.models import Chapter

class Quiz(Base):
    """
    SQLAlchemy model for the Quiz entity.
    """
    __tablename__ = "quizzes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("chapters.id"), nullable=False)
    quiz_name: Mapped[str] = mapped_column(String(255), nullable=False)
    quiz_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    difficulty: Mapped[str] = mapped_column(String(50), nullable=False)
    number_of_questions: Mapped[int] = mapped_column(Integer, default=0)
    total_magnitude: Mapped[float] = mapped_column(Float, default=0.0)

    # Relationships
    course: Mapped["Course"] = relationship("Course", back_populates="quizzes")
    chapter: Mapped["Chapter"] = relationship("Chapter", back_populates="quizzes")
