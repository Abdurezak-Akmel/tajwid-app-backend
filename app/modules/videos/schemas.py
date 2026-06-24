from pydantic import BaseModel, ConfigDict
from typing import Optional

class VideoBase(BaseModel):
    """
    Base Pydantic model for Video, containing shared fields.
    """
    course_id: int
    chapter_id: int
    title: str
    description: Optional[str] = None
    duration: int
    file_size: int

class VideoCreate(VideoBase):
    """
    Pydantic model for creating a new video.
    """
    pass

class VideoUpdate(BaseModel):
    """
    Pydantic model for updating an existing video.
    All fields are optional.
    """
    course_id: Optional[int] = None
    chapter_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    file_size: Optional[int] = None

class Video(VideoBase):
    """
    Pydantic model for video response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
