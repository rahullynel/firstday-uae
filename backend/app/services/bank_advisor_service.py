"""
Bank advisor service for personalized bank recommendations.

Recommends banks based on salary, remittance needs, digital banking
preference, and credit card rewards interest.
"""

from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime

from app.models import Bank, BankOffer
from app.schemas.bank_recommendation import (
    ActiveBankOffer,
    BankRecommendationDetail,
    BankRecommendationResponse,
)


def get_bank_recommendations(
    db: Session,
    monthly_salary: float,
    remittance_need: str,
    prefers_digital_banking: bool,
    wants_credit_card_rewards: bool,
) -> BankRecommendationResponse:
    """
    Get personalized bank recommendations based on user preferences.
    
    Args:
        db: SQLAlchemy session
        monthly_salary: Monthly salary in AED
        remittance_need: 'low', 'medium', or 'high'
        prefers_digital_banking: Whether digital banking is important
        wants_credit_card_rewards: Whether credit card offers are important
    
    Returns:
        BankRecommendationResponse with ranked bank recommendations
    """
    # Query eligible banks (salary requirement met)
    eligible_banks = db.query(Bank).filter(
        (Bank.min_salary_requirement == None) | (Bank.min_salary_requirement <= monthly_salary)
    ).all()
    
    if not eligible_banks:
        return BankRecommendationResponse(
            monthly_salary=monthly_salary,
            remittance_need=remittance_need,
            prefers_digital_banking=prefers_digital_banking,
            wants_credit_card_rewards=wants_credit_card_rewards,
            recommendations=[],
            total_matches=0,
            explanation="No banks found matching your salary requirement."
        )
    
    # Determine weight allocation based on preferences
    weights = _calculate_weights(remittance_need, prefers_digital_banking)
    
    # Score each eligible bank
    scored_banks = []
    for bank in eligible_banks:
        score, reasons = _score_bank(
            bank=bank,
            db=db,
            weights=weights,
            wants_credit_card_rewards=wants_credit_card_rewards,
        )
        scored_banks.append((bank, score, reasons))
    
    # Sort by score (descending)
    scored_banks.sort(key=lambda x: x[1], reverse=True)
    
    # Build recommendations
    recommendations = []
    for bank, score, reasons in scored_banks:
        # Get active offers
        active_offers = _get_active_offers(bank, db)
        
        detail = BankRecommendationDetail(
            bank_name=bank.name,
            slug=bank.slug,
            website_url=bank.website_url,
            description=bank.description,
            remittance_score=bank.remittance_score or 0.0,
            digital_score=bank.digital_score or 0.0,
            branch_network_score=bank.branch_network_score or 0.0,
            total_score=round(score, 1),
            top_reasons=reasons,
            active_offers=active_offers,
        )
        recommendations.append(detail)
    
    # Build explanation
    explanation = _build_explanation(
        remittance_need=remittance_need,
        prefers_digital_banking=prefers_digital_banking,
        wants_credit_card_rewards=wants_credit_card_rewards,
        top_bank=recommendations[0] if recommendations else None,
    )
    
    return BankRecommendationResponse(
        monthly_salary=monthly_salary,
        remittance_need=remittance_need,
        prefers_digital_banking=prefers_digital_banking,
        wants_credit_card_rewards=wants_credit_card_rewards,
        recommendations=recommendations,
        total_matches=len(recommendations),
        explanation=explanation,
    )


def _calculate_weights(remittance_need: str, prefers_digital_banking: bool) -> dict:
    """Calculate score weights based on user preferences."""
    
    # Base remittance weights
    remittance_weights = {
        "low": 0.10,
        "medium": 0.25,
        "high": 0.40,
    }
    
    remittance_weight = remittance_weights.get(remittance_need, 0.10)
    
    # Digital banking weight
    digital_weight = 0.35 if prefers_digital_banking else 0.15
    
    # Branch network weight (always present)
    branch_weight = 0.25
    
    # Remaining weight for balance
    remaining = 1.0 - (remittance_weight + digital_weight + branch_weight)
    if remaining > 0:
        branch_weight += remaining
    
    return {
        "remittance": remittance_weight,
        "digital": digital_weight,
        "branch_network": branch_weight,
    }


def _score_bank(
    bank: Bank,
    db: Session,
    weights: dict,
    wants_credit_card_rewards: bool,
) -> tuple[float, list[str]]:
    """
    Score a bank based on user preferences.
    
    Returns:
        Tuple of (total_score, list_of_reasons)
    """
    # Get normalized scores (0-100 scale)
    remittance_score = bank.remittance_score or 0.0
    digital_score = bank.digital_score or 0.0
    branch_network_score = bank.branch_network_score or 0.0
    
    # Calculate weighted score
    total_score = (
        remittance_score * weights["remittance"] +
        digital_score * weights["digital"] +
        branch_network_score * weights["branch_network"]
    )
    
    # Bonus for credit card rewards if requested
    if wants_credit_card_rewards:
        active_offers = _get_active_offers(bank, db)
        if active_offers:
            # Add 5-10% bonus based on number of offers
            offers_bonus = min(10.0, len(active_offers) * 3.0)
            total_score += offers_bonus
    
    # Cap at 100
    total_score = min(100.0, total_score)
    
    # Generate reasons
    reasons = _generate_reasons(
        bank_name=bank.name,
        remittance_score=remittance_score,
        digital_score=digital_score,
        branch_network_score=branch_network_score,
        weights=weights,
        active_offers_count=len(_get_active_offers(bank, db)),
    )
    
    return total_score, reasons


def _get_active_offers(bank: Bank, db: Session) -> list[ActiveBankOffer]:
    """Get currently active offers for a bank (valid today)."""
    today = datetime.now().date()
    
    offers = db.query(BankOffer).filter(
        BankOffer.bank_id == bank.id,
        BankOffer.valid_from <= today,
        (BankOffer.valid_to == None) | (BankOffer.valid_to >= today),
    ).all()
    
    return [
        ActiveBankOffer(
            title=offer.title,
            description=offer.description,
            source_url=offer.source_url,
        )
        for offer in offers
    ]


def _generate_reasons(
    bank_name: str,
    remittance_score: float,
    digital_score: float,
    branch_network_score: float,
    weights: dict,
    active_offers_count: int,
) -> list[str]:
    """Generate human-readable reasons for bank recommendation."""
    reasons = []
    
    # Remittance reason
    if remittance_score >= 80:
        reasons.append("Excellent remittance services")
    elif remittance_score >= 60:
        reasons.append("Strong remittance capabilities")
    
    # Digital reason
    if digital_score >= 80:
        reasons.append("Outstanding digital banking platform")
    elif digital_score >= 60:
        reasons.append("Solid digital banking options")
    
    # Branch network reason
    if branch_network_score >= 80:
        reasons.append("Extensive branch network")
    elif branch_network_score >= 60:
        reasons.append("Good branch network coverage")
    
    # Credit card reason
    if active_offers_count > 0:
        if active_offers_count >= 2:
            reasons.append("Multiple credit card offers available")
        else:
            reasons.append("Active credit card rewards program")
    
    # Limit to top 5 reasons
    return reasons[:5]


def _build_explanation(
    remittance_need: str,
    prefers_digital_banking: bool,
    wants_credit_card_rewards: bool,
    top_bank: Optional[BankRecommendationDetail],
) -> str:
    """Build human-readable explanation of recommendations."""
    
    if not top_bank:
        return "No banks found matching your criteria."
    
    parts = [f"Based on your preferences, we recommend {top_bank.bank_name}."]
    
    if remittance_need == "high":
        parts.append("They offer excellent remittance services")
    elif remittance_need == "medium":
        parts.append("They provide good remittance options")
    
    if prefers_digital_banking:
        parts.append("with a world-class digital banking platform")
    
    if wants_credit_card_rewards and top_bank.active_offers:
        parts.append(f"and {len(top_bank.active_offers)} attractive credit card offers.")
    else:
        parts.append(".")
    
    return " ".join(parts)
