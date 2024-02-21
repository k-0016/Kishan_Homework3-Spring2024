"""
Module-level docstring: This module contains unit tests for the functions in main.py.
"""
import sys
from io import StringIO
import pytest
from main import calculate_and_print, parse_user_input

def capture_print_output(func, *args, **kwargs):
    """
    Captures and returns the output of a function that prints to stdout.
    
    :param func: The function to capture the output from.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: The captured output as a string.
    """
    original_stdout = sys.stdout  # Save the original stdout
    sys.stdout = StringIO()  # Replace stdout with StringIO to capture output
    func(*args, **kwargs)
    output = sys.stdout.getvalue()  # Get the printed output
    sys.stdout = original_stdout  # Restore original stdout
    return output.strip()

@pytest.mark.parametrize("input_str, expected_output", [
    ("5 + 3", "The result of 5 + 3 is equal to 8"),
    ("10 - 2", "The result of 10 - 2 is equal to 8"),
    ("4 * 5", "The result of 4 * 5 is equal to 20"),
    ("20 / 4", "The result of 20 / 4 is equal to 5"),
    ("1 / 0", "An error occurred: Cannot divide by zero."),
    ("-100 + 200", "The result of -100 + 200 is equal to 100"),
    ("9999999 * 0.0001", "The result of 9999999 * 0.0001 is equal to 999.9999"),
    ("a + 3", "Invalid number input: a or 3 is not a valid number."),
    ("5 - b", "Invalid number input: 5 or b is not a valid number."),
    ("9 unknown 3", "Unknown operation: unknown"),
])
def test_calculate_and_print_with_various_inputs(input_str, expected_output):
    """
    Test calculate_and_print function with various inputs.
    """
    a, operation, b = parse_user_input(input_str)
    actual_output = capture_print_output(calculate_and_print, a, b, operation)
    assert actual_output == expected_output
