"""
Cities API endpoints.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import City
from app.schemas.city import CityRead

router = APIRouter()


@router.get("", response_model=list[CityRead])
async def list_cities(db: Session = Depends(get_db)) -> list[CityRead]:
    """
    Get all cities.
    
    Returns:
        list[CityRead]: List of all cities
    """
    cities = db.query(City).all()
    return cities
