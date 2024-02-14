from calculator.interfaces.operation_interface import OperationInterface

class Add(OperationInterface):
    def perform(self, a: float, b: float) -> float:
        return a + b

class Subtract(OperationInterface):
    def perform(self, a: float, b: float) -> float:
        return a - b

class Multiply(OperationInterface):
    def perform(self, a: float, b: float) -> float:
        return a * b

class Divide(OperationInterface):
    def perform(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
