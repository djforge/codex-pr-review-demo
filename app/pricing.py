from decimal import Decimal, ROUND_HALF_UP


def money(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def subtotal(unit_price: Decimal, quantity: int) -> Decimal:
    if unit_price < 0:
        raise ValueError("unit_price must be non-negative")
    if quantity < 1:
        raise ValueError("quantity must be positive")
    return money(unit_price * quantity)


def apply_discount(amount: Decimal, percent: Decimal) -> Decimal:
    if not Decimal("0") <= percent <= Decimal("100"):
        raise ValueError("percent must be between 0 and 100")
    return money(amount * (Decimal("1") - percent / Decimal("100")))
