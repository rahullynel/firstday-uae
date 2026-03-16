"""
Amenity model - represents amenities in neighborhoods.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Amenity(Base):
    """Amenity model representing a point of interest in a neighborhood."""

    __tablename__ = "amenities"

    id: int = Column(Integer, primary_key=True, index=True)
    neighborhood_id: int = Column(Integer, ForeignKey("neighborhoods.id"), nullable=False, index=True)
    name: str = Column(String(100), nullable=False, index=True)
    category: str = Column(String(50), nullable=False, index=True)
    address: str = Column(String(255), nullable=True)
    latitude: float = Column(Float, nullable=True)
    longitude: float = Column(Float, nullable=True)
    rating: float = Column(Float, nullable=True)
    source_url: str = Column(String(500), nullable=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    neighborhood = relationship("Neighborhood", back_populates="amenities")

    def __repr__(self) -> str:
        return f"<Amenity {self.name} ({self.category})>"
