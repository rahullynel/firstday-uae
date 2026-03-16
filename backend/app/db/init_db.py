"""Database initialization for FirstDay UAE application."""

from sqlalchemy.orm import Session
from app.models.base import Base
from app.db.session import engine
from app.models import (
    City,
    Neighborhood,
    Amenity,
    Bank,
    BankOffer,
    RelocationChecklistItem,
    CostIndex,
)
from .seed_data import seed_database


def init_db() -> None:
    """
    Initialize the database by creating all tables and seeding with sample data.
    
    This function:
    1. Creates all tables defined in the models
    2. Seeds the database with MVP sample data (idempotent)
    
    Call this during application startup or as part of a setup command.
    """
    print("Initializing database...")
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("✓ Database tables created")
    
    # Seed with sample data
    from app.db.session import get_db
    db = next(get_db())
    
    try:
        seed_database(db)
    finally:
        db.close()
    
    print("✓ Database initialization complete")


def reset_db() -> None:
    """
    Drop all tables and recreate them.
    
    WARNING: This will delete all data in the database.
    Use with caution in development only.
    """
    print("⚠️  Resetting database (deleting all tables)...")
    Base.metadata.drop_all(bind=engine)
    print("✓ All tables dropped")
    
    # Recreate and seed
    init_db()
