"""
Pytest configuration and shared fixtures.
"""

import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


@pytest.fixture(scope="session")
def test_db_url() -> str:
    """Get test database URL."""
    return os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")


@pytest.fixture(scope="session")
def engine(test_db_url: str):
    """Create test database engine."""
    return create_engine(test_db_url)


@pytest.fixture
def session(engine) -> Session:
    """Create test database session."""
    connection = engine.connect()
    transaction = connection.begin()
    SessionLocal = sessionmaker(bind=connection)
    session = SessionLocal()
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()
