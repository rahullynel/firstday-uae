"""
RelocationChecklistItem schema.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class RelocationChecklistItemBase(BaseModel):
    """Base checklist item schema."""

    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=500)
    category: str = Field(..., min_length=1, max_length=50)
    day_order: int = Field(..., ge=1, le=30)
    official_link: Optional[str] = Field(None, max_length=500)


class RelocationChecklistItemCreate(RelocationChecklistItemBase):
    """Schema for creating a checklist item."""

    city_id: int


class RelocationChecklistItemRead(RelocationChecklistItemBase):
    """Schema for reading checklist item data."""

    id: int
    city_id: int
    created_at: datetime

    class Config:
        from_attributes = True
