"""
Application configuration using Pydantic Settings.
"""

from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    # Application
    APP_NAME: str = "FirstDay UAE API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/firstday_uae"
    
    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]
    
    # API
    API_V1_STR: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
