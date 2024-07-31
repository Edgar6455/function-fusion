import math

from .abstract_function import AbstractFunction
from .polynomial import Polynomial


class Sin(AbstractFunction):
    def __call__(self, x):
        return math.sin(x)

    def derivative(self):
        return Cos()

    def _get_string(self, inner=None):
        if inner:
            return f"sin({str(inner)})"
        return "sin(x)"

    def __str__(self):
        return self._get_string()


class Cos(AbstractFunction):
    def __call__(self, x):
        return math.cos(x)

    def derivative(self):
        return Polynomial(-1) * Sin()

    def _get_string(self, inner=None):
        if inner:
            return f"cos({str(inner)})"
        return "cos(x)"

    def __str__(self):
        return self._get_string()
