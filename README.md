# Simple Python Console Calculator

A beginner-friendly Python console calculator application that performs basic arithmetic operations with comprehensive error handling.

## Features

- **Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Input Validation**: Validates numeric input and operation selection
- **Error Handling**:
  - Handles non-numeric input with user-friendly error messages
  - Prevents division by zero
  - Rejects unsupported operations
- **Beginner-Friendly Code**: Well-organized functions and clear variable names
- **Interactive Interface**: Step-by-step prompts for user input

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone https://github.com/prashanthikl/githubRepo5thOct.git
cd githubRepo5thOct
```

2. No additional dependencies required!

## Usage

Run the calculator:
```bash
python3 calculator.py
```

Then follow the prompts:
1. Enter the first number
2. Enter the second number
3. Choose an operation: `+`, `-`, `*`, or `/`
4. View the result

## Examples

### Addition
```
=== Simple Console Calculator ===

Enter the first number: 5
Enter the second number: 3
Enter an operation (+, -, *, /): +

Result: 5.0 + 3.0 = 8.0
```

### Division
```
=== Simple Console Calculator ===

Enter the first number: 20
Enter the second number: 4
Enter an operation (+, -, *, /): /

Result: 20.0 / 4.0 = 5.0
```

### Multiplication
```
=== Simple Console Calculator ===

Enter the first number: 7
Enter the second number: 6
Enter an operation (+, -, *, /): *

Result: 7.0 * 6.0 = 42.0
```

### Subtraction
```
=== Simple Console Calculator ===

Enter the first number: 10
Enter the second number: 3
Enter an operation (+, -, *, /): -

Result: 10.0 - 3.0 = 7.0
```

## Error Handling Examples

### Invalid Number Input
```
Enter the first number: abc
Invalid input! Please enter a valid number.

Enter the first number: 10
```

### Unsupported Operation
```
Enter an operation (+, -, *, /): %
Invalid operation! Please choose from: +, -, *, /

Enter an operation (+, -, *, /): +
```

### Division by Zero
```
Enter the first number: 10
Enter the second number: 0
Enter an operation (+, -, *, /): /

Error: Division by zero is not allowed!
```

## Code Structure

The calculator is organized with separate functions for each operation and validation:

- `validate_number(value)` - Validates and converts input to float
- `validate_operation(operation)` - Checks if operation is supported
- `add(a, b)` - Addition function
- `subtract(a, b)` - Subtraction function
- `multiply(a, b)` - Multiplication function
- `divide(a, b)` - Division function with zero check
- `get_operation_function(operation)` - Maps operation to function
- `calculator()` - Main calculator loop

## License

Open source project

## Author

Created as part of GitHub learning exercises
