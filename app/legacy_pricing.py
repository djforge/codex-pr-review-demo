def legacy_total(unit_price: float, quantity: int, discount_percent: float) -> float:
    """Calculate totals received from the legacy import feed."""
    discounted = unit_price * quantity * (1 - discount_percent / 100)
    return round(discounted, 2)
