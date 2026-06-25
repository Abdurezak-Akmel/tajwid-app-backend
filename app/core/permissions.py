from fastapi import Depends
from typing import List
from app.core.exceptions import ForbiddenError
from app.core.dependencies import get_current_user
from app.modules.users.models import User

def admin_required(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency to ensure the current user has an 'admin' role.
    """
    # Assuming 'role' relationship exists and has a 'name' attribute
    if not current_user.role or current_user.role.name.lower() != "admin":
        raise ForbiddenError(detail="Admin access required")
    return current_user

class RoleChecker:
    """
    A reusable dependency for checking multiple allowed roles.
    Example: Depends(RoleChecker(["admin", "teacher"]))
    """
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = [role.lower() for role in allowed_roles]

    def __call__(self, current_user: User = Depends(get_current_user)) -> User:
        if not current_user.role or current_user.role.name.lower() not in self.allowed_roles:
            raise ForbiddenError(
                detail=f"Access denied. Required roles: {', '.join(self.allowed_roles)}"
            )
        return current_user
