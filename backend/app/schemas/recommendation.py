"""
Recommendation request/response schemas.
"""

from typing import Optional
from pydantic import BaseModel, Field


class ScoreBreakdown(BaseModel):
    """Breakdown of recommendation score by category."""

    affordability_score: float = Field(..., ge=0, le=100, description="Affordability score (0-100)")
    commute_score: float = Field(..., ge=0, le=100, description="Commute score (0-100)")
    lifestyle_score: float = Field(..., ge=0, le=100, description="Lifestyle compatibility score (0-100)")
    walkability_score: float = Field(..., ge=0, le=100, description="Walkability score (0-100)")

    class Config:
        json_schema_extra = {
            "example": {
                "affordability_score": 85.0,
                "commute_score": 72.5,
                "lifestyle_score": 90.0,
                "walkability_score": 80.0,
            }
        }


class NeighborhoodRecommendation(BaseModel):
    """A single neighborhood recommendation with detailed scoring."""

    id: int
    name: str
    slug: str
    avg_rent_min: Optional[float] = None
    avg_rent_max: Optional[float] = None
    walkability_score: Optional[float] = None
    family_score: Optional[float] = None
    nightlife_score: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = None
    
    score_breakdown: ScoreBreakdown
    total_score: float = Field(..., ge=0, le=100, description="Overall recommendation score")
    top_reasons: list[str] = Field(default_factory=list, description="Top 3-5 reasons why recommended")
    summary: str = Field(..., description="Human-readable summary of the recommendation")

    class Config:
        from_attributes = True


class RecommendationRequest(BaseModel):
    """Request schema for neighborhood recommendations."""

    city_slug: str = Field(..., min_length=1, max_length=100, description="City slug (e.g., 'abu-dhabi')")
    work_location_text: str = Field(..., min_length=1, max_length=200, description="Work location address/name")
    monthly_salary: float = Field(..., gt=0, description="Monthly salary in AED")
    monthly_budget: Optional[float] = Field(None, gt=0, description="Monthly housing budget in AED")
    lifestyle: Optional[str] = Field(None, max_length=50, description="e.g., 'budget', 'balanced', 'premium'")
    transport_preference: Optional[str] = Field(None, max_length=50, description="e.g., 'car', 'public', 'mixed'")
    preferred_commute_minutes: Optional[int] = Field(None, ge=5, le=120, description="Maximum commute time in minutes")

    class Config:
        json_schema_extra = {
            "example": {
                "city_slug": "abu-dhabi",
                "work_location_text": "Hamdan Street",
                "monthly_salary": 15000,
                "monthly_budget": 3000,
                "lifestyle": "balanced",
                "transport_preference": "car",
                "preferred_commute_minutes": 30,
            }
        }


class RecommendedNeighborhood(BaseModel):
    """Individual recommended neighborhood (legacy, use NeighborhoodRecommendation)."""

    id: int
    name: str
    slug: str
    avg_rent_min: Optional[float] = None
    avg_rent_max: Optional[float] = None
    walkability_score: Optional[float] = None
    family_score: Optional[float] = None
    nightlife_score: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = None
    match_score: float = Field(..., ge=0, le=100, description="Recommendation match percentage")
    reason: str = Field(..., description="Why this neighborhood was recommended")

    class Config:
        from_attributes = True


class RecommendationResponse(BaseModel):
    """Response schema for neighborhood recommendations."""

    city_slug: str = Field(..., description="City slug for the recommendations")
    work_location: str = Field(..., description="Work location requested")
    work_location_found: bool = Field(default=False, description="Whether exact work location was found in system")
    salary_input: float = Field(..., gt=0, description="Monthly salary provided")
    budget_input: Optional[float] = Field(None, gt=0, description="Monthly budget provided")
    lifestyle_input: Optional[str] = Field(None, description="Lifestyle preference provided")
    transport_input: Optional[str] = Field(None, description="Transport preference provided")
    
    recommendations: list[NeighborhoodRecommendation] = Field(default_factory=list, description="Ranked neighborhood recommendations")
    total_matches: int = Field(default=0, ge=0, description="Total number of matched neighborhoods")
    summary: str = Field(..., description="Human-readable summary of recommendations")

