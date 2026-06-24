from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING, Any

from app.database.base import Base

if TYPE_CHECKING:
    from app.modules.users.models import User

class Role(Base):
    """
    SQLAlchemy model for the Role entity.
    """
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    access_details: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=True)

    # Relationships
    users: Mapped[List["User"]] = relationship("User", back_populates="role")
