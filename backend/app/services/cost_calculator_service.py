"""
Cost-of-living calculator service.

Calculates monthly and annual cost estimates based on salary, lifestyle,
transport preference, and optional neighborhood selection.
"""

from typing import Optional
from sqlalchemy.orm import Session

from app.models import City, Neighborhood, CostIndex
from app.schemas.cost_estimate import CostBreakdown, CostEstimateResponse


# Base costs for different categories (in AED)
BASE_COSTS = {
    "groceries": 1000.0,
    "utilities": 500.0,
    "transport": 500.0,
    "dining": 800.0,
    "miscellaneous": 500.0,
}

# Default city rent when neighborhood not specified (AED/month)
DEFAULT_CITY_RENT = {
    "abu-dhabi": 4200.0,  # Based on neighborhood averages
}

# Lifestyle multipliers for dining and miscellaneous costs
LIFESTYLE_MULTIPLIERS = {
    "budget": 0.6,
    "balanced": 1.0,
    "premium": 1.4,
}

# Transport preference multipliers (applied to base transport cost)
TRANSPORT_MULTIPLIERS = {
    "walk": 0.2,
    "public": 0.6,
    "car": 1.0,
}


def calculate_cost_estimate(
    db: Session,
    city: City,
    neighborhood: Optional[Neighborhood],
    monthly_salary: float,
    lifestyle: str,
    transport_preference: str,
) -> CostEstimateResponse:
    """
    Calculate comprehensive cost-of-living estimate.
    
    Args:
        db: SQLAlchemy session
        city: City object
        neighborhood: Optional Neighborhood object for specific rent
        monthly_salary: Monthly salary in AED
        lifestyle: 'budget', 'balanced', or 'premium'
        transport_preference: 'walk', 'public', or 'car'
    
    Returns:
        CostEstimateResponse with complete cost breakdown
    """
    # Get cost index for the city
    cost_index = db.query(CostIndex).filter_by(city_id=city.id).first()
    if not cost_index:
        raise ValueError(f"No cost index found for {city.name}")
    
    # Validate inputs
    lifestyle = lifestyle.lower()
    transport_preference = transport_preference.lower()
    
    if lifestyle not in LIFESTYLE_MULTIPLIERS:
        raise ValueError(f"Invalid lifestyle: {lifestyle}")
    if transport_preference not in TRANSPORT_MULTIPLIERS:
        raise ValueError(f"Invalid transport preference: {transport_preference}")
    
    # Calculate rent
    if neighborhood:
        estimated_rent = (neighborhood.avg_rent_min + neighborhood.avg_rent_max) / 2
    else:
        estimated_rent = DEFAULT_CITY_RENT.get(city.slug, 4200.0)
    
    # Calculate groceries
    # Cost indices are 0-100, divide by 100 to get percentage multiplier
    estimated_groceries = BASE_COSTS["groceries"] * (cost_index.grocery_index / 100)
    
    # Calculate transport
    base_transport = BASE_COSTS["transport"]
    transport_mult = TRANSPORT_MULTIPLIERS[transport_preference]
    estimated_transport = base_transport * (cost_index.transport_index / 100) * transport_mult
    
    # Calculate utilities
    estimated_utilities = BASE_COSTS["utilities"] * (cost_index.utility_index / 100)
    
    # Calculate dining (lifestyle affects)
    lifestyle_mult = LIFESTYLE_MULTIPLIERS[lifestyle]
    estimated_dining = BASE_COSTS["dining"] * (cost_index.dining_index / 100) * lifestyle_mult
    
    # Calculate miscellaneous (lifestyle affects)
    estimated_miscellaneous = BASE_COSTS["miscellaneous"] * (cost_index.misc_index / 100) * lifestyle_mult
    
    # Calculate totals
    total_monthly_cost = (
        estimated_rent +
        estimated_groceries +
        estimated_transport +
        estimated_utilities +
        estimated_dining +
        estimated_miscellaneous
    )
    
    estimated_savings = monthly_salary - total_monthly_cost
    savings_percentage = (estimated_savings / monthly_salary) * 100 if monthly_salary > 0 else 0
    
    # Calculate comfort score (0-100 based on savings rate)
    if estimated_savings < 0:
        comfort_score = 0.0
    elif savings_percentage >= 50:
        comfort_score = 100.0
    else:
        # Linear scale: 0% savings = 0 score, 50% savings = 100 score
        comfort_score = (savings_percentage / 50) * 100
    
    # Build explanation
    explanation = _build_explanation(
        city_name=city.name,
        neighborhood_name=neighborhood.name if neighborhood else None,
        monthly_salary=monthly_salary,
        total_monthly_cost=total_monthly_cost,
        estimated_savings=estimated_savings,
        savings_percentage=savings_percentage,
        comfort_score=comfort_score,
        lifestyle=lifestyle,
        transport_preference=transport_preference,
    )
    
    cost_breakdown = CostBreakdown(
        estimated_rent=round(estimated_rent, 2),
        estimated_groceries=round(estimated_groceries, 2),
        estimated_transport=round(estimated_transport, 2),
        estimated_utilities=round(estimated_utilities, 2),
        estimated_dining=round(estimated_dining, 2),
        estimated_miscellaneous=round(estimated_miscellaneous, 2),
        estimated_total_monthly_cost=round(total_monthly_cost, 2),
    )
    
    return CostEstimateResponse(
        city_slug=city.slug,
        neighborhood_slug=neighborhood.slug if neighborhood else None,
        monthly_salary=monthly_salary,
        lifestyle=lifestyle,
        transport_preference=transport_preference,
        cost_breakdown=cost_breakdown,
        estimated_savings=round(estimated_savings, 2),
        savings_percentage=round(savings_percentage, 1),
        comfort_score=round(comfort_score, 1),
        explanation=explanation,
    )


def _build_explanation(
    city_name: str,
    neighborhood_name: Optional[str],
    monthly_salary: float,
    total_monthly_cost: float,
    estimated_savings: float,
    savings_percentage: float,
    comfort_score: float,
    lifestyle: str,
    transport_preference: str,
) -> str:
    """Generate a human-readable explanation of cost estimates."""
    
    location = neighborhood_name if neighborhood_name else city_name
    
    if estimated_savings < 0:
        return (
            f"With your current salary of ₱{monthly_salary:,.0f}, living in {location} with "
            f"a {lifestyle} lifestyle and using {transport_preference} transport would be "
            f"challenging. Estimated monthly deficit: ₱{abs(estimated_savings):,.0f}. "
            f"Consider a higher salary, budget lifestyle, or less expensive neighborhood."
        )
    elif savings_percentage < 20:
        return (
            f"Living in {location} is possible but leaves minimal room for savings or emergencies. "
            f"With {savings_percentage:.1f}% savings rate (₱{estimated_savings:,.0f}/month), "
            f"you'll have limited financial flexibility. Consider reducing transport or dining costs."
        )
    elif savings_percentage < 40:
        return (
            f"You can afford {location} with a {lifestyle} lifestyle and {transport_preference} transport. "
            f"Your {savings_percentage:.1f}% savings rate (₱{estimated_savings:,.0f}/month) provides "
            f"moderate financial security for emergencies and investments."
        )
    elif savings_percentage < 60:
        return (
            f"Great choice! {location} fits your budget comfortably. "
            f"With a {savings_percentage:.1f}% savings rate (₱{estimated_savings:,.0f}/month), "
            f"you'll have substantial funds for savings, travel, or lifestyle upgrades."
        )
    else:
        return (
            f"Excellent affordability in {location}! "
            f"Your {savings_percentage:.1f}% savings rate (₱{estimated_savings:,.0f}/month) "
            f"provides outstanding financial flexibility. You can comfortably save, invest, or upgrade lifestyle."
        )
