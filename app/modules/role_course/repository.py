from sqlalchemy.orm import Session
from typing import List
from app.database.base_repository import BaseRepository
from app.modules.role_course.models import RoleCourse

class RoleCourseRepository(BaseRepository[RoleCourse]):
    def __init__(self, db: Session):
        super().__init__(RoleCourse, db)

    def get_by_role(self, role_id: int) -> List[RoleCourse]:
        return self.db.query(self.model).filter(self.model.role_id == role_id).all()

    def get_by_course(self, course_id: int) -> List[RoleCourse]:
        return self.db.query(self.model).filter(self.model.course_id == course_id).all()

    def get_by_role_and_course(self, role_id: int, course_id: int) -> List[RoleCourse]:
        return self.db.query(self.model).filter(
            self.model.role_id == role_id,
            self.model.course_id == course_id
        ).all()
