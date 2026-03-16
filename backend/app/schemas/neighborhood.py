"""
Neighborhood and Amenity schemas.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class AmenityBase(BaseModel):
    """Base amenity schema."""

    name: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=50)
    address: Optional[str] = Field(None, max_length=255)
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    rating: Optional[float] = Field(None, ge=0, le=5)
    source_url: Optional[str] = Field(None, max_length=500)


class AmenityRead(AmenityBase):
    """Schema for reading amenity data."""

    id: int
    neighborhood_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class NeighborhoodBase(BaseModel):
    """Base neighborhood schema."""

    name: str = Field(..., min_length=1, max_length=100)
    slug: str = Field(..., min_length=1, max_length=100)
    avg_rent_min: Optional[float] = Field(None, ge=0)
    avg_rent_max: Optional[float] = Field(None, ge=0)
    walkability_score: Optional[float] = Field(None, ge=0, le=100)
    noise_score: Optional[float] = Field(None, ge=0, le=100)
    family_score: Optional[float] = Field(None, ge=0, le=100)
    nightlife_score: Optional[float] = Field(None, ge=0, le=100)
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = Field(None, max_length=500)


class NeighborhoodCreate(NeighborhoodBase):
    """Schema for creating a neighborhood."""

    city_id: int


class NeighborhoodRead(NeighborhoodBase):
    """Schema for reading neighborhood data."""

    id: int
    city_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class NeighborhoodWithAmenities(NeighborhoodRead):
    """Neighborhood with nested amenities."""

    amenities: list[AmenityRead] = []
