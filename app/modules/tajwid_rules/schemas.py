from pydantic import BaseModel, ConfigDict
from typing import Optional

class TajwidRuleBase(BaseModel):
    """
    Base Pydantic model for TajwidRule, containing shared fields.
    """
    title: str
    description: Optional[str] = None
    example: Optional[str] = None

class TajwidRuleCreate(TajwidRuleBase):
    """
    Pydantic model for creating a new Tajwid rule.
    """
    pass

class TajwidRuleUpdate(BaseModel):
    """
    Pydantic model for updating an existing Tajwid rule.
    All fields are optional.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    example: Optional[str] = None

class TajwidRule(TajwidRuleBase):
    """
    Pydantic model for TajwidRule response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
