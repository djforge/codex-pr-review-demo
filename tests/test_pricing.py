import unittest
from decimal import Decimal

from app.orders import Order
from app.pricing import apply_discount, subtotal


class PricingTests(unittest.TestCase):
    def test_subtotal(self):
        self.assertEqual(subtotal(Decimal("12.50"), 2), Decimal("25.00"))

    def test_discount(self):
        self.assertEqual(apply_discount(Decimal("100"), Decimal("15")), Decimal("85.00"))

    def test_order_total(self):
        order = Order("DEMO-1", Decimal("19.99"), 3, Decimal("10"))
        self.assertEqual(order.total(), Decimal("53.97"))

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            subtotal(Decimal("5"), 0)


if __name__ == "__main__":
    unittest.main()
