"""
API integration tests.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    return TestClient(app)


class TestAPIIntegration:
    """API integration tests."""
    
    def test_api_documentation_available(self, client: TestClient) -> None:
        """Test that API documentation is available."""
        response = client.get("/docs")
        assert response.status_code == 200
    
    def test_openapi_schema_available(self, client: TestClient) -> None:
        """Test that OpenAPI schema is available."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "info" in data
    
    def test_all_v1_routes_documented(self, client: TestClient) -> None:
        """Test that all v1 routes are in OpenAPI schema."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        paths = data.get("paths", {})
        
        # Check health endpoints are documented
        assert "/api/v1/health" in paths
        assert "/api/v1/health/ready" in paths
