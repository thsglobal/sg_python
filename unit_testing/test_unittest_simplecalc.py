# Unittest framework

from unit_testing.simplecalc import SimpleCalc
import unittest


# Define class that inherits from TestCase
class CalcTests(unittest.TestCase):
    def setUp(self):
        calc = SimpleCalc()
        print("Setting Up")

    def tearDown(self):
        pass

    def test_add(self):
        actual = self.calc.add(2,4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(2,4)
        expected = -2
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multiply(2,4)
        expected = 8
        self.assertAlmostEqual(actual, expected)

    def test_divide(self):
        actual = self.calc.divide(2,4)
        expected = 0.5
        self.assertAlmostEqual(actual, expected)