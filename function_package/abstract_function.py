from abc import ABC, abstractmethod
from .operations import OperationType


class AbstractFunction(ABC):
    @abstractmethod
    def __call__(self, x):
        pass

    @abstractmethod
    def derivative(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __add__(self, other):
        from .function_composition import CompositeFunction
        return CompositeFunction(self, other, OperationType.ADD)

    def __sub__(self, other):
        from .function_composition import CompositeFunction
        return CompositeFunction(self, other, OperationType.SUB)

    def __mul__(self, other):
        from .function_composition import CompositeFunction
        return CompositeFunction(self, other, OperationType.MUL)

    def __truediv__(self, other):
        from .function_composition import CompositeFunction
        return CompositeFunction(self, other, OperationType.DIV)

    def apply(self, func):
        from .function_application import FunctionApplication
        return FunctionApplication(self, func)
