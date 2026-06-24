from pydantic import BaseModel, ConfigDict
from typing import Optional

class QuizBase(BaseModel):
    """
    Base Pydantic model for Quiz, containing shared fields.
    """
    course_id: int
    chapter_id: int
    quiz_name: str
    quiz_description: Optional[str] = None
    difficulty: str
    number_of_questions: int = 0
    total_magnitude: float = 0.0

class QuizCreate(QuizBase):
    """
    Pydantic model for creating a new quiz.
    """
    pass

class QuizUpdate(BaseModel):
    """
    Pydantic model for updating an existing quiz.
    All fields are optional.
    """
    course_id: Optional[int] = None
    chapter_id: Optional[int] = None
    quiz_name: Optional[str] = None
    quiz_description: Optional[str] = None
    difficulty: Optional[str] = None
    number_of_questions: Optional[int] = None
    total_magnitude: Optional[float] = None

class Quiz(QuizBase):
    """
    Pydantic model for quiz response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
