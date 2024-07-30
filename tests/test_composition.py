import unittest
import math

from function_package import *


class TestComposition(unittest.TestCase):
    def test_add(self):
        two = Polynomial(2)
        cos = Cos()
        pi6 = math.pi / 6

        p1_add_cos = two + cos

        expected = 2 + math.cos(pi6)

        self.assertAlmostEqual(p1_add_cos(pi6), expected)

    def test_sub(self):
        _2_add_3x = Polynomial(2, 3)
        cos = Cos()
        pi4 = math.pi / 4

        cos_sub_p1 = cos - _2_add_3x

        expected = math.cos(pi4) - (2 + 3*pi4)

        self.assertAlmostEqual(cos_sub_p1(pi4), expected)

    def test_mul(self):
        sin = Sin()
        cos = Cos()
        two = Polynomial(2)

        _2sinxcosx = two * sin * cos

        _2x = Polynomial(0, 2)
        sin2x = sin.apply(_2x)

        pi3 = math.pi / 3
        self.assertAlmostEqual(_2sinxcosx(pi3), sin2x(pi3))

    def test_div(self):
        sin = Sin()
        cos = Cos()

        ctg = cos / sin
        self.assertAlmostEqual(ctg(math.pi/4), 1.0)

    def test_derivative_add(self):
        sin = Sin()
        cos = Cos()

        sin_derivative = sin.derivative()
        cos_derivative = cos.derivative()

        sin_add_cos = sin + cos
        sin_add_cos_derivative = sin_add_cos.derivative()

        pi4 = math.pi / 4

        self.assertAlmostEqual(sin_add_cos_derivative(pi4), sin_derivative(pi4) + cos_derivative(pi4))

    def test_derivative_sub(self):
        sin = Sin()
        cos = Cos()

        sin_derivative = sin.derivative()
        cos_derivative = cos.derivative()

        sin_sub_cos = sin - cos
        sin_sub_cos_derivative = sin_sub_cos.derivative()

        pi6 = math.pi / 6

        self.assertAlmostEqual(sin_sub_cos_derivative(pi6), sin_derivative(pi6) - cos_derivative(pi6))

    def test_derivative_mul(self):
        sin = Sin()
        cos = Cos()

        sin_derivative = sin.derivative()
        cos_derivative = cos.derivative()

        sin_mul_cos = sin * cos
        sin_mul_cos_derivative = sin_mul_cos.derivative()

        pi3 = math.pi / 3

        expected = sin_derivative(pi3) * cos(pi3) + cos_derivative(pi3) * sin(pi3)

        self.assertAlmostEqual(sin_mul_cos_derivative(pi3), expected)

    def test_derivative_div(self):
        sin = Sin()
        cos = Cos()

        sin_derivative = sin.derivative()
        cos_derivative = cos.derivative()

        ctg = cos / sin
        ctg_derivative = ctg.derivative()

        pi6 = math.pi / 6

        numerator = cos_derivative(pi6) * sin(pi6) - cos(pi6) * sin_derivative(pi6)
        denominator = sin(pi6) * sin(pi6)
        expected = numerator / denominator

        self.assertAlmostEqual(ctg_derivative(pi6), expected)

    def test_str_add(self):
        sin = Sin()
        cos = Cos()

        sin_add_cos = sin + cos

        expected = "(" + str(sin) + ") + (" + str(cos) + ")"

        self.assertEqual(str(sin_add_cos), expected)

    def test_str_div(self):
        p1 = Polynomial(2, 3, 4)
        p2 = Polynomial(1, 4, 2)

        p3 = p1 / p2

        expected = "(" + str(p1) + ") / (" + str(p2) + ")"

        self.assertEqual(str(p3), expected)


if __name__ == '__main__':
    unittest.main()
