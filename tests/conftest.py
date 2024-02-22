"""This is conftest.py file"""
from decimal import Decimal
import pytest
from faker import Faker

fake = Faker()

# Default options can be overridden using command-line arguments
DEFAULT_NUM_RECORDS = 10
DEFAULT_PRECISION = 2  # Default precision for division results

def generate_test_data(num_records, precision):
    """Generate test data for the specified number of records and precision for division results."""
    operations = ['add', 'subtract', 'multiply', 'divide']
    test_data = []
    for _ in range(num_records):
        a = fake.pydecimal(left_digits=2, right_digits=2, positive=True)  # More control over decimals
        b = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
        operation = fake.random_element(elements=operations)

        if operation == 'divide' and b == 0:
            expected = "Cannot divide by zero"
        elif operation == 'divide':
            expected = Decimal(a) / Decimal(b)
            expected = expected.quantize(Decimal(10) ** -precision)  # Control precision
        elif operation == 'multiply':
            expected = Decimal(a) * Decimal(b)
        elif operation == 'subtract':
            expected = Decimal(a) - Decimal(b)
        elif operation == 'add':
            expected = Decimal(a) + Decimal(b)
        else:
            expected = "Unknown operation"

        test_data.append((a, b, operation, expected))
    return test_data

def pytest_addoption(parser):
    """Add options to specify the number of test records and division precision."""
    parser.addoption("--num_records", action="store", type=int, default=DEFAULT_NUM_RECORDS, help="Number of test records to generate")
    parser.addoption("--precision", action="store", type=int, default=DEFAULT_PRECISION, help="Precision for division results")

@pytest.hookimpl(tryfirst=True)
def pytest_generate_tests(metafunc):
    """Generate tests dynamically based on the number of records and precision."""
    if {'a', 'b', 'operation', 'expected'}.issubset(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        precision = metafunc.config.getoption("precision")
        test_data = generate_test_data(num_records, precision)
        metafunc.parametrize("a,b,operation,expected", test_data, ids=[f"test_{i}" for i in range(len(test_data))])
