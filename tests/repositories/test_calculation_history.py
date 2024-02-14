"""Module for testing the Calculation model."""
from calculator.repositories.calculation_history import CalculationHistory
from calculator.models.calculation import Calculation

def test_add_and_retrieve_last_calculation():
    """Test add and retrieve last calculation."""
    CalculationHistory.clear_history()  # Ensure a clean state
    calculation = Calculation("add", (1, 2), 3)
    CalculationHistory.add_calculation("add", (1, 2), 3)
    last_calc = CalculationHistory.get_last_calculation()
    assert last_calc.operation == calculation.operation
    assert last_calc.operands == calculation.operands
    assert last_calc.result == calculation.result

def test_clear_history():
    """Test Clear History."""
    CalculationHistory.add_calculation("subtract", (10, 5), 5)
    CalculationHistory.clear_history()
    assert CalculationHistory.get_last_calculation() is None
