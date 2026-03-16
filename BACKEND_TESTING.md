# FirstDay UAE Backend - Local Testing Guide

## Prerequisites

### Option 1: Native Development (Linux/Mac)

```bash
# Ubuntu/Debian - Install Python development tools
sudo apt install python3.12-venv python3-pip python3-dev

# macOS 
brew install python@3.12
```

### Option 2: Docker (Recommended)

Ensure Docker and Docker Compose are installed:
```bash
docker --version
docker-compose --version
```

## Testing with Docker Compose (Recommended)

### Start All Services

```bash
# From project root
docker-compose up --build
```

This will start:
- **PostgreSQL** on `localhost:5432`
- **Backend API** on `localhost:8000`
- **Frontend** on `localhost:3000`

### Test Backend API

Once running, test the endpoints:

```bash
# Health check
curl http://localhost:8000/api/v1/health

# Readiness check
curl http://localhost:8000/api/v1/health/ready

# Root endpoint
curl http://localhost:8000/

# API Documentation (browser)
open http://localhost:8000/docs
```

## Testing Locally (Without Docker)

### 1. Install Dependencies

```bash
cd backend

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy example env file
cp .env.example .env
```

Edit `.env` if needed (defaults should work for local postgres on localhost).

### 3. Start Backend

```bash
# From backend directory with .venv activated
uvicorn app.main:app --reload

# Or run directly
python3 app/main.py
```

Backend will start on `http://localhost:8000`

### 4. Test Endpoints

In a new terminal:

```bash
# Health check
curl http://localhost:8000/api/v1/health

# Readiness probe
curl http://localhost:8000/api/v1/health/ready

# API root
curl http://localhost:8000/

# Interactive docs
open http://localhost:8000/docs
```

## Running Tests

### With Dependencies Installed

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_health.py -v

# Run and watch
pip install pytest-watch
ptw
```

### Test Results Should Show

```
tests/test_main.py::test_root_endpoint PASSED
tests/test_main.py::test_health_check PASSED
tests/test_main.py::test_readiness_check PASSED
tests/test_config.py::test_settings_loaded PASSED
tests/test_health.py::TestHealthEndpoints::test_health_status PASSED
tests/test_api_integration.py::TestAPIIntegration::test_openapi_schema_available PASSED
```

## Troubleshooting

### Port Already in Use

If port 8000 is already in use:
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or use different port
uvicorn app.main:app --port 8001 --reload
```

### Database Connection Errors

Ensure PostgreSQL is running:
```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# Or start with Docker Compose database only
docker-compose up db
```

### Module Import Errors

Ensure virtual environment is activated:
```bash
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate      # Windows

# Verify
which python  # Should show path in .venv
```

## API Endpoints Available

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Root endpoint with app info |
| GET | `/health` | Basic health check |
| GET | `/docs` | Swagger UI documentation |
| GET | `/openapi.json` | OpenAPI schema |
| GET | `/api/v1/health` | API health status |
| GET | `/api/v1/health/ready` | Readiness probe |

## Next Steps

After confirming the backend is running:

1. **Add Features**: Create new endpoint routers in `app/api/v1/endpoints/`
2. **Add Models**: Create SQLAlchemy models in `app/models/`
3. **Add Schemas**: Create Pydantic schemas in `app/schemas/`
4. **Add Services**: Implement business logic in `app/services/`
5. **Expand Tests**: Add more tests as features are added

## Documentation Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
