"""
Tests for health check endpoints.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    return TestClient(app)


class TestHealthEndpoints:
    """Health check endpoint tests."""
    
    def test_health_status(self, client: TestClient) -> None:
        """Test health status endpoint."""
        response = client.get("/api/v1/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
    
    def test_readiness_status(self, client: TestClient) -> None:
        """Test readiness status endpoint."""
        response = client.get("/api/v1/health/ready")
        assert response.status_code == 200
        assert response.json()["status"] == "ready"
    
    def test_health_response_type(self, client: TestClient) -> None:
        """Test health response is JSON dict."""
        response = client.get("/api/v1/health")
        assert isinstance(response.json(), dict)
        assert "status" in response.json()
