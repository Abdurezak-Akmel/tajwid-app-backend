from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AccessRequestBase(BaseModel):
    """
    Base Pydantic model for AccessRequest, containing shared fields.
    """
    user_id: int
    course_id: int
    amount: float
    receipt_file_url: Optional[str] = None
    receipt_file_size: Optional[int] = None
    status: str = "pending"

class AccessRequestCreate(AccessRequestBase):
    """
    Pydantic model for creating a new access request.
    """
    pass

class AccessRequestUpdate(BaseModel):
    """
    Pydantic model for updating an existing access request.
    All fields are optional.
    """
    status: Optional[str] = None
    amount: Optional[float] = None
    receipt_file_url: Optional[str] = None
    receipt_file_size: Optional[int] = None

class AccessRequest(AccessRequestBase):
    """
    Pydantic model for access request response, including the generated ID and timestamps.
    """
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
