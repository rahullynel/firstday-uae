"""
Cost-of-living estimate API endpoint.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import City, Neighborhood
from app.schemas.cost_estimate import CostEstimateRequest, CostEstimateResponse
from app.services.cost_calculator_service import calculate_cost_estimate

router = APIRouter()


@router.post("", response_model=CostEstimateResponse)
async def get_cost_estimate(
    request: CostEstimateRequest,
    db: Session = Depends(get_db),
) -> CostEstimateResponse:
    """
    Get cost-of-living estimate for a city and lifestyle.
    
    Provides detailed breakdown of monthly expenses including rent, groceries,
    transport, utilities, dining, and miscellaneous costs. Calculates savings
    and comfort score based on provided salary.
    
    Args:
        request: Cost estimate request with city, salary, lifestyle preferences
        db: Database session
    
    Returns:
        Comprehensive cost estimate with breakdown and savings analysis
    """
    # Find city by slug
    city = db.query(City).filter_by(slug=request.city_slug).first()
    if not city:
        raise HTTPException(status_code=404, detail=f"City '{request.city_slug}' not found")
    
    # Find neighborhood if specified
    neighborhood = None
    if request.neighborhood_slug:
        neighborhood = db.query(Neighborhood).filter_by(
            city_id=city.id,
            slug=request.neighborhood_slug
        ).first()
        if not neighborhood:
            raise HTTPException(
                status_code=404,
                detail=f"Neighborhood '{request.neighborhood_slug}' not found in {city.name}"
            )
    
    # Calculate cost estimate
    try:
        estimate = calculate_cost_estimate(
            db=db,
            city=city,
            neighborhood=neighborhood,
            monthly_salary=request.monthly_salary,
            lifestyle=request.lifestyle,
            transport_preference=request.transport_preference,
        )
        return estimate
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
