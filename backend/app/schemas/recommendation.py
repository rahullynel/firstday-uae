"""
Recommendation request/response schemas.
"""

from typing import Optional
from pydantic import BaseModel, Field


class RecommendationRequest(BaseModel):
    """Request schema for neighborhood recommendations."""

    work_location: str = Field(..., min_length=1, max_length=200, description="Work location address/name")
    city_id: int = Field(..., description="City ID to search in")
    monthly_salary: float = Field(..., gt=0, description="Monthly salary in AED")
    monthly_budget: Optional[float] = Field(None, gt=0, description="Monthly housing budget in AED")
    lifestyle: Optional[str] = Field(None, max_length=50, description="e.g., 'family', 'young-professional', 'nightlife'")
    transport_preference: Optional[str] = Field(None, max_length=50, description="e.g., 'car', 'public', 'mixed'")
    preferred_commute_minutes: Optional[int] = Field(None, ge=5, le=120, description="Maximum commute time in minutes")

    class Config:
        json_schema_extra = {
            "example": {
                "work_location": "DIFC, Dubai",
                "city_id": 1,
                "monthly_salary": 15000,
                "monthly_budget": 3000,
                "lifestyle": "family",
                "transport_preference": "car",
                "preferred_commute_minutes": 30,
            }
        }


class RecommendedNeighborhood(BaseModel):
    """Individual recommended neighborhood."""

    id: int
    name: str
    slug: str
    avg_rent_min: Optional[float]
    avg_rent_max: Optional[float]
    walkability_score: Optional[float]
    family_score: Optional[float]
    nightlife_score: Optional[float]
    latitude: Optional[float]
    longitude: Optional[float]
    description: Optional[str]
    match_score: float = Field(..., ge=0, le=100, description="Recommendation match percentage")
    reason: str = Field(..., description="Why this neighborhood was recommended")

    class Config:
        from_attributes = True


class RecommendationResponse(BaseModel):
    """Response schema for neighborhood recommendations."""

    work_location: str
    recommended_neighborhoods: list[RecommendedNeighborhood] = []
    total_matches: int = Field(default=0, ge=0)
    search_summary: str = Field(..., description="Human-readable summary of recommendations")
