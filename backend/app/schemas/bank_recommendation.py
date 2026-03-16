"""
Bank recommendation request/response schemas.
"""

from typing import Optional
from pydantic import BaseModel, Field


class BankRecommendationRequest(BaseModel):
    """Request schema for bank recommendations."""

    city_id: int = Field(..., description="City ID")
    monthly_salary: float = Field(..., gt=0, description="Monthly salary in AED")
    priorities: Optional[list[str]] = Field(
        None,
        description="Bank selection priorities: 'digital', 'remittance', 'branch-network', 'salary-requirements'",
    )
    budget: Optional[float] = Field(None, gt=0, description="Monthly budget for banking services")

    class Config:
        json_schema_extra = {
            "example": {
                "city_id": 1,
                "monthly_salary": 15000,
                "priorities": ["digital", "remittance"],
                "budget": 100,
            }
        }


class BankWithRecommendationScore(BaseModel):
    """Bank with recommendation score."""

    id: int
    name: str
    slug: str
    min_salary_requirement: Optional[float]
    digital_score: Optional[float]
    remittance_score: Optional[float]
    branch_network_score: Optional[float]
    website_url: Optional[str]
    description: Optional[str]
    recommendation_score: float = Field(..., ge=0, le=100, description="Match score")
    matching_priorities: list[str] = Field(default_factory=list, description="Which priorities this bank matches")
    key_benefits: list[str] = Field(default_factory=list, description="Key benefits for this user")

    class Config:
        from_attributes = True


class BankRecommendationResponse(BaseModel):
    """Response schema for bank recommendations."""

    city_id: int
    city_name: str
    salary_input: float
    recommended_banks: list[BankWithRecommendationScore] = []
    total_matches: int = Field(default=0, ge=0)
    summary: str = Field(..., description="Human-readable summary of recommendations")
    top_reasons: list[str] = Field(default_factory=list, description="Top reasons for recommendations")
