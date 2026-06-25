from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """
    Base Pydantic model for User, containing shared fields.
    """
    full_name: str
    email: EmailStr
    tg_username: Optional[str] = None
    role_id: int

class UserCreate(UserBase):
    """
    Pydantic model for creating a new user, includes password.
    """
    password: str
    is_verified: bool = False

class UserUpdate(BaseModel):
    """
    Pydantic model for updating an existing user.
    All fields are optional.
    """
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    tg_username: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None
    is_verified: Optional[bool] = None

class User(UserBase):
    """
    Pydantic model for user response, including the generated ID.
    """
    id: int
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
