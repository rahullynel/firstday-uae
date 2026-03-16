"""
CostIndex model - represents cost of living indices for cities.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey

from app.models.base import Base
from sqlalchemy.orm import relationship


class CostIndex(Base):
    """CostIndex model representing cost of living metrics for a city."""

    __tablename__ = "cost_indices"

    id: int = Column(Integer, primary_key=True, index=True)
    city_id: int = Column(Integer, ForeignKey("cities.id"), nullable=False, unique=True, index=True)
    rent_index: float = Column(Float, nullable=True)
    grocery_index: float = Column(Float, nullable=True)
    transport_index: float = Column(Float, nullable=True)
    utility_index: float = Column(Float, nullable=True)
    dining_index: float = Column(Float, nullable=True)
    misc_index: float = Column(Float, nullable=True)
    last_updated: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    city = relationship("City", back_populates="cost_indices")

    def __repr__(self) -> str:
        return f"<CostIndex city_id={self.city_id}>"
