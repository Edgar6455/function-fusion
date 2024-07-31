from abc import ABC, abstractmethod


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
        return CompositeFunction(self, other, 'add')

    def __sub__(self, other):
        from .function_composition import CompositeFunction
        return CompositeFunction(self, other, 'sub')

    def __mul__(self, other):
        from .function_composition import CompositeFunction
        return CompositeFunction(self, other, 'mul')

    def __truediv__(self, other):
        from .function_composition import CompositeFunction
        return CompositeFunction(self, other, 'div')

    def apply(self, func):
        from .function_application import FunctionApplication
        return FunctionApplication(self, func)
