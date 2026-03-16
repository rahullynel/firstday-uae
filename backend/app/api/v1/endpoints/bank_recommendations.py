"""
Bank recommendation API endpoint.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.bank_recommendation import (
    BankRecommendationRequest,
    BankRecommendationResponse,
)
from app.services.bank_advisor_service import get_bank_recommendations

router = APIRouter()


@router.post("", response_model=BankRecommendationResponse)
async def recommend_banks(
    request: BankRecommendationRequest,
    db: Session = Depends(get_db),
) -> BankRecommendationResponse:
    """
    Get personalized bank recommendations.
    
    Recommends banks based on salary, remittance needs, digital banking
    preference, and credit card rewards interest.
    
    Args:
        request: Bank recommendation request with user preferences
        db: Database session
    
    Returns:
        Ranked list of banks with detailed scores and active offers
    """
    try:
        recommendations = get_bank_recommendations(
            db=db,
            monthly_salary=request.monthly_salary,
            remittance_need=request.remittance_need,
            prefers_digital_banking=request.prefers_digital_banking,
            wants_credit_card_rewards=request.wants_credit_card_rewards,
        )
        return recommendations
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
