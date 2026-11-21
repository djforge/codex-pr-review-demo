import unittest
from decimal import Decimal

from app.pricing import money


class RoundingTests(unittest.TestCase):
    def test_rounds_half_up(self):
        self.assertEqual(money(Decimal("1.005")), Decimal("1.01"))

    def test_preserves_two_places(self):
        self.assertEqual(money(Decimal("4")), Decimal("4.00"))
