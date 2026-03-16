"""
Tests for application configuration.
"""

import pytest
from app.core.config import settings


def test_settings_loaded() -> None:
    """Test that settings are loaded correctly."""
    assert settings.APP_NAME == "FirstDay UAE API"
    assert settings.APP_VERSION == "0.1.0"
    assert settings.API_V1_STR == "/api/v1"


def test_database_url_configured() -> None:
    """Test that database URL is configured."""
    assert settings.DATABASE_URL
    assert "postgresql" in settings.DATABASE_URL


def test_cors_origins_configured() -> None:
    """Test that CORS origins are configured."""
    assert len(settings.CORS_ORIGINS) > 0
    assert "http://localhost:3000" in settings.CORS_ORIGINS


def test_cors_credentials_enabled() -> None:
    """Test that CORS credentials are enabled."""
    assert settings.CORS_CREDENTIALS is True
