"""
Module-level docstring: This module provides utilities for generating test data and configuring pytest.
"""
from decimal import Decimal, InvalidOperation
import pytest
from faker import Faker
from calculator.operations.basic_operations import Add, Subtract, Multiply, Divide

fake = Faker()

def generate_test_data(num_records):
    """
    Generate test data for parameterized tests, with enhanced variability in operands and operations.
    """
    operation_mappings = {
        'add': Add(),
        'subtract': Subtract(),
        'multiply': Multiply(),
        'divide': Divide(),
        # Add more operations here as your application grows
    }

    for _ in range(num_records):
        # Introduce a chance for edge cases, including zeros, very large numbers, and high precision decimals
        a = Decimal(f"{fake.random_number(digits=fake.random_int(min=1, max=5))}{'.' + fake.random_number(digits=fake.random_int(min=1, max=2), fix_len=True) if fake.boolean() else ''}")
        b = Decimal(f"{fake.random_number(digits=fake.random_int(min=1, max=5))}{'.' + fake.random_number(digits=fake.random_int(min=1, max=2), fix_len=True) if fake.boolean() else ''}")
        # Chance to make 'a' or 'b' a specific edge case
        if fake.random_int(min=0, max=100) < 10:  # 10% chance
            a = Decimal(fake.random_element(elements=['0', '0.00001', '-0.00001', str(fake.random_int(min=100000, max=1000000))]))
        if fake.random_int(min=0, max=100) < 10:  # 10% chance for 'b', including division by zero explicitly
            b = Decimal(fake.random_element(elements=['0', '0.00001', '-0.00001', str(fake.random_int(min=100000, max=1000000)), '0']))  # Include '0' to test division by zero
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation = operation_mappings[operation_name]

        try:
            # Attempt to calculate expected result, accounting for operation behavior
            expected = operation.perform(a, b) if b != 0 or operation_name != 'divide' else "ZeroDivisionError"
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        except InvalidOperation:
            expected = "InvalidOperation"

        yield a, b, operation_name, expected

@pytest.hookimpl(tryfirst=True)
def pytest_addoption(parser):
    """
    Add a command-line option to specify the number of test records to generate.
    """
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records to generate")

@pytest.hookimpl(tryfirst=True)
def pytest_generate_tests(metafunc):
    """
    Dynamically generate test cases based on the specified number of records.
    """
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames and "operation_name" in metafunc.fixturenames and "expected" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("a,b,operation_name,expected", parameters)
