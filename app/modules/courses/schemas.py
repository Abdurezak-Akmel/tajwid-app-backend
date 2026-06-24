from pydantic import BaseModel, ConfigDict
from typing import Optional

class CourseBase(BaseModel):
    """
    Base Pydantic model for Course, containing shared fields.
    """
    title: str
    description: Optional[str] = None
    level: str
    category: str
    access_type: str
    price: float = 0.0
    course_group: Optional[str] = None

class CourseCreate(CourseBase):
    """
    Pydantic model for creating a new course.
    """
    pass

class CourseUpdate(BaseModel):
    """
    Pydantic model for updating an existing course.
    All fields are optional.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    level: Optional[str] = None
    category: Optional[str] = None
    access_type: Optional[str] = None
    price: Optional[float] = None
    course_group: Optional[str] = None

class Course(CourseBase):
    """
    Pydantic model for course response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
