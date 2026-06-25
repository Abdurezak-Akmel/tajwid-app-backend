from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional
from app.database.base_repository import BaseRepository
from app.modules.access_requests.models import AccessRequest

class AccessRequestRepository(BaseRepository[AccessRequest]):
    def __init__(self, db: Session):
        super().__init__(AccessRequest, db)

    def get_by_status(self, status: str, skip: int = 0, limit: int = 100) -> List[AccessRequest]:
        return self.db.query(self.model).filter(self.model.status == status).offset(skip).limit(limit).all()

    def get_by_user_id(self, user_id: int) -> List[AccessRequest]:
        return self.db.query(self.model).filter(self.model.user_id == user_id).all()

    def get_by_course_id(self, course_id: int) -> List[AccessRequest]:
        return self.db.query(self.model).filter(self.model.course_id == course_id).all()

    def get_by_user_and_course(self, user_id: int, course_id: int) -> Optional[AccessRequest]:
        return self.db.query(self.model).filter(
            and_(
                self.model.user_id == user_id,
                self.model.course_id == course_id
            )
        ).first()

    def update_status(self, request_id: int, status: str) -> Optional[AccessRequest]:
        db_obj = self.get(request_id)
        if db_obj:
            db_obj.status = status
            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj

    def get_pending_requests_count(self) -> int:
        return self.db.query(self.model).filter(self.model.status == "pending").count()
