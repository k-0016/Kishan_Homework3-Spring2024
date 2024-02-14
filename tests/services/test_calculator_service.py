"""Module for testing the Calculation model."""
import pytest
from calculator.services.calculator_service import CalculatorService
from calculator.operations.basic_operations import Add, Subtract, Multiply, Divide
from calculator.repositories.calculation_history import CalculationHistory

@pytest.fixture
def calculator_service():
    """Test Calculator Service."""
    CalculationHistory.clear_history()  # Ensure a clean state before each test
    return CalculatorService()

def test_perform_add_operation(calculator_service):
    """Test Perfrom addition operation."""
    result = calculator_service.perform_operation(Add(), 1, 2)
    assert result == 3
    assert CalculationHistory.get_last_calculation().result == 3

def test_perform_subtract_operation(calculator_service):
    """Test Perform Substraction operation."""
    result = calculator_service.perform_operation(Subtract(), 5, 3)
    assert result == 2
    assert CalculationHistory.get_last_calculation().result == 2

def test_perform_multiply_operation(calculator_service):
    """Test Perform Multiply operation."""
    result = calculator_service.perform_operation(Multiply(), 3, 4)
    assert result == 12
    assert CalculationHistory.get_last_calculation().result == 12

def test_perform_divide_operation(calculator_service):
    """Test Divide operation."""
    result = calculator_service.perform_operation(Divide(), 8, 2)
    assert result == 4
    assert CalculationHistory.get_last_calculation().result == 4

def test_divide_by_zero_raises_exception(calculator_service):
    """Test divide by zero operation."""
    with pytest.raises(ValueError):
        calculator_service.perform_operation(Divide(), 1, 0)
