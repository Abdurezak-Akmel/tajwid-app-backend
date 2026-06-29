from fastapi import APIRouter, Depends, status, BackgroundTasks
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.modules.auth.service import AuthService
from app.modules.auth.schemas import (
    LoginRequest, 
    Token, 
    RegisterRequest, 
    ForgotPasswordRequest, 
    ResetPasswordRequest
)
from app.modules.users.schemas import User as UserSchema
from app.core.mail import send_reset_password_email, send_verification_email

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def register(
    user_in: RegisterRequest, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Register a new user in the system.
    Sends a verification email to non-admin users.
    """
    auth_service = AuthService(db)
    user = auth_service.register(user_in)
    
    # 1 is Admin Role ID
    if user.role_id != 1:
        token = auth_service.generate_verification_token(user.email)
        background_tasks.add_task(send_verification_email, user.email, token)
        
    return user

@router.get("/verify")
def verify_email(token: str, db: Session = Depends(get_db)):
    """
    Verify a user's email address using a token.
    """
    auth_service = AuthService(db)
    return auth_service.verify_email(token)

@router.post("/login", response_model=Token)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate a user and return a JWT access token.
    """
    auth_service = AuthService(db)
    return auth_service.login(login_data.model_dump())

@router.post("/forgot-password")
async def forgot_password(
    request: ForgotPasswordRequest, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Send a password reset link (via token) to the user's email.
    """
    auth_service = AuthService(db)
    token = auth_service.forgot_password(request.email)
    
    # Add email sending to background tasks
    background_tasks.add_task(send_reset_password_email, request.email, token)
    
    return {"message": "If the email exists, a reset token has been sent."}

@router.post("/reset-password")
def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    """
    Reset user password using a valid reset token.
    """
    auth_service = AuthService(db)
    return auth_service.reset_password(request.token, request.new_password)

@router.post("/logout")
def logout():
    """
    Client-side logout (token disposal). 
    Server-side token blacklisting can be implemented here.
    """
    return {"message": "Logged out successfully"}

