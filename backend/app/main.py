"""
FirstDay UAE Backend - Main Application Entry Point
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    # Startup
    print("🚀 FirstDay UAE Backend Starting...")
    yield
    # Shutdown
    print("🛑 FirstDay UAE Backend Shutting Down...")


def create_app() -> FastAPI:
    """
    Create and configure FastAPI application instance.
    
    Returns:
        FastAPI: Configured application instance
    """
    app = FastAPI(
        title=settings.APP_NAME,
        description="Relocation intelligence platform for UAE newcomers",
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )
    
    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_CREDENTIALS,
        allow_methods=settings.CORS_METHODS,
        allow_headers=settings.CORS_HEADERS,
    )
    
    # Include API routers
    app.include_router(api_router, prefix=settings.API_V1_STR)
    
    # Root endpoint
    @app.get("/")
    async def root() -> dict[str, str]:
        """Root endpoint."""
        return {
            "message": "FirstDay UAE API",
            "version": settings.APP_VERSION,
            "docs": "/docs",
        }
    
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
