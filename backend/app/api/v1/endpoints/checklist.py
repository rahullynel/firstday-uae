"""
Relocation checklist API endpoint.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.checklist import ChecklistRequest, ChecklistResponse
from app.services.checklist_service import get_checklist

router = APIRouter()


@router.post("", response_model=ChecklistResponse)
async def get_relocation_checklist(
    request: ChecklistRequest,
    db: Session = Depends(get_db),
) -> ChecklistResponse:
    """
    Get relocation checklist for newcomers moving to Abu Dhabi.
    
    Items are grouped into practical time periods:
    - Day 1-3: Essential first steps
    - Week 1: Complete during the first week
    - After settling in: Additional setup tasks
    
    Optionally filter by city_slug (e.g., "abu-dhabi").
    """
    return get_checklist(db, city_slug=request.city_slug)
