"""
CostIndex schema.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CostIndexBase(BaseModel):
    """Base cost index schema."""

    rent_index: Optional[float] = Field(None, ge=0)
    grocery_index: Optional[float] = Field(None, ge=0)
    transport_index: Optional[float] = Field(None, ge=0)
    utility_index: Optional[float] = Field(None, ge=0)
    dining_index: Optional[float] = Field(None, ge=0)
    misc_index: Optional[float] = Field(None, ge=0)


class CostIndexCreate(CostIndexBase):
    """Schema for creating a cost index."""

    city_id: int


class CostIndexRead(CostIndexBase):
    """Schema for reading cost index data."""

    id: int
    city_id: int
    last_updated: datetime

    class Config:
        from_attributes = True


class CostIndexSummary(BaseModel):
    """Summary cost index for frontend display."""

    city_id: int
    city_name: str
    overall_index: float = Field(..., description="Average of all indices")
    rent_index: Optional[float] = None
    grocery_index: Optional[float] = None
    transport_index: Optional[float] = None
    utility_index: Optional[float] = None
    dining_index: Optional[float] = None
    misc_index: Optional[float] = None
    last_updated: datetime
