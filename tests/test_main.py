"""
This test_main.py file contains unit tests for the main.py module.
"""
from decimal import Decimal
import pytest
from main import Calculator

@pytest.fixture
def calculator():
    """Function Calculator"""
    return Calculator()
# Fixtures provided by conftest.py to generate test data
# ('a', 'b', 'operation', 'expected')
def test_calculate(a, b, operation, expected, calculator): # pylint: disable=invalid-name
    """Test the calculate method with dynamically generated data."""
    a_decimal = Decimal(a)
    b_decimal = Decimal(b)
    result = calculator.calculate(a_decimal, operation, b_decimal)

    # Handle special cases
    if expected == "Cannot divide by zero":
        with pytest.raises(ValueError) as excinfo:
            result = calculator.calculate(a_decimal, operation, b_decimal) # Calculation should raise the error
        assert "Cannot divide by zero" in str(excinfo.value)
    elif expected == "Unknown operation":
        with pytest.raises(ValueError) as excinfo:
            result = calculator.calculate(a_decimal, operation, b_decimal) # Calculation should raise the error
        assert "Unknown operation" in str(excinfo.value)
    else:
        tolerance = 0.01  # Adjust as needed
        assert abs(result - float(expected)) <= tolerance
