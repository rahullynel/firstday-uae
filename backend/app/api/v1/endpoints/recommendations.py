"""
Neighborhood recommendations API endpoint.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import City, Neighborhood
from app.schemas.recommendation import RecommendationRequest, RecommendationResponse
from app.services.recommendation_service import (
    score_neighborhoods,
    build_recommendation_response,
)

router = APIRouter()


@router.post("", response_model=RecommendationResponse)
async def get_recommendations(
    request: RecommendationRequest,
    db: Session = Depends(get_db),
) -> RecommendationResponse:
    """
    Get neighborhood recommendations based on user preferences.
    
    Returns ranked neighborhoods with detailed scoring and reasoning.
    """
    # Find city by slug
    city = db.query(City).filter_by(slug=request.city_slug).first()
    if not city:
        raise HTTPException(status_code=404, detail=f"City '{request.city_slug}' not found")
    
    # Get neighborhoods for the city
    neighborhoods = db.query(Neighborhood).filter_by(city_id=city.id).all()
    if not neighborhoods:
        raise HTTPException(status_code=404, detail=f"No neighborhoods found for {city.name}")
    
    # Score neighborhoods
    scored = score_neighborhoods(
        neighborhoods=neighborhoods,
        work_location_text=request.work_location_text,
        monthly_salary=request.monthly_salary,
        monthly_budget=request.monthly_budget,
        lifestyle=request.lifestyle,
        transport_preference=request.transport_preference,
        preferred_commute_minutes=request.preferred_commute_minutes,
    )
    
    # Build response
    response = build_recommendation_response(
        city=city,
        work_location_text=request.work_location_text,
        monthly_salary=request.monthly_salary,
        monthly_budget=request.monthly_budget,
        lifestyle=request.lifestyle,
        transport_preference=request.transport_preference,
        preferred_commute_minutes=request.preferred_commute_minutes,
        scored_neighborhoods=scored,
    )
    
    return response
