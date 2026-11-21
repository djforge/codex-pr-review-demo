import unittest
from decimal import Decimal

from app.pricing import apply_discount


class RegressionTests(unittest.TestCase):
    def test_discount_regression(self):
        self.assertEqual(apply_discount(Decimal("100"), Decimal("10")), Decimal("91.00"))
