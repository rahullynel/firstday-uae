"""
Relocation checklist API schemas.
"""

from datetime import datetime
from typing import Optional, List
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


class ChecklistItem(BaseModel):
    """Checklist item for API response."""

    id: int
    title: str
    description: Optional[str]
    category: str
    day_order: int
    official_link: Optional[str]

    class Config:
        from_attributes = True


class ChecklistGroup(BaseModel):
    """Grouped checklist items by time period."""

    period: str  # "Day 1-3", "Week 1", "After settling in"
    items: List[ChecklistItem]


class ChecklistRequest(BaseModel):
    """Request to fetch relocation checklist."""

    city_slug: Optional[str] = Field(None, description="Optionally filter by city slug")


class ChecklistResponse(BaseModel):
    """Response containing grouped checklist items."""

    city_name: Optional[str]
    city_slug: Optional[str]
    total_items: int
    groups: List[ChecklistGroup]
