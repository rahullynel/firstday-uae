"""
RelocationChecklistItem model - represents checklist items for relocation.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class RelocationChecklistItem(Base):
    """RelocationChecklistItem model for first-week relocation checklist."""

    __tablename__ = "relocation_checklist_items"

    id: int = Column(Integer, primary_key=True, index=True)
    city_id: int = Column(Integer, ForeignKey("cities.id"), nullable=False, index=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(String(500), nullable=True)
    category: str = Column(String(50), nullable=False, index=True)
    day_order: int = Column(Integer, nullable=False)
    official_link: str = Column(String(500), nullable=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    city = relationship("City", back_populates="checklists")

    def __repr__(self) -> str:
        return f"<ChecklistItem {self.title}>"
