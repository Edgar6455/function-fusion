import unittest
import math

from function_package import *


class TestApplication(unittest.TestCase):
    def test_apply_1(self):
        sin = Sin()
        cos = Cos()

        # cos(2x) == (cosx)^2 - (sinx)^2

        _2x = Polynomial(0, 2)
        cos2x = cos.apply(_2x)

        cosx_sq = cos * cos
        sinx_sq = sin * sin

        expected = cosx_sq - sinx_sq
        pi3 = math.pi / 3

        self.assertAlmostEqual(cos2x(pi3), expected(pi3))

    def test_apply_2(self):
        sin = Sin()
        cos = Cos()

        # (sin(x/2))^2 == (1 - cosx) / 2

        x2 = Polynomial(0, 0.5)
        sinx2 = sin.apply(x2)
        sinx2_sq = sinx2 * sinx2

        one = Polynomial(1)
        two = Polynomial(2)
        one_minus_cosx = one - cos

        expected = one_minus_cosx / two

        pi6 = math.pi / 6

        self.assertAlmostEqual(sinx2_sq(pi6), expected(pi6))

    def test_derivative(self):
        sin = Sin()
        cos = Cos()

        # (sin(x^2))' == (cos(x^2)) * (2x)

        x2 = Polynomial(0, 0, 1)
        sinx2 = sin.apply(x2)
        sinx2_derivative = sinx2.derivative()

        cosx2 = cos.apply(x2)
        _2x = Polynomial(0, 2)

        expected = cosx2 * _2x
        self.assertEqual(str(sinx2_derivative), str(expected))

        pi4 = math.pi / 4
        self.assertAlmostEqual(sinx2_derivative(pi4), expected(pi4))

    def test_str_1(self):
        sin = Sin()
        cos = Cos()

        sincosx = sin.apply(cos)

        expected = "sin(cos(x))"
        self.assertEqual(str(sincosx), expected)

    def test_str_2(self):
        sin = Sin()
        cos = Cos()

        cossinx = cos.apply(sin)
        _1_minus_x2 = Polynomial(1, 0, -2)
        cossin_1_minus_x2 = cossinx.apply(_1_minus_x2)

        expected = "cos(sin(1 - 2x^2))"
        self.assertEqual(str(cossin_1_minus_x2), expected)


if __name__ == '__main__':
    unittest.main()
