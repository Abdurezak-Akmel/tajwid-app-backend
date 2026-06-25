from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.core.config import settings
from app.core.exceptions import UnauthenticatedError
from app.modules.users.service import UserService
from app.modules.users.models import User

# This tells FastAPI where the login endpoint is for the Swagger UI Authorize button
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login", auto_error=False)

def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency to validate the JWT token and return the current user.
    """
    if not token:
        raise UnauthenticatedError(detail="Missing authorization token")

    try:
        # 1. Decode the JWT token
        payload = jwt.decode(
            token, 
            settings.secret_key, 
            algorithms=[settings.algorithm]
        )
        email: str = payload.get("sub")
        
        if email is None:
            raise UnauthenticatedError(detail="Invalid token payload")
            
    except JWTError:
        raise UnauthenticatedError(detail="Could not validate credentials")
    
    # 2. Fetch the user from the database
    user_service = UserService(db)
    user = user_service.get_user_by_email(email)
    
    if user is None:
        raise UnauthenticatedError(detail="User not found")
        
    return user
