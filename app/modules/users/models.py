from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.roles.models import Role
    from app.modules.progress.models import Progress
    from app.modules.access_requests.models import AccessRequest
    from app.modules.downloads.models import Download
    from app.modules.notifications.models import Notification

class User(Base):
    """
    SQLAlchemy model for the User entity.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    tg_username: Mapped[str | None] = mapped_column(String(100), unique=True, nullable=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    # Relationships
    role: Mapped["Role"] = relationship("Role", back_populates="users")
    progress: Mapped[List["Progress"]] = relationship("Progress", back_populates="user")
    access_requests: Mapped[List["AccessRequest"]] = relationship("AccessRequest", back_populates="user")
    downloads: Mapped[List["Download"]] = relationship("Download", back_populates="user")
    notifications: Mapped[List["Notification"]] = relationship("Notification", back_populates="user")
