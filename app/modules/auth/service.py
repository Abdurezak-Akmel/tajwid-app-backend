from sqlalchemy.orm import Session
from datetime import timedelta
from app.modules.users.service import UserService
from app.modules.users.schemas import UserCreate, UserUpdate
from app.core.security import verify_password, create_access_token
from app.core.exceptions import UnauthenticatedError, NotFoundError, BadRequestError
from app.core.config import settings
from jose import jwt, JWTError

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_service = UserService(db)

    def register(self, user_in: UserCreate):
        """
        Register a new user.
        """
        return self.user_service.create_user(user_in)

    def authenticate_user(self, email: str, password: str):
        """
        Verify user credentials.
        """
        user = self.user_service.get_user_by_email(email)
        if not user:
            return None
            
        if not verify_password(password, user.password_hash):
            return None
            
        return user

    def login(self, login_data: dict) -> dict:
        """
        Handle user login and return an access token.
        """
        user = self.authenticate_user(
            email=login_data.get("email"), 
            password=login_data.get("password")
        )
        
        if not user:
            raise UnauthenticatedError(detail="Invalid email or password")
        
        access_token = create_access_token(data={"sub": user.email})
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    def logout(self, token: str):
        """
        Log out the user. 
        In a stateless JWT system, tokens are usually cleared on the client side.
        Server-side logout requires a blacklisting mechanism (e.g., Redis).
        """
        # TODO: Implement token blacklisting if Redis is available
        return {"message": "Successfully logged out"}

    def forgot_password(self, email: str) -> str:
        """
        Generate a password reset token.
        """
        user = self.user_service.get_user_by_email(email)
        if not user:
            raise NotFoundError(detail="User with this email does not exist")
        
        # Create a short-lived token specifically for password reset
        reset_token = create_access_token(
            data={"sub": user.email, "purpose": "password_reset"},
            expires_delta=timedelta(minutes=15)
        )
        
        return reset_token

    def reset_password(self, token: str, new_password: str):
        """
        Validate reset token and update user password.
        """
        try:
            payload = jwt.decode(
                token, 
                settings.secret_key, 
                algorithms=[settings.algorithm]
            )
            email: str = payload.get("sub")
            purpose: str = payload.get("purpose")
            
            if email is None or purpose != "password_reset":
                raise BadRequestError(detail="Invalid or expired reset token")
                
        except JWTError:
            raise BadRequestError(detail="Invalid or expired reset token")
            
        user = self.user_service.get_user_by_email(email)
        if not user:
            raise NotFoundError(detail="User not found")
            
    # --- Email Verification ---

    def generate_verification_token(self, email: str) -> str:
        """
        Generate a token for email verification.
        """
        return create_access_token(
            data={"sub": email, "purpose": "email_verification"},
            expires_delta=timedelta(days=1)  # Verification tokens usually last longer
        )

    def verify_email(self, token: str):
        """
        Validate verification token and mark user as verified.
        """
        try:
            payload = jwt.decode(
                token, 
                settings.secret_key, 
                algorithms=[settings.algorithm]
            )
            email: str = payload.get("sub")
            purpose: str = payload.get("purpose")
            
            if email is None or purpose != "email_verification":
                raise BadRequestError(detail="Invalid or expired verification token")
                
        except JWTError:
            raise BadRequestError(detail="Invalid or expired verification token")
            
        user = self.user_service.get_user_by_email(email)
        if not user:
            raise NotFoundError(detail="User not found")
            
        if user.is_verified:
            return {"message": "Email already verified"}

        # Use the verify_user method from UserService
        self.user_service.verify_user(user.id)
        
        return {"message": "Email verified successfully"}
