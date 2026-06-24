from pydantic import BaseModel, ConfigDict

class RoleCourseBase(BaseModel):
    """
    Base Pydantic model for RoleCourse association.
    """
    role_id: int
    course_id: int

class RoleCourseCreate(RoleCourseBase):
    """
    Pydantic model for creating a new role-course association.
    """
    pass

class RoleCourse(RoleCourseBase):
    """
    Pydantic model for RoleCourse response.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
