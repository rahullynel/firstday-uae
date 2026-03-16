"""
City model - represents cities in the platform.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.models.base import Base


class City(Base):
    """City model representing a city in the UAE."""

    __tablename__ = "cities"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), unique=True, nullable=False, index=True)
    slug: str = Column(String(100), unique=True, nullable=False, index=True)
    country: str = Column(String(100), nullable=False, default="UAE")
    currency: str = Column(String(10), nullable=False, default="AED")
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    neighborhoods = relationship("Neighborhood", back_populates="city", cascade="all, delete-orphan")
    checklists = relationship("RelocationChecklistItem", back_populates="city", cascade="all, delete-orphan")
    cost_indices = relationship("CostIndex", back_populates="city", cascade="all, delete-orphan")
    user_searches = relationship("UserSearchQuery", back_populates="city", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<City {self.name}>"
