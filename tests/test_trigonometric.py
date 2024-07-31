import unittest
import math

from function_package import *


class TestSin(unittest.TestCase):
    def test_call_1(self):
        sin = Sin()

        self.assertAlmostEqual(sin(0), 0.0)

    def test_call_2(self):
        sin = Sin()

        self.assertAlmostEqual(sin(math.pi/6), math.sin(math.pi/6))

    def test_derivative(self):
        sin = Sin()
        sin_derivative = sin.derivative()

        expected = Cos()

        self.assertEqual(str(sin_derivative), str(expected))

    def test_str_1(self):
        sin = Sin()

        expected = "sin(x)"

        self.assertEqual(str(sin), expected)

    def test_str_2(self):
        sin = Sin()
        cos = Cos()

        expected = "sin(cos(x))"

        self.assertEqual(str(sin.apply(cos)), expected)


class TestCos(unittest.TestCase):
    def test_call_1(self):
        cos = Cos()

        self.assertAlmostEqual(cos(0), 1.0)

    def test_call_2(self):
        cos = Cos()

        self.assertAlmostEqual(cos(math.pi / 6), math.cos(math.pi / 6))

    def test_derivative(self):
        cos = Cos()
        cos_derivative = cos.derivative()

        minus_1 = Polynomial(-1)
        expected = minus_1 * Sin()

        self.assertEqual(str(cos_derivative), str(expected))

    def test_str_1(self):
        cos = Cos()

        expected = "cos(x)"

        self.assertEqual(str(cos), expected)

    def test_str_2(self):
        sin = Sin()
        cos = Cos()

        expected = "cos(sin(x))"

        self.assertEqual(str(cos.apply(sin)), expected)


if __name__ == '__main__':
    unittest.main()
