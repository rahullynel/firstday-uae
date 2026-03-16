"""
Health check endpoints.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("", tags=["health"])
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.
    
    Returns:
        dict: Status indicator
    """
    return {"status": "healthy"}


@router.get("/ready", tags=["health"])
async def readiness_check() -> dict[str, str]:
    """
    Readiness check endpoint for deployment.
    
    Returns:
        dict: Readiness status
    """
    return {"status": "ready"}
