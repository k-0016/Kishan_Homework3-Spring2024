from typing import Callable
from calculator.repositories.calculation_history import CalculationHistory
from calculator.interfaces.operation_interface import OperationInterface
from calculator.models.calculation import Calculation

class CalculatorService:
    @staticmethod
    def perform_operation(operation: OperationInterface, a: float, b: float) -> float:
        result = operation.perform(a, b)
        CalculationHistory.add_calculation(operation.__class__.__name__, (a, b), result)
        return result
