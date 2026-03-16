"""
Main API v1 router.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import health, cities

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, prefix="/health")
api_router.include_router(cities.router, prefix="/cities")
