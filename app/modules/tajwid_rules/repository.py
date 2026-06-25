from sqlalchemy.orm import Session
from app.database.base_repository import BaseRepository
from app.modules.tajwid_rules.models import TajwidRule

class TajwidRuleRepository(BaseRepository[TajwidRule]):
    def __init__(self, db: Session):
        super().__init__(TajwidRule, db)
