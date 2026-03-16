"""
Neighborhood model - represents neighborhoods within cities.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Neighborhood(Base):
    """Neighborhood model representing a neighborhood in a city."""

    __tablename__ = "neighborhoods"

    id: int = Column(Integer, primary_key=True, index=True)
    city_id: int = Column(Integer, ForeignKey("cities.id"), nullable=False, index=True)
    name: str = Column(String(100), nullable=False, index=True)
    slug: str = Column(String(100), nullable=False, index=True)
    avg_rent_min: float = Column(Float, nullable=True)
    avg_rent_max: float = Column(Float, nullable=True)
    walkability_score: float = Column(Float, nullable=True)
    noise_score: float = Column(Float, nullable=True)
    family_score: float = Column(Float, nullable=True)
    nightlife_score: float = Column(Float, nullable=True)
    latitude: float = Column(Float, nullable=True)
    longitude: float = Column(Float, nullable=True)
    description: str = Column(String(500), nullable=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    city = relationship("City", back_populates="neighborhoods")
    amenities = relationship("Amenity", back_populates="neighborhood", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Neighborhood {self.name}>"
