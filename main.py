from decimal import Decimal, InvalidOperation
from calculator.services.calculator_service import CalculatorService
from calculator.operations.basic_operations import Add, Subtract, Multiply, Divide
import re

def calculate_and_print(a, b, operation_input):
    # Enhanced mapping to support both symbols and text for operations
    operation_mappings = {
        '+': Add(),
        'add': Add(),
        '-': Subtract(),
        'subtract': Subtract(),
        '*': Multiply(),
        'multiply': Multiply(),
        '/': Divide(),
        'divide': Divide()
    }

    try:
        a_decimal = Decimal(a)
        b_decimal = Decimal(b)
        
        # Normalize operation input to handle both symbols and text
        operation_input = operation_input.strip().lower()
        operation = operation_mappings.get(operation_input)

        if operation is None:
            print(f"Unknown operation: {operation_input}")
            return

        result = CalculatorService.perform_operation(operation, a_decimal, b_decimal)
        print(f"The result of {a} {operation_input} {b} is equal to {result}")

    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_user_input(user_input: str):
    # This regex now also captures non-numeric and textual operations
    parts = re.findall(r'([^ ]+)\s*([^ ]+)\s*([^ ]+)', user_input)
    if parts:
        return parts[0]
    raise ValueError("Invalid input format. Please use the format: <number> <operation> <number>.")


if __name__ == "__main__":
    print("Welcome to Calculator! Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter calculation (e.g., '5 + 3' or '5 add 3'): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting Calculator. Goodbye!")
            break
        
        try:
            a, operation, b = parse_user_input(user_input)
            # Normalize operation to handle both textual and symbol inputs
            operation_normalized = 'add' if operation == '+' else 'subtract' if operation == '-' else 'multiply' if operation == '*' else 'divide' if operation == '/' else operation
            calculate_and_print(a, b, operation_normalized)
        except ValueError as e:
            print(f"{e} Example: 5 * 3 or 5 multiply 3")
        except Exception as e:
            print(f"An error occurred: {e}")
