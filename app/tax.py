from decimal import Decimal

from app.pricing import money


def add_tax(amount: Decimal, rate_percent: Decimal) -> Decimal:
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if not Decimal("0") <= rate_percent <= Decimal("100"):
        raise ValueError("rate_percent must be between 0 and 100")
    return money(amount * (Decimal("1") + rate_percent / Decimal("100")))
