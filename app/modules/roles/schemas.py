from pydantic import BaseModel, ConfigDict
from typing import Optional, Any

class RoleBase(BaseModel):
    """
    Base Pydantic model for Role, containing shared fields.
    """
    name: str
    access_details: Optional[dict[str, Any]] = None

class RoleCreate(RoleBase):
    """
    Pydantic model for creating a new role.
    """
    pass

class RoleUpdate(BaseModel):
    """
    Pydantic model for updating an existing role.
    All fields are optional.
    """
    name: Optional[str] = None
    access_details: Optional[dict[str, Any]] = None

class Role(RoleBase):
    """
    Pydantic model for role response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
