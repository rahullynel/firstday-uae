"""
Relocation checklist service.

Fetches and groups checklist items for newcomers moving to Abu Dhabi.
"""

from typing import Optional
from sqlalchemy.orm import Session

from app.models import City, RelocationChecklistItem
from app.schemas.checklist import ChecklistItem, ChecklistGroup, ChecklistResponse


def _categorize_period(day_order: int) -> str:
    """Categorize day_order into practical time periods."""
    if day_order <= 3:
        return "Day 1-3"
    elif day_order <= 7:
        return "Week 1"
    else:
        return "After settling in"


def get_checklist(
    db: Session,
    city_slug: Optional[str] = None,
) -> ChecklistResponse:
    """
    Get relocation checklist items, grouped by practical time periods.
    
    Args:
        db: Database session
        city_slug: Optional city slug to filter by (e.g., "abu-dhabi")
    
    Returns:
        ChecklistResponse with items grouped into Day 1-3, Week 1, After settling in
    """
    # Determine city filter
    city = None
    city_name = None
    
    if city_slug:
        city = db.query(City).filter_by(slug=city_slug).first()
        if not city:
            # City not found - return empty response
            return ChecklistResponse(
                city_name=None,
                city_slug=city_slug,
                total_items=0,
                groups=[],
            )
        city_name = city.name
        query = db.query(RelocationChecklistItem).filter_by(city_id=city.id)
    else:
        # Fetch all checklist items (no city filter)
        query = db.query(RelocationChecklistItem)
    
    # Order by day_order for predictable grouping
    items = query.order_by(RelocationChecklistItem.day_order).all()
    
    if not items:
        return ChecklistResponse(
            city_name=city_name,
            city_slug=city_slug,
            total_items=0,
            groups=[],
        )
    
    # Group items by time period
    groups_dict = {}
    periods_order = ["Day 1-3", "Week 1", "After settling in"]
    
    for item in items:
        period = _categorize_period(item.day_order)
        if period not in groups_dict:
            groups_dict[period] = []
        
        # Convert model to schema
        checklist_item = ChecklistItem(
            id=item.id,
            title=item.title,
            description=item.description,
            category=item.category,
            day_order=item.day_order,
            official_link=item.official_link,
        )
        groups_dict[period].append(checklist_item)
    
    # Build groups in the correct order
    groups = [
        ChecklistGroup(period=period, items=groups_dict[period])
        for period in periods_order
        if period in groups_dict
    ]
    
    return ChecklistResponse(
        city_name=city_name,
        city_slug=city_slug,
        total_items=len(items),
        groups=groups,
    )
