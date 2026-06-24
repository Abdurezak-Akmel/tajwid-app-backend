from pydantic import BaseModel, ConfigDict
from typing import Optional

class ChapterBase(BaseModel):
    """
    Base Pydantic model for Chapter, containing shared fields.
    """
    course_id: int
    ch_title: str
    ch_description: Optional[str] = None
    content: Optional[str] = None

class ChapterCreate(ChapterBase):
    """
    Pydantic model for creating a new chapter.
    """
    pass

class ChapterUpdate(BaseModel):
    """
    Pydantic model for updating an existing chapter.
    All fields are optional.
    """
    course_id: Optional[int] = None
    ch_title: Optional[str] = None
    ch_description: Optional[str] = None
    content: Optional[str] = None

class Chapter(ChapterBase):
    """
    Pydantic model for chapter response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
