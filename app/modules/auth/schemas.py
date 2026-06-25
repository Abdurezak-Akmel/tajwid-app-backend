from pydantic import BaseModel, EmailStr
from app.modules.users.schemas import UserCreate

class Token(BaseModel):
    """Schema for returning a JWT access token."""
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    """Schema for client login requests."""
    email: EmailStr
    password: str

class RegisterRequest(UserCreate):
    """Schema for user registration, inherits from UserCreate."""
    pass

class ForgotPasswordRequest(BaseModel):
    """Schema for forgot password requests."""
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    """Schema for password reset requests."""
    token: str
    new_password: str
