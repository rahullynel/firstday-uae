"""
UserSearchQuery model - represents user search and preference data.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class UserSearchQuery(Base):
    """UserSearchQuery model for tracking user location preferences."""

    __tablename__ = "user_search_queries"

    id: int = Column(Integer, primary_key=True, index=True)
    work_location_text: str = Column(String(200), nullable=False)
    city_id: int = Column(Integer, ForeignKey("cities.id"), nullable=True, index=True)
    monthly_salary: float = Column(Float, nullable=True)
    monthly_budget: float = Column(Float, nullable=True)
    lifestyle: str = Column(String(50), nullable=True)
    transport_preference: str = Column(String(50), nullable=True)
    preferred_commute_minutes: int = Column(Integer, nullable=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    city = relationship("City", back_populates="user_searches")

    def __repr__(self) -> str:
        return f"<UserSearchQuery user_id={self.id}>"
