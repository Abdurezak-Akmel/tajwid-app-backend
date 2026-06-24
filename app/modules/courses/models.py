from sqlalchemy import String, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.chapters.models import Chapter
    from app.modules.videos.models import Video
    from app.modules.quizzes.models import Quiz
    from app.modules.access_requests.models import AccessRequest

class Course(Base):
    """
    SQLAlchemy model for the Course entity.
    """
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    level: Mapped[str] = mapped_column(String(50), nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    access_type: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, default=0.0)
    course_group: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Relationships
    chapters: Mapped[List["Chapter"]] = relationship("Chapter", back_populates="course")
    videos: Mapped[List["Video"]] = relationship("Video", back_populates="course")
    quizzes: Mapped[List["Quiz"]] = relationship("Quiz", back_populates="course")
    access_requests: Mapped[List["AccessRequest"]] = relationship("AccessRequest", back_populates="course")
