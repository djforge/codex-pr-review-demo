from decimal import Decimal

from app.pricing import money


def refund_amount(paid: Decimal, restocking_percent: Decimal) -> Decimal:
    """Calculate a refund after the restocking fee."""
    return money(paid * (Decimal("1") - restocking_percent / Decimal("100")))
