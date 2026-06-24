from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.users.models import User
    from app.modules.videos.models import Video

class Download(Base):
    """
    SQLAlchemy model for User Downloads.
    """
    __tablename__ = "downloads"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    video_id: Mapped[int] = mapped_column(ForeignKey("videos.id"), nullable=False)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="downloads")
    video: Mapped["Video"] = relationship("Video", back_populates="downloads")
