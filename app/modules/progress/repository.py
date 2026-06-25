from sqlalchemy.orm import Session
from typing import Optional
from app.database.base_repository import BaseRepository
from app.modules.progress.models import Progress

class ProgressRepository(BaseRepository[Progress]):
    def __init__(self, db: Session):
        super().__init__(Progress, db)

    def get_user_progress(self, user_id: int) -> Optional[Progress]:
        return self.db.query(self.model).filter(self.model.user_id == user_id).first()

    def update_user_progress(self, user_id: int, progress_data: dict) -> Optional[Progress]:
        db_obj = self.get_user_progress(user_id)
        if db_obj:
            return self.update(db_obj, progress_data)
        return self.create({"user_id": user_id, **progress_data})
