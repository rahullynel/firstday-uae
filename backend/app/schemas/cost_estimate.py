"""
Cost estimate request/response schemas.
"""

from typing import Optional
from pydantic import BaseModel, Field


class CostEstimateRequest(BaseModel):
    """Request schema for cost of living estimates."""

    city_id: int = Field(..., description="City ID")
    neighborhood_ids: Optional[list[int]] = Field(None, description="Optional: specific neighborhoods to estimate")
    monthly_salary: float = Field(..., gt=0, description="Monthly salary in AED")
    family_size: Optional[int] = Field(None, ge=1, le=10, description="Number of people in household")
    lifestyle: Optional[str] = Field(None, max_length=50, description="e.g., 'budget', 'comfortable', 'luxury'")

    class Config:
        json_schema_extra = {
            "example": {
                "city_id": 1,
                "monthly_salary": 15000,
                "family_size": 4,
                "lifestyle": "comfortable",
            }
        }


class CostBreakdown(BaseModel):
    """Detailed cost breakdown for a location."""

    category: str
    estimated_cost: float = Field(..., ge=0, description="Estimated monthly cost in AED")
    percentage_of_salary: float = Field(..., ge=0, le=100, description="Percentage of salary")
    notes: Optional[str] = None


class LocationCostEstimate(BaseModel):
    """Cost estimate for a specific location."""

    city_id: int
    city_name: str
    neighborhood_id: Optional[int] = None
    neighborhood_name: Optional[str] = None
    monthly_rent: float = Field(..., ge=0, description="Estimated monthly rent in AED")
    monthly_expenses: float = Field(..., ge=0, description="Estimated monthly other expenses")
    total_monthly_cost: float = Field(..., ge=0, description="Total monthly cost")
    salary_remaining: float = Field(..., description="Monthly salary after living costs")
    affordability: str = Field(..., description="'affordable', 'moderate', 'tight' or 'unaffordable'")
    breakdown: list[CostBreakdown] = []


class CostEstimateResponse(BaseModel):
    """Response schema for cost estimates."""

    salary_input: float
    estimates: list[LocationCostEstimate] = []
    recommendations: list[str] = []
    summary: str = Field(..., description="Human-readable summary of costs")

    class Config:
        json_schema_extra = {
            "example": {
                "salary_input": 15000,
                "estimates": [
                    {
                        "city_id": 1,
                        "city_name": "Abu Dhabi",
                        "neighborhood_name": "Downtown",
                        "monthly_rent": 2500,
                        "monthly_expenses": 2000,
                        "total_monthly_cost": 4500,
                        "salary_remaining": 10500,
                        "affordability": "affordable",
                    }
                ],
                "recommendations": ["Community", "Downtown area is affordable"],
                "summary": "You can comfortably afford living in Abu Dhabi",
            }
        }
