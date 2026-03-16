"""
Schemas package - Pydantic models for validation and serialization.

Exports all schemas for easy importing.
"""

# Base schemas
from app.schemas.city import CityBase, CityCreate, CityRead
from app.schemas.neighborhood import (
    AmenityBase,
    AmenityRead,
    NeighborhoodBase,
    NeighborhoodCreate,
    NeighborhoodRead,
    NeighborhoodWithAmenities,
)
from app.schemas.bank import (
    BankBase,
    BankCreate,
    BankRead,
    BankWithOffers,
    BankOfferBase,
    BankOfferCreate,
    BankOfferRead,
)
from app.schemas.checklist import (
    RelocationChecklistItemBase,
    RelocationChecklistItemCreate,
    RelocationChecklistItemRead,
)
from app.schemas.cost_index import CostIndexBase, CostIndexCreate, CostIndexRead, CostIndexSummary

# Request/Response schemas
from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendedNeighborhood,
    RecommendationResponse,
)
from app.schemas.cost_estimate import (
    CostEstimateRequest,
    CostBreakdown,
    LocationCostEstimate,
    CostEstimateResponse,
)
from app.schemas.bank_recommendation import (
    BankRecommendationRequest,
    BankWithRecommendationScore,
    BankRecommendationResponse,
)

__all__ = [
    # City
    "CityBase",
    "CityCreate",
    "CityRead",
    # Neighborhood & Amenity
    "AmenityBase",
    "AmenityRead",
    "NeighborhoodBase",
    "NeighborhoodCreate",
    "NeighborhoodRead",
    "NeighborhoodWithAmenities",
    # Bank & BankOffer
    "BankBase",
    "BankCreate",
    "BankRead",
    "BankWithOffers",
    "BankOfferBase",
    "BankOfferCreate",
    "BankOfferRead",
    # Checklist
    "RelocationChecklistItemBase",
    "RelocationChecklistItemCreate",
    "RelocationChecklistItemRead",
    # Cost Index
    "CostIndexBase",
    "CostIndexCreate",
    "CostIndexRead",
    "CostIndexSummary",
    # Recommendation
    "RecommendationRequest",
    "RecommendedNeighborhood",
    "RecommendationResponse",
    # Cost Estimate
    "CostEstimateRequest",
    "CostBreakdown",
    "LocationCostEstimate",
    "CostEstimateResponse",
    # Bank Recommendation
    "BankRecommendationRequest",
    "BankWithRecommendationScore",
    "BankRecommendationResponse",
]
