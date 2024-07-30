import unittest

from function_package import *


class TestPolynomial(unittest.TestCase):
    def test_call(self):
        p1 = Polynomial(1, 2, 3)

        self.assertEqual(p1(2), 17)  # 1 + 2*2 + 3*2^2

    def test_add(self):
        p1 = Polynomial(3, 2)
        p2 = Polynomial(1, 1, 1)
        p12 = p1 + p2

        expected = Polynomial(4, 3, 1)

        self.assertEqual(str(p12), str(expected))

    def test_sub(self):
        p1 = Polynomial(6, 7, 8)
        p2 = Polynomial(9, 1)
        p12 = p1 - p2

        expected = Polynomial(-3, 6, 8)

        self.assertEqual(str(p12), str(expected))

    def test_mul(self):
        p1 = Polynomial(2, 3)
        p2 = Polynomial(1, 2)
        p12 = p1 * p2

        expected = Polynomial(2, 7, 6)

        self.assertEqual(str(p12), str(expected))

    def test_derivative_1(self):
        p1 = Polynomial(1, 2, 3, 4)
        p1_derivative = p1.derivative()

        expected = Polynomial(2, 6, 12)

        self.assertEqual(str(p1_derivative), str(expected))

    def test_derivative_2(self):
        p1 = Polynomial(10)
        p1_derivative = p1.derivative()

        expected = Polynomial(0)

        self.assertEqual(str(p1_derivative), str(expected))


if __name__ == '__main__':
    unittest.main()
