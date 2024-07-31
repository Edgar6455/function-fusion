from .abstract_function import AbstractFunction
from .function_composition import CompositeFunction
from .operations import OperationType


class Polynomial(AbstractFunction):
    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for power, coefficient in enumerate(self.coefficients):
            result += coefficient * (x ** power)
        return result

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            return CompositeFunction(self, other, OperationType.ADD)

        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [0] * max_len

        for i in range(max_len):
            coefficient1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coefficient2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coefficients[i] = coefficient1 + coefficient2

        return Polynomial(*new_coefficients)

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            return CompositeFunction(self, other, OperationType.SUB)

        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [0] * max_len

        for i in range(max_len):
            coefficient1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coefficient2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coefficients[i] = coefficient1 - coefficient2

        return Polynomial(*new_coefficients)

    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            return CompositeFunction(self, other, OperationType.MUL)

        new_coefficients = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        for i, coefficient1 in enumerate(self.coefficients):
            for j, coefficient2 in enumerate(other.coefficients):
                new_coefficients[i + j] += coefficient1 * coefficient2

        return Polynomial(*new_coefficients)

    def derivative(self):
        if len(self.coefficients) == 1:
            return Polynomial(0)

        derivative_coefficients = [coeff * power for power, coeff in enumerate(self.coefficients) if power > 0]
        return Polynomial(*derivative_coefficients)

    def _get_string(self, inner=None):
        if not any(self.coefficients):
            return "0"

        inner_view = str(inner) if inner else "x"

        members = []
        for power, coeff in enumerate(self.coefficients):
            if coeff == 0:
                continue

            coeff_str = "" if coeff == 1 and power != 0 else "-" if coeff == -1 and power != 0 else str(coeff)

            if power == 0:
                member = coeff_str
            elif power == 1:
                member = f"{coeff_str}{inner_view}"
            else:
                member = f"{coeff_str}{inner_view}^{power}"

            members.append(member)

        result = members[0] if members else "0"

        for i, member in enumerate(members[1:], 1):
            result += " " + ('+' if member[0] != '-' else '-')
            result += " " + (member if member[0] != '-' else member[1:])
            if i != len(members) - 1:
                result += " "

        return result

    def __str__(self):
        return self._get_string()
