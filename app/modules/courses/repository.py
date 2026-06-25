from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.base_repository import BaseRepository
from app.modules.courses.models import Course

class CourseRepository(BaseRepository[Course]):
    def __init__(self, db: Session):
        super().__init__(Course, db)

    def get_by_level(self, level: str) -> List[Course]:
        return self.db.query(self.model).filter(self.model.level == level).all()

    def get_by_category(self, category: str) -> List[Course]:
        return self.db.query(self.model).filter(self.model.category == category).all()

    def get_by_access_type(self, access_type: str) -> List[Course]:
        return self.db.query(self.model).filter(self.model.access_type == access_type).all()
