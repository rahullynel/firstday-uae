"""
Cost estimation request/response schemas.
"""

from typing import Optional
from pydantic import BaseModel, Field


class CostEstimateRequest(BaseModel):
    """Request schema for cost-of-living estimates."""

    city_slug: str = Field(..., min_length=1, max_length=100, description="City slug (e.g., 'abu-dhabi')")
    monthly_salary: float = Field(..., gt=0, description="Monthly salary in AED")
    lifestyle: str = Field(
        default="balanced",
        description="Lifestyle preference: 'budget', 'balanced', or 'premium'",
        pattern="^(budget|balanced|premium)$"
    )
    transport_preference: str = Field(
        default="car",
        description="Transport mode: 'walk', 'public', or 'car'",
        pattern="^(walk|public|car)$"
    )
    neighborhood_slug: Optional[str] = Field(
        None,
        max_length=100,
        description="Optional neighborhood slug for specific neighborhood rent"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "city_slug": "abu-dhabi",
                "monthly_salary": 15000,
                "lifestyle": "balanced",
                "transport_preference": "car",
                "neighborhood_slug": "hamdan-street",
            }
        }


class CostBreakdown(BaseModel):
    """Detailed breakdown of monthly costs."""

    estimated_rent: float = Field(..., ge=0, description="Monthly rent in AED")
    estimated_groceries: float = Field(..., ge=0, description="Monthly groceries in AED")
    estimated_transport: float = Field(..., ge=0, description="Monthly transport in AED")
    estimated_utilities: float = Field(..., ge=0, description="Monthly utilities in AED")
    estimated_dining: float = Field(..., ge=0, description="Monthly dining/eating out in AED")
    estimated_miscellaneous: float = Field(..., ge=0, description="Monthly miscellaneous in AED")
    estimated_total_monthly_cost: float = Field(..., ge=0, description="Total monthly expenses in AED")

    class Config:
        json_schema_extra = {
            "example": {
                "estimated_rent": 4000.0,
                "estimated_groceries": 1200.0,
                "estimated_transport": 450.0,
                "estimated_utilities": 520.0,
                "estimated_dining": 1200.0,
                "estimated_miscellaneous": 500.0,
                "estimated_total_monthly_cost": 7870.0,
            }
        }


class CostEstimateResponse(BaseModel):
    """Response schema for cost-of-living estimates."""

    city_slug: str
    neighborhood_slug: Optional[str] = None
    monthly_salary: float
    lifestyle: str
    transport_preference: str

    cost_breakdown: CostBreakdown
    estimated_savings: float = Field(..., description="Monthly savings (salary - total cost)")
    savings_percentage: float = Field(..., description="Savings as percentage of salary (can be negative)")
    comfort_score: float = Field(..., ge=0, le=100, description="Comfort score based on savings (0-100)")
    explanation: str = Field(..., description="Human-readable explanation of the estimate")

    class Config:
        json_schema_extra = {
            "example": {
                "city_slug": "abu-dhabi",
                "neighborhood_slug": "hamdan-street",
                "monthly_salary": 15000.0,
                "lifestyle": "balanced",
                "transport_preference": "car",
                "cost_breakdown": {
                    "estimated_rent": 4200.0,
                    "estimated_groceries": 1200.0,
                    "estimated_transport": 500.0,
                    "estimated_utilities": 520.0,
                    "estimated_dining": 1200.0,
                    "estimated_miscellaneous": 600.0,
                    "estimated_total_monthly_cost": 8220.0,
                },
                "estimated_savings": 6780.0,
                "savings_percentage": 45.2,
                "comfort_score": 90.4,
                "explanation": "With a 45.2% savings rate, you can comfortably afford this lifestyle in Hamdan Street. You'll have ₱6,780/month for emergencies and investments.",
            }
        }
