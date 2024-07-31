from enum import Enum


class OperationType(Enum):
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"


class OperationFactory:
    _operations = {
        OperationType.ADD: {
            'apply': lambda f1, f2, x: f1(x) + f2(x),
            'derivative': lambda f1, f2: f1.derivative() + f2.derivative(),
            'to_string': lambda f1_str, f2_str: f"({f1_str}) + ({f2_str})"
        },
        OperationType.SUB: {
            'apply': lambda f1, f2, x: f1(x) - f2(x),
            'derivative': lambda f1, f2: f1.derivative() - f2.derivative(),
            'to_string': lambda f1_str, f2_str: f"({f1_str}) - ({f2_str})"
        },
        OperationType.MUL: {
            'apply': lambda f1, f2, x: f1(x) * f2(x),
            'derivative': lambda f1, f2: f1.derivative() * f2 + f1 * f2.derivative(),
            'to_string': lambda f1_str, f2_str: f"({f1_str}) * ({f2_str})"
        },
        OperationType.DIV: {
            'apply': lambda f1, f2, x: f1(x) / f2(x),
            'derivative': lambda f1, f2: (f1.derivative() * f2 - f1 * f2.derivative()) / (f2 * f2),
            'to_string': lambda f1_str, f2_str: f"({f1_str}) / ({f2_str})"
        }
    }

    @classmethod
    def get_operation(cls, operation: OperationType):
        return cls._operations[operation]

    @staticmethod
    def apply(operation: OperationType, f1, f2, x):
        return OperationFactory.get_operation(operation)['apply'](f1, f2, x)

    @staticmethod
    def derivative(operation: OperationType, f1, f2):
        return OperationFactory.get_operation(operation)['derivative'](f1, f2)

    @staticmethod
    def to_string(operation: OperationType, f1_str, f2_str):
        return OperationFactory.get_operation(operation)['to_string'](f1_str, f2_str)
