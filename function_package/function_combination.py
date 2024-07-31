from .abstract_function import AbstractFunction
from .operations import OperationFactory, OperationType


class CompositeFunction(AbstractFunction):
    def __init__(self, f1, f2, operation: OperationType):
        self.f1 = f1
        self.f2 = f2
        self.operation = operation

    def __call__(self, x):
        return OperationFactory.apply(self.operation, self.f1, self.f2, x)

    def derivative(self):
        return OperationFactory.derivative(self.operation, self.f1, self.f2)

    def __str__(self):
        f1_str = str(self.f1)
        f2_str = str(self.f2)
        return OperationFactory.to_string(self.operation, f1_str, f2_str)
