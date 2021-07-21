# test_stock.py
#
# Exercise 8.2: Writing Unit Tests

import unittest
import stock

class TestStock(unittest.TestCase):
    
    def test_create(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = stock.Stock("GOOG", 100, 490.1)
        cost = s.cost
        self.assertEqual(cost, 49010.0)

    def test_sell(self):
        s = stock.Stock("GOOG", 100, 490.1)
        s.sell(25)
        shares = s.shares
        self.assertEqual(shares, 75)

    def test_str_shares(self):
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertRaises(TypeError, s.shares, "twenty")
        with self.assertRaises(TypeError):
            s.shares = "100"
        # both ways work

if __name__ == "__main__":
    unittest.main()