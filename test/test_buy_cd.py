import unittest
from unittest.mock import MagicMock

from src.compact_disc import CompactDisc
from src.credit_card import CreditCard
from src.payments import Payments


class BuyCdTest(unittest.TestCase):
    def test_cd_in_stock_payment_accepted(self):
        payments = Payments()
        payments.pay = MagicMock(return_value=True)
        cd = CompactDisc(9.99, 10, payments)
        card = CreditCard()
        cd.buy(1, card)
        self.assertEqual(9, cd.stock)


if __name__ == '__main__':
    unittest.main()
