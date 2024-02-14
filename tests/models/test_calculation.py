"""Module for testing the Calculation model."""

from calculator.models.calculation import Calculation

def test_calculation_creation():
    """Test creation and properties of a Calculation instance."""
    operation = "add"
    operands = (1, 2)
    result = 3
    calculation = Calculation(operation, operands, result)
    assert calculation.operation == operation
    assert calculation.operands == operands
    assert calculation.result == result
