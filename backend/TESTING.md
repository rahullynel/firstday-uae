# Test Commands

## Running Tests Locally

Before running tests, install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest
```

### Run With Coverage
```bash
pytest --cov=app --cov-report=html
```

### Run Specific Test File
```bash
pytest tests/test_main.py
```

### Run Specific Test
```bash
pytest tests/test_main.py::test_root_endpoint
```

### Run Tests by Marker
```bash
pytest -m unit
pytest -m integration
```

### Watch Mode (with pytest-watch)
```bash
pip install pytest-watch
ptw
```

## Test Structure

- `tests/test_main.py` - Main app initialization and routing
- `tests/test_config.py` - Configuration and settings
- `tests/test_health.py` - Health check endpoints
- `tests/test_api_integration.py` - API integration tests

## Test Coverage Goals

- **Unit Tests**: Core functionality (settings, config)
- **Integration Tests**: API endpoints, CORS, documentation
- **Coverage Target**: 80%+ of critical paths

## CI/CD Integration

Tests will run automatically on:
- Pull requests
- Commits to main branch
- Before Docker image builds
