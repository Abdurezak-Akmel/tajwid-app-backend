from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.users.models import User

class Notification(Base):
    """
    SQLAlchemy model for User Notifications.
    """
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    details: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Relationship back to User
    user: Mapped["User"] = relationship("User", back_populates="notifications")
