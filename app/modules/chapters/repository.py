from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.base_repository import BaseRepository
from app.modules.chapters.models import Chapter

class ChapterRepository(BaseRepository[Chapter]):
    def __init__(self, db: Session):
        super().__init__(Chapter, db)

    def get_by_course(self, course_id: int) -> List[Chapter]:
        return self.db.query(self.model).filter(self.model.course_id == course_id).all()
