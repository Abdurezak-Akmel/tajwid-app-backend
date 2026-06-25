from sqlalchemy.orm import Session
from typing import List
from app.database.base_repository import BaseRepository
from app.modules.downloads.models import Download

class DownloadRepository(BaseRepository[Download]):
    def __init__(self, db: Session):
        super().__init__(Download, db)

    def get_user_downloads(self, user_id: int) -> List[Download]:
        return self.db.query(self.model).filter(self.model.user_id == user_id).all()

    def get_by_user_and_video(self, user_id: int, video_id: int) -> List[Download]:
        return self.db.query(self.model).filter(
            self.model.user_id == user_id, 
            self.model.video_id == video_id
        ).all()
