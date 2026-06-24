from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.courses.models import Course
    from app.modules.chapters.models import Chapter
    from app.modules.downloads.models import Download

class Video(Base):
    """
    SQLAlchemy model for the Video entity.
    """
    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("chapters.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)  # Duration in seconds
    file_size: Mapped[int] = mapped_column(Integer, nullable=False)  # Size in bytes

    # Relationships
    course: Mapped["Course"] = relationship("Course", back_populates="videos")
    chapter: Mapped["Chapter"] = relationship("Chapter", back_populates="videos")
    downloads: Mapped[List["Download"]] = relationship("Download", back_populates="video")
