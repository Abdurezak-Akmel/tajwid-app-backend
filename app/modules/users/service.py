from sqlalchemy.orm import Session
from typing import List, Optional, Any
from app.modules.users.repository import UserRepository
from app.modules.users.schemas import UserCreate, UserUpdate
from app.modules.users.models import User
from app.core.security import get_password_hash
from app.core.exceptions import (
    ConflictError,
    NotFoundError
)

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    def create_user(self, user_in: UserCreate) -> User:
        """
        Create a new user after validating uniqueness and hashing the password.
        """
        # 1. Check if email already exists
        if self.repository.get_by_email(user_in.email):
            raise ConflictError(detail="Email already registered")

        # 2. Check if telegram username already exists (if provided)
        if user_in.tg_username and self.repository.get_by_tg_username(user_in.tg_username):
            raise ConflictError(detail="Telegram username already taken")

        # 3. Hash the password
        user_data = user_in.model_dump()
        user_data["password_hash"] = get_password_hash(user_data.pop("password"))

        # 4. Create and return the user
        return self.repository.create(user_data)

    def get_user_by_id(self, user_id: int) -> User:
        """
        Fetch a user by ID or raise an exception.
        """
        user = self.repository.get(user_id)
        if not user:
            raise NotFoundError(detail="User not found")
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Fetch a user by email.
        """
        return self.repository.get_by_email(email)

    def list_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """
        List all users with pagination.
        """
        return self.repository.get_multi(skip=skip, limit=limit)

    def update_user(self, user_id: int, user_in: UserUpdate) -> User:
        """
        Update user details, including password hashing if changed.
        """
        db_user = self.get_user_by_id(user_id)
        
        update_data = user_in.model_dump(exclude_unset=True)
        
        if "password" in update_data:
            update_data["password_hash"] = get_password_hash(update_data.pop("password"))
            
        return self.repository.update(db_user, update_data)

    def delete_user(self, user_id: int) -> None:
        """
        Remove a user from the system.
        """
        db_user = self.get_user_by_id(user_id)
        self.repository.remove(user_id)

    def verify_user(self, user_id: int) -> User:
        """
        Mark a user as verified.
        """
        db_user = self.get_user_by_id(user_id)
        return self.repository.update(db_user, {"is_verified": True})
