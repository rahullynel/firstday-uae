"""
BankOffer model - represents promotional offers from banks.
"""

from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.models.base import Base


class BankOffer(Base):
    """BankOffer model representing a promotional offer from a bank."""

    __tablename__ = "bank_offers"

    id: int = Column(Integer, primary_key=True, index=True)
    bank_id: int = Column(Integer, ForeignKey("banks.id"), nullable=False, index=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(String(500), nullable=True)
    offer_type: str = Column(String(50), nullable=False, index=True)
    source_url: str = Column(String(500), nullable=True)
    valid_from: date = Column(Date, nullable=True)
    valid_to: date = Column(Date, nullable=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    bank = relationship("Bank", back_populates="offers")

    def __repr__(self) -> str:
        return f"<BankOffer {self.title}>"
