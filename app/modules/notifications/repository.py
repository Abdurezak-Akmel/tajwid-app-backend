from sqlalchemy.orm import Session
from typing import List
from app.database.base_repository import BaseRepository
from app.modules.notifications.models import Notification

class NotificationRepository(BaseRepository[Notification]):
    def __init__(self, db: Session):
        super().__init__(Notification, db)

    def get_user_notifications(self, user_id: int) -> List[Notification]:
        return self.db.query(self.model).filter(self.model.user_id == user_id).all()
