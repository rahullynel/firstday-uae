"""Seed data for FirstDay UAE MVP database."""

from datetime import datetime
from sqlalchemy.orm import Session
from app.models import (
    City,
    Neighborhood,
    Amenity,
    Bank,
    BankOffer,
    RelocationChecklistItem,
    CostIndex,
)


SEED_DATA = {
    "cities": [
        {
            "name": "Abu Dhabi",
            "slug": "abu-dhabi",
            "country": "United Arab Emirates",
            "currency": "AED",
        }
    ],
    "neighborhoods": {
        "Abu Dhabi": [
            {
                "name": "Al Zahiyah",
                "slug": "al-zahiyah",
                "description": "Central area with good schools and family-oriented features",
                "avg_rent_min": 3200,
                "avg_rent_max": 3800,
                "family_score": 85,
                "walkability_score": 75,
                "latitude": 24.4500,
                "longitude": 54.3700,
            },
            {
                "name": "Hamdan Street",
                "slug": "hamdan-street",
                "description": "Downtown hub with shopping and business centers",
                "avg_rent_min": 3800,
                "avg_rent_max": 4600,
                "walkability_score": 90,
                "family_score": 65,
                "latitude": 24.4620,
                "longitude": 54.3670,
            },
            {
                "name": "Khalidiya",
                "slug": "khalidiya",
                "description": "Mix of residential and commercial areas",
                "avg_rent_min": 3400,
                "avg_rent_max": 4200,
                "walkability_score": 80,
                "family_score": 70,
                "latitude": 24.4300,
                "longitude": 54.3800,
            },
            {
                "name": "Al Reem Island",
                "slug": "al-reem-island",
                "description": "Modern waterfront development with high-rise apartments",
                "avg_rent_min": 5000,
                "avg_rent_max": 6000,
                "nightlife_score": 75,
                "walkability_score": 85,
                "latitude": 24.4956,
                "longitude": 54.3939,
            },
            {
                "name": "Tourist Club Area",
                "slug": "tourist-club-area",
                "description": "Central location near Corniche with family amenities",
                "avg_rent_min": 3600,
                "avg_rent_max": 4400,
                "family_score": 80,
                "walkability_score": 88,
                "latitude": 24.4800,
                "longitude": 54.3600,
            },
            {
                "name": "Electra Street",
                "slug": "electra-street",
                "description": "Mixed-use area with offices and residential units",
                "avg_rent_min": 3500,
                "avg_rent_max": 4300,
                "walkability_score": 85,
                "family_score": 72,
                "latitude": 24.4500,
                "longitude": 54.3600,
            },
            {
                "name": "Muroor",
                "slug": "muroor",
                "description": "Residential neighborhood with local amenities",
                "avg_rent_min": 2900,
                "avg_rent_max": 3500,
                "family_score": 75,
                "walkability_score": 70,
                "latitude": 24.4000,
                "longitude": 54.3500,
            },
            {
                "name": "Al Nahyan",
                "slug": "al-nahyan",
                "description": "Family-friendly area with parks and schools",
                "avg_rent_min": 2800,
                "avg_rent_max": 3400,
                "family_score": 88,
                "walkability_score": 72,
                "latitude": 24.3800,
                "longitude": 54.3500,
            },
        ]
    },
    "amenities_per_neighborhood": {
        "laundry": {
            "name": "Laundry Service",
            "category": "laundry",
            "address": None,
        },
        "grocery": {
            "name": "Supermarket",
            "category": "grocery",
            "address": None,
        },
        "pharmacy": {
            "name": "Pharmacy",
            "category": "pharmacy",
            "address": None,
        },
        "gym": {
            "name": "Fitness Center",
            "category": "gym",
            "address": None,
        },
        "eatery": {
            "name": "Restaurant/Café",
            "category": "eatery",
            "address": None,
        },
    },
    "banks": [
        {
            "name": "Emirates NBD",
            "slug": "emirates-nbd",
            "description": "Leading banking services provider across UAE",
            "digital_score": 92,
            "remittance_score": 85,
            "branch_network_score": 95,
        },
        {
            "name": "ADCB",
            "slug": "adcb",
            "description": "Abu Dhabi Commercial Bank",
            "digital_score": 88,
            "remittance_score": 80,
            "branch_network_score": 90,
        },
        {
            "name": "FAB",
            "slug": "fab",
            "description": "First Abu Dhabi Bank (merged)",
            "digital_score": 90,
            "remittance_score": 88,
            "branch_network_score": 85,
        },
        {
            "name": "Mashreq",
            "slug": "mashreq",
            "description": "Mashreq Bank - full-service banking",
            "digital_score": 85,
            "remittance_score": 82,
            "branch_network_score": 92,
        },
    ],
    "bank_offers": [
        {
            "bank_name": "Emirates NBD",
            "title": "Welcome Bonus",
            "description": "0% interest for 6 months on credit card",
            "offer_type": "credit_card",
        },
        {
            "bank_name": "Emirates NBD",
            "title": "Salary Account",
            "description": "Free account opening with monthly salary transfer",
            "offer_type": "account",
        },
        {
            "bank_name": "ADCB",
            "title": "Digital Banking",
            "description": "Instant account opening via mobile app",
            "offer_type": "account",
        },
        {
            "bank_name": "ADCB",
            "title": "Remittance Benefits",
            "description": "Reduced fees for international transfers",
            "offer_type": "transfer",
        },
        {
            "bank_name": "FAB",
            "title": "Zero Transfer Fee",
            "description": "No fees on domestic transfers",
            "offer_type": "transfer",
        },
        {
            "bank_name": "FAB",
            "title": "Expat Loans",
            "description": "Flexible loan terms for expatriates",
            "offer_type": "loan",
        },
        {
            "bank_name": "Mashreq",
            "title": "Welcome Package",
            "description": "Cash back on first transaction",
            "offer_type": "credit_card",
        },
        {
            "bank_name": "Mashreq",
            "title": "Bill Payment",
            "description": "Pay utilities free of charge",
            "offer_type": "service",
        },
    ],
    "checklist_items": [
        {
            "category": "Documentation",
            "title": "Valid Passport",
            "description": "Ensure your passport is valid for at least 6 months",
            "day_order": 1,
        },
        {
            "category": "Documentation",
            "title": "Visa Application",
            "description": "Complete visa application process with employer sponsorship",
            "day_order": 2,
        },
        {
            "category": "Housing",
            "title": "Apply for Housing",
            "description": "Start house hunting or finalize accommodation arrangement",
            "day_order": 3,
        },
        {
            "category": "Housing",
            "title": "Validate Lease Agreement",
            "description": "Review and sign the tenancy contract",
            "day_order": 4,
        },
        {
            "category": "Banking",
            "title": "Open Bank Account",
            "description": "Open a local bank account for salary and expenses",
            "day_order": 5,
        },
        {
            "category": "Utilities",
            "title": "Set Up Electricity/Water",
            "description": "Register for EWEC services in Abu Dhabi",
            "day_order": 6,
        },
        {
            "category": "Utilities",
            "title": "Internet & Mobile",
            "description": "Subscribe to internet and mobile services",
            "day_order": 7,
        },
        {
            "category": "Vehicle",
            "title": "Register Vehicle",
            "description": "Register your car with Abu Dhabi RTA if bringing one",
            "day_order": 8,
        },
        {
            "category": "Healthcare",
            "title": "Health Insurance",
            "description": "Arrange health insurance coverage",
            "day_order": 9,
        },
        {
            "category": "Education",
            "title": "Enroll Children",
            "description": "Apply to schools for dependent children",
            "day_order": 10,
        },
        {
            "category": "Social",
            "title": "Meet-up Groups",
            "description": "Join expat community groups and networks",
            "day_order": 11,
        },
        {
            "category": "Finance",
            "title": "Tax & Compliance",
            "description": "Understand tax obligations and local regulations",
            "day_order": 12,
        },
    ],
    "cost_index": {
        "Abu Dhabi": {
            "rent_index": 85,
            "grocery_index": 78,
            "transport_index": 70,
            "utility_index": 72,
            "dining_index": 75,
            "misc_index": 80,
        }
    },
}


def seed_database(db: Session) -> None:
    """
    Seed the database with initial data.
    
    This function is idempotent - it can be called multiple times safely.
    It checks for existing data before inserting.
    
    Args:
        db: SQLAlchemy database session
    """
    # Check if data already seeded
    existing_city = db.query(City).filter_by(name="Abu Dhabi").first()
    if existing_city:
        print("Database already seeded. Skipping.")
        return

    print("Seeding database...")

    # Create Cities
    cities_map = {}
    for city_data in SEED_DATA["cities"]:
        city = City(**city_data)
        db.add(city)
        db.flush()  # Get the ID
        cities_map[city.name] = city
        print(f"✓ Created city: {city.name}")

    # Create Neighborhoods and Amenities
    neighborhoods_map = {}
    for city_name, neighborhoods in SEED_DATA["neighborhoods"].items():
        city = cities_map[city_name]
        for nbhood_data in neighborhoods:
            neighborhood = Neighborhood(**nbhood_data, city_id=city.id)
            db.add(neighborhood)
            db.flush()
            neighborhoods_map[neighborhood.name] = neighborhood
            
            # Add amenities to neighborhood
            for amenity_key, amenity_data in SEED_DATA["amenities_per_neighborhood"].items():
                amenity = Amenity(
                    **amenity_data,
                    neighborhood_id=neighborhood.id,
                )
                db.add(amenity)
            
            print(f"✓ Created neighborhood: {neighborhood.name} with 5 amenities")

    # Create Banks
    banks_map = {}
    for bank_data in SEED_DATA["banks"]:
        bank = Bank(**bank_data)
        db.add(bank)
        db.flush()
        banks_map[bank.name] = bank
        print(f"✓ Created bank: {bank.name}")

    # Create Bank Offers
    for offer_data in SEED_DATA["bank_offers"]:
        bank_name = offer_data.pop("bank_name")
        bank = banks_map[bank_name]
        offer = BankOffer(**offer_data, bank_id=bank.id)
        db.add(offer)
    
    db.flush()
    offers_count = len(SEED_DATA["bank_offers"])
    print(f"✓ Created {offers_count} bank offers")

    # Create Relocation Checklist Items
    for item_data in SEED_DATA["checklist_items"]:
        # Assign to Abu Dhabi city
        city = cities_map["Abu Dhabi"]
        item = RelocationChecklistItem(**item_data, city_id=city.id)
        db.add(item)
    
    db.flush()
    items_count = len(SEED_DATA["checklist_items"])
    print(f"✓ Created {items_count} checklist items")

    # Create Cost Index
    for city_name, cost_data in SEED_DATA["cost_index"].items():
        city = cities_map[city_name]
        cost_index = CostIndex(
            city_id=city.id,
            rent_index=cost_data["rent_index"],
            grocery_index=cost_data["grocery_index"],
            transport_index=cost_data["transport_index"],
            utility_index=cost_data["utility_index"],
            dining_index=cost_data["dining_index"],
            misc_index=cost_data["misc_index"],
        )
        db.add(cost_index)
    
    db.flush()
    print(f"✓ Created cost index for Abu Dhabi")

    # Commit all changes
    db.commit()
    print("\n✅ Database seeding completed successfully!")
    print(f"   - 1 city (Abu Dhabi)")
    print(f"   - 8 neighborhoods")
    print(f"   - 40 amenities (5 per neighborhood)")
    print(f"   - 4 banks")
    print(f"   - 8 bank offers")
    print(f"   - 12 checklist items")
    print(f"   - 1 cost index record")
