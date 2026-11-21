from decimal import Decimal

from app.pricing import money


def shipping_cost(weight_kg: Decimal, rate_per_kg: Decimal) -> Decimal:
    """Return a rounded shipping charge for a positive parcel weight."""
    if weight_kg <= 0:
        raise ValueError("weight_kg must be positive")
    if rate_per_kg < 0:
        raise ValueError("rate_per_kg must be non-negative")
    return money(weight_kg * rate_per_kg)
