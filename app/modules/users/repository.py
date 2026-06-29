from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from app.database.base_repository import BaseRepository
from app.modules.users.models import User

class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(self.model).filter(self.model.email == email).first()

    def get_by_tg_username(self, tg_username: str) -> Optional[User]:
        return self.db.query(self.model).filter(self.model.tg_username == tg_username).first()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.get(user_id)

    def list_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self.get_multi(skip=skip, limit=limit)

    def create_user(self, user_data: Dict[str, Any]) -> User:
        return self.create(user_data)

    def update_user(self, db_user: User, update_data: Dict[str, Any]) -> User:
        return self.update(db_user, update_data)

    def delete_user(self, user_id: int) -> User:
        return self.remove(user_id)

    def verify_user(self, db_user: User) -> User:
        return self.update(db_user, {"is_verified": True})
