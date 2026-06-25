from typing import Generic, TypeVar, Type, Optional, List, Any, Dict, Union
from sqlalchemy.orm import Session
from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: Any) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def create(self, obj_in: Dict[str, Any]) -> ModelType:
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj: ModelType, obj_in: Union[Dict[str, Any], Any]) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.__dict__
            
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])
        
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def remove(self, id: Any) -> ModelType:
        obj = self.db.query(self.model).get(id)
        self.db.delete(obj)
        self.db.commit()
        return obj
