from pydantic import BaseModel, ConfigDict
from typing import Optional

class NotificationBase(BaseModel):
    """
    Base Pydantic model for Notification, containing shared fields.
    """
    user_id: int
    title: str
    details: Optional[str] = None

class NotificationCreate(NotificationBase):
    """
    Pydantic model for creating a new notification.
    """
    pass

class NotificationUpdate(BaseModel):
    """
    Pydantic model for updating an existing notification.
    All fields are optional.
    """
    title: Optional[str] = None
    details: Optional[str] = None

class Notification(NotificationBase):
    """
    Pydantic model for notification response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
