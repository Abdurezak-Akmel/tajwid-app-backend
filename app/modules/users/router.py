from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.modules.users.service import UserService
from app.modules.users.schemas import User as UserSchema, UserUpdate
from app.modules.users.models import User
from app.core.dependencies import get_current_user
from app.core.permissions import admin_required

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserSchema)
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Get profile details of the currently logged-in user.
    """
    return current_user

@router.put("/me", response_model=UserSchema)
def update_current_user(
    user_in: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update profile details of the currently logged-in user.
    """
    user_service = UserService(db)
    return user_service.update_user(current_user.id, user_in)

# --- Admin Only Routes ---

@router.get("/", response_model=List[UserSchema], dependencies=[Depends(admin_required)])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List all users (Admin only).
    """
    user_service = UserService(db)
    return user_service.list_users(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserSchema, dependencies=[Depends(admin_required)])
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Fetch a specific user by ID (Admin only).
    """
    user_service = UserService(db)
    return user_service.get_user_by_id(user_id)

@router.put("/{user_id}", response_model=UserSchema, dependencies=[Depends(admin_required)])
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    """
    Update details of a specific user (Admin only).
    """
    user_service = UserService(db)
    return user_service.update_user(user_id, user_in)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(admin_required)])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user from the system (Admin only).
    """
    user_service = UserService(db)
    user_service.delete_user(user_id)
    return None
