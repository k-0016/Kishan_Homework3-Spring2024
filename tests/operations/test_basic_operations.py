"""
Module: test_calculator_operations

This module contains unit tests for basic arithmetic operations of a calculator.
"""
import pytest
from calculator.operations.basic_operations import Add, Subtract, Multiply, Divide

# Parameterized test for addition
@pytest.mark.parametrize("operand1, operand2, expected_result", [(1, 2, 3), (4, -1, 3), (0, 0, 0)])
def test_add(operand1, operand2, expected_result):
    """Test addition operation with multiple sets of data."""
    assert Add().perform(operand1, operand2) == expected_result

# Parameterized test for subtraction
@pytest.mark.parametrize("operand1, operand2, expected_result", [(5, 2, 3), (3, 3, 0), (-1, -2, 1)])
def test_subtract(operand1, operand2, expected_result):
    """Test subtraction operation with multiple sets of data."""
    assert Subtract().perform(operand1, operand2) == expected_result

# Parameterized test for multiplication
@pytest.mark.parametrize("operand1, operand2, expected_result", [(2, 3, 6), (5, 0, 0), (-1, -1, 1)])
def test_multiply(operand1, operand2, expected_result):
    """Test multiplication operation with multiple sets of data."""
    assert Multiply().perform(operand1, operand2) == expected_result

# Parameterized test for division and divide by zero exception
@pytest.mark.parametrize("operand1, operand2, expected_result", [(6, 3, 2), (5, -1, -5), (0, 1, 0)])
def test_divide(operand1, operand2, expected_result):
    """Test division operation with multiple sets of data."""
    assert Divide().perform(operand1, operand2) == expected_result

# Testing divide by zero exception with parameterized data
@pytest.mark.parametrize("operand1, operand2", [(1, 0), (10, 0)])
def test_divide_by_zero(operand1, operand2):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        Divide().perform(operand1, operand2)
