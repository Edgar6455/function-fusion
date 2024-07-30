import math

from .abstract_function import AbstractFunction
from .polynomial import Polynomial


class Sin(AbstractFunction):
    def __call__(self, x):
        return math.sin(x)

    def derivative(self):
        return Cos()

    def __str__(self, inner=None):
        if inner:
            return f"sin({str(inner)})"
        return "sin(x)"


class Cos(AbstractFunction):
    def __call__(self, x):
        return math.cos(x)

    def derivative(self):
        return Polynomial(-1) * Sin()

    def __str__(self, inner=None):
        if inner:
            return f"cos({str(inner)})"
        return "cos(x)"
