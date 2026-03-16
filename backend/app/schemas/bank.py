"""
Bank and BankOffer schemas.
"""

from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class BankOfferBase(BaseModel):
    """Base bank offer schema."""

    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=500)
    offer_type: str = Field(..., min_length=1, max_length=50)
    source_url: Optional[str] = Field(None, max_length=500)
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None


class BankOfferCreate(BankOfferBase):
    """Schema for creating a bank offer."""

    bank_id: int


class BankOfferRead(BankOfferBase):
    """Schema for reading bank offer data."""

    id: int
    bank_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class BankBase(BaseModel):
    """Base bank schema."""

    name: str = Field(..., min_length=1, max_length=100)
    slug: str = Field(..., min_length=1, max_length=100)
    min_salary_requirement: Optional[float] = Field(None, ge=0)
    digital_score: Optional[float] = Field(None, ge=0, le=100)
    remittance_score: Optional[float] = Field(None, ge=0, le=100)
    branch_network_score: Optional[float] = Field(None, ge=0, le=100)
    website_url: Optional[str] = Field(None, max_length=500)
    description: Optional[str] = Field(None, max_length=500)


class BankCreate(BankBase):
    """Schema for creating a bank."""

    pass


class BankRead(BankBase):
    """Schema for reading bank data."""

    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class BankWithOffers(BankRead):
    """Bank with nested offers."""

    offers: list[BankOfferRead] = []
