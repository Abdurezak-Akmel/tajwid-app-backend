from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base

class RoleCourse(Base):
    """
    SQLAlchemy model for the Role-Course many-to-many relationship.
    """
    __tablename__ = "role_course"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
