from sqlalchemy.orm import Session
from typing import Optional
from app.database.base_repository import BaseRepository
from app.modules.roles.models import Role

class RoleRepository(BaseRepository[Role]):
    def __init__(self, db: Session):
        super().__init__(Role, db)

    def get_by_name(self, name: str) -> Optional[Role]:
        return self.db.query(self.model).filter(self.model.name == name).first()
