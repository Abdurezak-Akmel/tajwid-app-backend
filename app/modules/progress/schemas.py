from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProgressBase(BaseModel):
    """
    Base Pydantic model for Progress, containing shared fields.
    """
    user_id: int
    course_progress: float = 0.0
    chapter_progress: float = 0.0
    quiz_progress: float = 0.0
    total_progress: float = 0.0

class ProgressCreate(ProgressBase):
    """
    Pydantic model for creating new progress records.
    """
    pass

class ProgressUpdate(BaseModel):
    """
    Pydantic model for updating an existing progress record.
    All fields are optional.
    """
    user_id: Optional[int] = None
    course_progress: Optional[float] = None
    chapter_progress: Optional[float] = None
    quiz_progress: Optional[float] = None
    total_progress: Optional[float] = None

class Progress(ProgressBase):
    """
    Pydantic model for progress response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
