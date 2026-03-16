"""
FirstDay UAE Backend - Main Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Placeholder for routes
# from app.api import health, neighborhoods, locations, banks, amenities, commute, checklist

app_instance: FastAPI | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager"""
    # Startup logic
    print("🚀 FirstDay UAE Backend Starting...")
    yield
    # Shutdown logic
    print("🛑 FirstDay UAE Backend Shutting Down...")


def create_app() -> FastAPI:
    """
    Create and configure FastAPI application instance.
    
    Returns:
        FastAPI: Configured application instance
    """
    app = FastAPI(
        title="FirstDay UAE API",
        description="Relocation intelligence platform for UAE newcomers",
        version="0.1.0",
        lifespan=lifespan,
    )
    
    # CORS Configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",  # Local development
            "http://127.0.0.1:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    # app.include_router(health.router, prefix="/api/health", tags=["health"])
    # app.include_router(neighborhoods.router, prefix="/api/neighborhoods", tags=["neighborhoods"])
    # app.include_router(locations.router, prefix="/api/locations", tags=["locations"])
    # app.include_router(banks.router, prefix="/api/banks", tags=["banks"])
    # app.include_router(amenities.router, prefix="/api/amenities", tags=["amenities"])
    # app.include_router(commute.router, prefix="/api/commute", tags=["commute"])
    # app.include_router(checklist.router, prefix="/api/checklist", tags=["checklist"])
    
    @app.get("/")
    async def root() -> dict[str, str]:
        """Root endpoint"""
        return {"message": "FirstDay UAE API is running"}
    
    @app.get("/health")
    async def health_check() -> dict[str, str]:
        """Health check endpoint"""
        return {"status": "healthy"}
    
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
