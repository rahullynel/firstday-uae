"""
City schemas - request/response for city data.
"""

from datetime import datetime
from pydantic import BaseModel, Field


class CityBase(BaseModel):
    """Base city schema with common fields."""

    name: str = Field(..., min_length=1, max_length=100)
    slug: str = Field(..., min_length=1, max_length=100)
    country: str = Field(default="UAE", max_length=100)
    currency: str = Field(default="AED", max_length=10)


class CityCreate(CityBase):
    """Schema for creating a new city."""

    pass


class CityRead(CityBase):
    """Schema for reading city data (response)."""

    id: int
    created_at: datetime

    class Config:
        from_attributes = True
