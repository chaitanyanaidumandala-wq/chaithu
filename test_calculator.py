import unittest
import calculator  # import your calculator functions


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 7), 21)
        self.assertEqual(calculator.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(5, 0), "Error! Division by zero.")


if __name__ == "__main__":
    unittest.main()
