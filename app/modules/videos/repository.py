from sqlalchemy.orm import Session
from typing import List
from app.database.base_repository import BaseRepository
from app.modules.videos.models import Video

class VideoRepository(BaseRepository[Video]):
    def __init__(self, db: Session):
        super().__init__(Video, db)

    def get_by_course(self, course_id: int) -> List[Video]:
        return self.db.query(self.model).filter(self.model.course_id == course_id).all()

    def get_by_chapter(self, chapter_id: int) -> List[Video]:
        return self.db.query(self.model).filter(self.model.chapter_id == chapter_id).all()
