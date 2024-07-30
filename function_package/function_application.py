from .abstract_function import AbstractFunction


class FunctionApplication(AbstractFunction):
    def __init__(self, outer_func, inner_func):
        self.outer_func = outer_func
        self.inner_func = inner_func

    def __call__(self, x):
        return self.outer_func(self.inner_func(x))

    def derivative(self):
        outer_derivative = self.outer_func.derivative()
        inner_derivative = self.inner_func.derivative()
        return FunctionApplication(outer_derivative, self.inner_func) * inner_derivative

    def __str__(self, inner=None):
        if inner:
            self.inner_func = self.inner_func.apply(inner)

        return f"{self.outer_func.__str__(self.inner_func)}"
