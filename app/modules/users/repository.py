from sqlalchemy.orm import Session
from typing import Optional
from app.database.base_repository import BaseRepository
from app.modules.users.models import User

class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(self.model).filter(self.model.email == email).first()

    def get_by_tg_username(self, tg_username: str) -> Optional[User]:
        return self.db.query(self.model).filter(self.model.tg_username == tg_username).first()
