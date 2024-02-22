from decimal import Decimal, InvalidOperation
from calculator.services.calculator_service import CalculatorService
from calculator.operations.basic_operations import Add, Subtract, Multiply, Divide

# Assuming these operation classes are defined and implement a method called `perform`
operation_mappings = {
    'add': Add(),
    'subtract': Subtract(),
    'multiply': Multiply(),
    'divide': Divide(),
}

class Calculator:
    def __init__(self):
        self.supported_operations = list(operation_mappings.keys())

    def calculate(self, a, operation_input, b):
        """Perform calculation and return a float result."""
        try:
            a_decimal = Decimal(a)
            b_decimal = Decimal(b)
            operation_key = operation_input.strip().lower()

            if operation_key not in operation_mappings:
                raise ValueError(f"Unknown operation: {operation_input}")

            operation = operation_mappings[operation_key]

            if operation_key == 'divide' and b_decimal == 0:
                raise ValueError("Cannot divide by zero")

            result = CalculatorService.perform_operation(operation, a_decimal, b_decimal)
            return float(result)  # Keep float for test compatibility

        except InvalidOperation:
            raise ValueError(f"Invalid number input: {a} or {b} is not a valid number.")

def main():
    print("Calculator is running. Type 'exit' to quit.")
    print(f"Supported operations: {', '.join(Calculator().supported_operations)}")

    while True:
        user_input = input("Enter calculation (e.g., 5 add 3): ").strip()
        if user_input.lower() == 'exit':
            break

        try:
            a, operation_input, b = user_input.split()
            calculator = Calculator()  # Create a calculator for each calculation
            result = calculator.calculate(a, operation_input, b)
            print(f"The result of {a} {operation_input} {b} is equal to {result}")

        except ValueError as e:
            print(f"Error: {e}")

        except IndexError: 
            print("Error: Please enter your input in the format '<number1> <operation> <number2>'.")

        except Exception as e:  # Catch-all for unexpected issues
            print(f"An unexpected error occurred: {e}") 

if __name__ == '__main__':
    main()