"""
Bank recommendation request/response schemas.
"""

from typing import Optional
from pydantic import BaseModel, Field


class BankRecommendationRequest(BaseModel):
    """Request schema for bank recommendations."""

    monthly_salary: float = Field(..., gt=0, description="Monthly salary in AED")
    remittance_need: str = Field(
        default="low",
        description="Remittance importance: 'low', 'medium', or 'high'",
        pattern="^(low|medium|high)$"
    )
    prefers_digital_banking: bool = Field(
        default=False,
        description="Whether digital banking capabilities are important"
    )
    wants_credit_card_rewards: bool = Field(
        default=False,
        description="Whether credit card rewards/offers are important"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "monthly_salary": 15000,
                "remittance_need": "high",
                "prefers_digital_banking": True,
                "wants_credit_card_rewards": True,
            }
        }


class ActiveBankOffer(BaseModel):
    """An active offer from a bank."""

    title: str = Field(..., description="Offer title")
    description: str = Field(..., description="Offer description")
    source_url: Optional[str] = Field(None, description="Link to offer details")


class BankRecommendationDetail(BaseModel):
    """Detailed recommendation for a single bank."""

    bank_name: str
    slug: str
    website_url: Optional[str] = None
    description: Optional[str] = None

    remittance_score: float = Field(..., ge=0, le=100)
    digital_score: float = Field(..., ge=0, le=100)
    branch_network_score: float = Field(..., ge=0, le=100)
    
    total_score: float = Field(..., ge=0, le=100, description="Weighted composite score")
    top_reasons: list[str] = Field(default_factory=list, description="Top 3-5 reasons for recommendation")
    active_offers: list[ActiveBankOffer] = Field(default_factory=list, description="Currently active offers")

    class Config:
        from_attributes = True


class BankRecommendationResponse(BaseModel):
    """Response schema for bank recommendations."""

    monthly_salary: float
    remittance_need: str
    prefers_digital_banking: bool
    wants_credit_card_rewards: bool

    recommendations: list[BankRecommendationDetail] = Field(default_factory=list)
    total_matches: int = Field(default=0, ge=0, description="Number of eligible banks")
    explanation: str = Field(..., description="Human-readable explanation of recommendations")

    class Config:
        json_schema_extra = {
            "example": {
                "monthly_salary": 15000.0,
                "remittance_need": "high",
                "prefers_digital_banking": True,
                "wants_credit_card_rewards": True,
                "recommendations": [
                    {
                        "bank_name": "Emirates NBD",
                        "slug": "emirates-nbd",
                        "website_url": "https://www.emiratesnbd.com",
                        "description": "UAE's leading bank",
                        "remittance_score": 95.0,
                        "digital_score": 92.0,
                        "branch_network_score": 98.0,
                        "total_score": 94.2,
                        "top_reasons": [
                            "Excellent remittance services",
                            "Outstanding digital banking platform",
                            "Extensive branch network",
                            "Premium credit card rewards"
                        ],
                        "active_offers": [
                            {
                                "title": "Welcome Bonus",
                                "description": "Cashback on credit card spend",
                                "source_url": "https://example.com/offer"
                            }
                        ]
                    }
                ],
                "total_matches": 4,
                "explanation": "Based on your high remittance needs and preference for digital banking, we recommend Emirates NBD. They offer excellent remittance services with a world-class app and extensive branch network."
            }
        }
