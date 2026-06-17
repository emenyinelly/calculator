import math


class Calculator:
    def __init__(self):
        """Initialize the calculator with basic mathematical operations."""
        self.operations = {}
        self.init()

    def init(self):
        """Set up the basic mathematical operations (+, -, *, /)."""
        self.operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

    def add_operation(self, symbol, func):
        """
        Add a new operation to the calculator.

        Args:
            symbol (str): The operation symbol (e.g. '**', 'sqrt', 'log')
            func (callable): The function to perform the operation
        """
        self.operations[symbol] = func

    def calculate(self, num1, symbol, num2):
        """
        Perform a calculation using the given numbers and operation symbol.

        Args:
            num1: The first number
            symbol (str): The operation symbol
            num2: The second number (may be ignored for unary operations)

        Returns:
            The result of the calculation

        Raises:
            ValueError: If inputs are not numbers or symbol is invalid
            ZeroDivisionError: If dividing by zero
            Exception: For any other math errors
        """
        # Validate that inputs are numbers
        if not isinstance(num1, (int, float)):
            print(f"Error: '{num1}' is not a valid number.")
            raise ValueError(f"Invalid input: '{num1}' is not a number.")

        if not isinstance(num2, (int, float)):
            print(f"Error: '{num2}' is not a valid number.")
            raise ValueError(f"Invalid input: '{num2}' is not a number.")

        # Validate that the operation symbol exists
        if symbol not in self.operations:
            valid = ', '.join(self.operations.keys())
            print(f"Error: '{symbol}' is not a supported operation.")
            print(f"Supported operations: {valid}")
            raise ValueError(f"Invalid operation symbol: '{symbol}'")

        # Perform the calculation with error handling
        try:
            result = self.operations[symbol](num1, num2)
            return result
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            raise
        except ValueError as e:
            print(f"Math error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error during calculation: {e}")
            raise


# Advanced operation functions

def exponentiation(base, exponent):
    """Raise base to the power of exponent."""
    return math.pow(base, exponent)


def square_root(num, _ignored=None):
    """Return the square root of num (second operand is ignored)."""
    if num < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(num)


def logarithm(num, base=math.e):
    """
    Return the logarithm of num.
    If a second argument is provided it is used as the base;
    otherwise the natural log is returned.
    """
    if num <= 0:
        raise ValueError("Logarithm is undefined for non-positive numbers.")
    if base == math.e:
        return math.log(num)
    return math.log(num, base)


# Helper: safely parse user input to a number

def parse_number(text):
    """
    Convert a string to int or float.
    Returns the number, or None if conversion fails.
    """
    try:
        value = float(text)
        # Return int when the value is a whole number (cleaner display)
        return int(value) if value.is_integer() else value
    except ValueError:
        return None


# Main program 

def main():
    # Create calculator instance (basic ops are registered automatically)
    calc = Calculator()

    # Register advanced operations
    calc.add_operation('**',   exponentiation)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log',  logarithm)

    print("=" * 50)
    print("       Welcome to the Advanced Calculator")
    print("=" * 50)
    print("Available operations:", ', '.join(calc.operations.keys()))
    print("  • For 'sqrt': enter any number as the second value (it is ignored).")
    print("  • For 'log' : enter the desired base as the second value,")
    print("                or 0 to use the natural log (base e).")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        # Get first number
        raw1 = input("Enter the first number: ").strip()
        if raw1.lower() == 'exit':
            print("Goodbye!")
            break

        num1 = parse_number(raw1)
        if not isinstance(num1, (int, float)):
            print(f"  ✗ '{raw1}' is not a valid number. Please try again.\n")
            continue

        # Get operation symbol
        symbol = input("Enter the operation symbol: ").strip()
        if symbol.lower() == 'exit':
            print("Goodbye!")
            break

        # Get second number
        raw2 = input("Enter the second number: ").strip()
        if raw2.lower() == 'exit':
            print("Goodbye!")
            break

        # For natural log, allow 0 as a sentinel meaning "use base e"
        if symbol == 'log' and raw2 == '0':
            num2 = math.e
        else:
            num2 = parse_number(raw2)
            if not isinstance(num2, (int, float)):
                print(f"  ✗ '{raw2}' is not a valid number. Please try again.\n")
                continue

        # Perform calculation
        try:
            result = calc.calculate(num1, symbol, num2)
            # Round to avoid floating-point noise in display
            display = round(result, 10)
            print(f"  ✓ Result: {num1} {symbol} {raw2} = {display}\n")
        except Exception:
            # Error message already printed inside calculate()
            print("  Please try again.\n")


if __name__ == "__main__":
    main()
