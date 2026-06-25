from sqlalchemy.orm import Session
from typing import List, Optional
from app.modules.roles.repository import RoleRepository
from app.modules.roles.schemas import RoleCreate, RoleUpdate
from app.modules.roles.models import Role
from app.core.exceptions import ConflictError, NotFoundError

class RoleService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = RoleRepository(db)

    def create_role(self, role_in: RoleCreate) -> Role:
        """
        Create a new role after ensuring the name is unique.
        """
        if self.repository.get_by_name(role_in.name):
            raise ConflictError(detail=f"Role with name '{role_in.name}' already exists")
        
        return self.repository.create(role_in.model_dump())

    def get_role_by_id(self, role_id: int) -> Role:
        """
        Fetch a role by ID or raise NotFoundError.
        """
        role = self.repository.get(role_id)
        if not role:
            raise NotFoundError(detail="Role not found")
        return role

    def get_role_by_name(self, name: str) -> Optional[Role]:
        """
        Fetch a role by name.
        """
        return self.repository.get_by_name(name)

    def list_roles(self, skip: int = 0, limit: int = 100) -> List[Role]:
        """
        List all roles with pagination.
        """
        return self.repository.get_multi(skip=skip, limit=limit)

    def update_role(self, role_id: int, role_in: RoleUpdate) -> Role:
        """
        Update an existing role.
        """
        db_role = self.get_role_by_id(role_id)
        
        # Check uniqueness if name is being changed
        if role_in.name and role_in.name != db_role.name:
            if self.repository.get_by_name(role_in.name):
                raise ConflictError(detail=f"Role with name '{role_in.name}' already exists")

        return self.repository.update(db_role, role_in.model_dump(exclude_unset=True))

    def delete_role(self, role_id: int) -> None:
        """
        Delete a role from the system.
        """
        self.get_role_by_id(role_id)  # Verify existence
        self.repository.remove(role_id)
