def validate_number(value):
    """Validate and convert input to a float."""
    try:
        return float(value)
    except ValueError:
        return None


def validate_operation(operation):
    """Validate if the operation is supported."""
    supported_operations = ['+', '-', '*', '/']
    return operation in supported_operations


def add(a, b):
    """Perform addition."""
    return a + b


def subtract(a, b):
    """Perform subtraction."""
    return a - b


def multiply(a, b):
    """Perform multiplication."""
    return a * b


def divide(a, b):
    """Perform division with zero check."""
    if b == 0:
        return None
    return a / b


def get_operation_function(operation):
    """Map operation to corresponding function."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return operations.get(operation)


def calculator():
    """Main calculator function."""
    print("=== Simple Console Calculator ===\n")

    # Get first number
    while True:
        first_num_input = input("Enter the first number: ")
        first_num = validate_number(first_num_input)
        if first_num is not None:
            break
        print("Invalid input! Please enter a valid number.\n")

    # Get second number
    while True:
        second_num_input = input("Enter the second number: ")
        second_num = validate_number(second_num_input)
        if second_num is not None:
            break
        print("Invalid input! Please enter a valid number.\n")

    # Get operation
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if validate_operation(operation):
            break
        print("Invalid operation! Please choose from: +, -, *, /\n")

    # Perform calculation
    operation_func = get_operation_function(operation)
    result = operation_func(first_num, second_num)

    # Handle division by zero
    if result is None:
        print("\nError: Division by zero is not allowed!")
    else:
        print(f"\nResult: {first_num} {operation} {second_num} = {result}")


if __name__ == "__main__":
    calculator()
