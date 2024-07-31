from .abstract_function import AbstractFunction


class CompositeFunction(AbstractFunction):
    def __init__(self, f1, f2, operation):
        self.f1 = f1
        self.f2 = f2
        self.operation = operation

    def __call__(self, x):
        if self.operation == 'add':
            return self.f1(x) + self.f2(x)
        elif self.operation == 'sub':
            return self.f1(x) - self.f2(x)
        elif self.operation == 'mul':
            return self.f1(x) * self.f2(x)
        elif self.operation == 'div':
            return self.f1(x) / self.f2(x)

    def derivative(self):
        if self.operation == 'add':
            return self.f1.derivative() + self.f2.derivative()
        elif self.operation == 'sub':
            return self.f1.derivative() - self.f2.derivative()
        elif self.operation == 'mul':
            return self.f1.derivative() * self.f2 + self.f1 * self.f2.derivative()
        elif self.operation == 'div':
            numerator = self.f1.derivative() * self.f2 - self.f1 * self.f2.derivative()
            denominator = self.f2 * self.f2
            return numerator / denominator

    def __str__(self):
        f1_str = str(self.f1)
        f2_str = str(self.f2)

        if self.operation == 'add':
            return f"({f1_str}) + ({f2_str})"
        elif self.operation == 'sub':
            return f"({f1_str}) - ({f2_str})"
        elif self.operation == 'mul':
            return f"({f1_str}) * ({f2_str})"
        elif self.operation == 'div':
            return f"({f1_str}) / ({f2_str})"
