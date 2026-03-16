"""
Bank model - represents banks operating in the UAE.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from app.models.base import Base


class Bank(Base):
    """Bank model representing a financial institution."""

    __tablename__ = "banks"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), unique=True, nullable=False, index=True)
    slug: str = Column(String(100), unique=True, nullable=False, index=True)
    min_salary_requirement: float = Column(Float, nullable=True)
    digital_score: float = Column(Float, nullable=True)
    remittance_score: float = Column(Float, nullable=True)
    branch_network_score: float = Column(Float, nullable=True)
    website_url: str = Column(String(500), nullable=True)
    description: str = Column(String(500), nullable=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    offers = relationship("BankOffer", back_populates="bank", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Bank {self.name}>"
