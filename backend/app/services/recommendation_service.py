"""
Neighborhood recommendation engine service.

Scores neighborhoods based on affordability, commute, lifestyle, and walkability.
"""

from typing import Optional
from dataclasses import dataclass
from math import sqrt
from sqlalchemy.orm import Session

from app.models import City, Neighborhood
from app.schemas.recommendation import (
    ScoreBreakdown,
    NeighborhoodRecommendation,
    RecommendationResponse,
)


# Work location coordinates (latitude, longitude) - sample UAE locations
WORK_LOCATIONS = {
    "najda street": (24.4524, 54.3759),
    "hamdan street": (24.4632, 54.3667),
    "al maryah island": (24.4956, 54.3939),
    "khalifa street": (24.4538, 54.3636),
    "corniche": (24.4800, 54.3567),
    "mussafah": (24.3667, 54.5667),
}


@dataclass
class LocationScore:
    """Score breakdown for a single neighborhood."""
    
    neighborhood: Neighborhood
    affordability_score: float
    commute_score: float
    lifestyle_score: float
    walkability_score: float
    total_score: float


def _find_work_location_coords(location_text: str) -> Optional[tuple[float, float]]:
    """Find work location coordinates (simplified matching)."""
    location_lower = location_text.lower()
    
    # Exact match
    if location_lower in WORK_LOCATIONS:
        return WORK_LOCATIONS[location_lower]
    
    # Partial match
    for work_loc, coords in WORK_LOCATIONS.items():
        if work_loc in location_lower or location_lower in work_loc:
            return coords
    
    # Default to central Abu Dhabi if not found
    return (24.4539, 54.3773)


def _calculate_distance(
    coord1: tuple[float, float],
    coord2: tuple[float, float],
) -> float:
    """Calculate simple distance between two coordinates (Euclidean approximation)."""
    lat_diff = (coord2[0] - coord1[0]) * 111  # km per degree latitude
    lon_diff = (coord2[1] - coord1[1]) * 111 * 0.8  # km per degree longitude at equator
    return sqrt(lat_diff**2 + lon_diff**2)


def _calculate_affordability_score(
    rent_range: tuple[float, float],
    monthly_budget: float,
    monthly_salary: float,
) -> float:
    """Calculate affordability score (0-100)."""
    annual_salary = monthly_salary * 12
    rent_avg = (rent_range[0] + rent_range[1]) / 2
    
    # If no budget specified, use 30% of salary as guideline
    if not monthly_budget:
        monthly_budget = monthly_salary * 0.30
    
    # Check if affordable
    if rent_avg > monthly_budget:
        affordability = max(0, 100 - ((rent_avg - monthly_budget) / monthly_budget * 50))
    else:
        # Extra points for saving money
        savings = (monthly_budget - rent_avg) / monthly_budget
        affordability = min(100, 80 + (savings * 20))
    
    return affordability


def _calculate_commute_score(
    distance_km: float,
    preferred_minutes: int,
) -> float:
    """Calculate commute score based on distance (0-100)."""
    # Estimate ~2 km per minute in urban area
    estimated_minutes = distance_km / 2
    
    if estimated_minutes <= preferred_minutes:
        # Full points if within preference
        return 100 - (estimated_minutes / preferred_minutes * 20)
    else:
        # Deduct points for exceeding preference
        excess = estimated_minutes - preferred_minutes
        return max(25, 60 - (excess * 2))


def _calculate_lifestyle_score(
    lifestyle: str,
    neighborhood: Neighborhood,
) -> float:
    """Calculate lifestyle compatibility score (0-100)."""
    scores = []
    
    # Base on existing scores in neighborhood
    if neighborhood.family_score and lifestyle == "budget":
        scores.append(neighborhood.family_score * 0.7)  # Families want affordable areas
    elif neighborhood.nightlife_score and lifestyle == "premium":
        scores.append(neighborhood.nightlife_score)  # Premium likes nightlife
    elif neighborhood.walkability_score:
        scores.append(neighborhood.walkability_score * 0.8)  # All lifestyles like walkability
    
    if scores:
        return sum(scores) / len(scores)
    
    # Default score
    return 75.0


def _calculate_walkability_score(neighborhood: Neighborhood) -> float:
    """Get walkability score from neighborhood."""
    return neighborhood.walkability_score or 70.0


def score_neighborhoods(
    neighborhoods: list[Neighborhood],
    work_location_text: str,
    monthly_salary: float,
    monthly_budget: Optional[float],
    lifestyle: str,
    transport_preference: str,
    preferred_commute_minutes: int,
) -> list[LocationScore]:
    """Score and rank neighborhoods based on recommendation criteria."""
    
    # Get work location coordinates
    work_coords = _find_work_location_coords(work_location_text)
    
    scored_neighborhoods = []
    
    for neighborhood in neighborhoods:
        # Skip if no rent data
        if not neighborhood.avg_rent_min or not neighborhood.avg_rent_max:
            continue
        
        # Calculate individual scores
        affordability = _calculate_affordability_score(
            (neighborhood.avg_rent_min, neighborhood.avg_rent_max),
            monthly_budget or monthly_salary * 0.30,
            monthly_salary,
        )
        
        # Calculate commute score
        if neighborhood.latitude and neighborhood.longitude:
            distance = _calculate_distance(
                work_coords,
                (neighborhood.latitude, neighborhood.longitude),
            )
        else:
            distance = 5.0  # Default distance if no coords
        
        commute = _calculate_commute_score(distance, preferred_commute_minutes)
        
        lifestyle_fit = _calculate_lifestyle_score(lifestyle, neighborhood)
        walkability = _calculate_walkability_score(neighborhood)
        
        # Calculate total score (weighted average)
        weights = {
            "affordability": 0.35,
            "commute": 0.30,
            "lifestyle": 0.20,
            "walkability": 0.15,
        }
        
        total_score = (
            affordability * weights["affordability"]
            + commute * weights["commute"]
            + lifestyle_fit * weights["lifestyle"]
            + walkability * weights["walkability"]
        )
        
        scored_neighborhoods.append(
            LocationScore(
                neighborhood=neighborhood,
                affordability_score=affordability,
                commute_score=commute,
                lifestyle_score=lifestyle_fit,
                walkability_score=walkability,
                total_score=total_score,
            )
        )
    
    # Sort by score descending
    return sorted(scored_neighborhoods, key=lambda x: x.total_score, reverse=True)


def build_recommendation_response(
    city: City,
    work_location_text: str,
    monthly_salary: float,
    monthly_budget: Optional[float],
    lifestyle: str,
    transport_preference: str,
    preferred_commute_minutes: int,
    scored_neighborhoods: list[LocationScore],
) -> RecommendationResponse:
    """Build recommendation response from scored neighborhoods."""
    
    recommendations = []
    
    for location_score in scored_neighborhoods[:10]:  # Top 10
        neighborhood = location_score.neighborhood
        
        # Build reasons
        reasons = []
        if location_score.affordability_score > 80:
            reasons.append("Great affordability")
        if location_score.commute_score > 80:
            reasons.append("Close to work")
        if location_score.lifestyle_score > 80:
            reasons.append("Matches your lifestyle")
        if location_score.walkability_score > 80:
            reasons.append("Very walkable")
        
        # Build summary
        if not reasons:
            reasons.append("Good overall fit")
        
        summary = f"{neighborhood.name} offers {reasons[0].lower()} "
        summary += f"with average rent AED {int((neighborhood.avg_rent_min or 0 + neighborhood.avg_rent_max or 0) / 2)}/month."
        
        recommendations.append(
            NeighborhoodRecommendation(
                id=neighborhood.id,
                name=neighborhood.name,
                slug=neighborhood.slug,
                avg_rent_min=neighborhood.avg_rent_min,
                avg_rent_max=neighborhood.avg_rent_max,
                walkability_score=neighborhood.walkability_score,
                family_score=neighborhood.family_score,
                nightlife_score=neighborhood.nightlife_score,
                latitude=neighborhood.latitude,
                longitude=neighborhood.longitude,
                description=neighborhood.description,
                total_score=round(location_score.total_score, 1),
                score_breakdown=ScoreBreakdown(
                    affordability_score=round(location_score.affordability_score, 1),
                    commute_score=round(location_score.commute_score, 1),
                    lifestyle_score=round(location_score.lifestyle_score, 1),
                    walkability_score=round(location_score.walkability_score, 1),
                ),
                top_reasons=reasons,
                summary=summary,
            )
        )
    
    # Overall summary
    if recommendations:
        top_neighborhood = recommendations[0]
        overall_summary = f"Top recommendation: {top_neighborhood.name} (Score: {top_neighborhood.total_score}/100). "
        overall_summary += f"Found {len(recommendations)} neighborhoods matching your criteria."
    else:
        overall_summary = "No neighborhoods found matching your criteria."
    
    return RecommendationResponse(
        city_slug=city.slug,
        work_location=work_location_text,
        work_location_found=work_location_text.lower() in [k.lower() for k in WORK_LOCATIONS.keys()],
        salary_input=monthly_salary,
        budget_input=monthly_budget,
        lifestyle_input=lifestyle,
        transport_input=transport_preference,
        recommendations=recommendations,
        total_matches=len(recommendations),
        summary=overall_summary,
    )
