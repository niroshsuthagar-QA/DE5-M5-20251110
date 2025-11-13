import unittest
from calculator_app import Calculator

class TestOperations(unittest.TestCase):

    def test_div(self):
        calc = Calculator(10, 2)
        self.assertEqual(calc.get_quotient(), 5, "The division is wrong")

    def test_sum(self):
        calc = Calculator(10, 2)
        self.assertEqual(calc.get_sum(), 12, "The answer is wrong")

    def test_minus(self):
        calc = Calculator(10, 2)
        self.assertEqual(calc.get_difference(), 8, "The answer is wrong")

    def test_prod(self):
        calc = Calculator(10, 2)
        self.assertEqual(calc.get_product(), 20, "The answer is wrong")


if __name__ == "__main__":
    unittest.main()

        