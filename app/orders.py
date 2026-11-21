from dataclasses import dataclass
from decimal import Decimal

from app.pricing import apply_discount, subtotal


@dataclass(frozen=True)
class Order:
    sku: str
    unit_price: Decimal
    quantity: int
    discount_percent: Decimal = Decimal("0")

    def total(self) -> Decimal:
        return apply_discount(subtotal(self.unit_price, self.quantity), self.discount_percent)
