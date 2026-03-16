"""
Main API v1 router.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import health, cities, recommendations, cost_estimator, bank_recommendations

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, prefix="/health")
api_router.include_router(cities.router, prefix="/cities")
api_router.include_router(recommendations.router, prefix="/recommendations")
api_router.include_router(cost_estimator.router, prefix="/cost-estimate")
api_router.include_router(bank_recommendations.router, prefix="/bank-advisor")
