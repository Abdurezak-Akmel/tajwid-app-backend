from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database.session import get_db
from app.modules.roles.service import RoleService
from app.modules.roles.schemas import Role as RoleSchema, RoleCreate, RoleUpdate
from app.core.permissions import admin_required

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=List[RoleSchema])
def list_roles(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    """
    List all available roles (Admin only).
    """
    role_service = RoleService(db)
    return role_service.list_roles(skip=skip, limit=limit)

@router.post("/", response_model=RoleSchema, status_code=status.HTTP_201_CREATED)
def create_role(
    role_in: RoleCreate, 
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    """
    Create a new role (Admin only).
    """
    role_service = RoleService(db)
    return role_service.create_role(role_in)

@router.get("/{role_id}", response_model=RoleSchema)
def get_role(
    role_id: int, 
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    """
    Fetch a specific role by ID (Admin only).
    """
    role_service = RoleService(db)
    return role_service.get_role_by_id(role_id)

@router.put("/{role_id}", response_model=RoleSchema)
def update_role(
    role_id: int, 
    role_in: RoleUpdate, 
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    """
    Update an existing role (Admin only).
    """
    role_service = RoleService(db)
    return role_service.update_role(role_id, role_in)

@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
    role_id: int, 
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):
    """
    Delete a role from the system (Admin only).
    """
    role_service = RoleService(db)
    role_service.delete_role(role_id)
    return None
