# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python console calculator application designed for beginners. It's a single-file educational project that demonstrates input validation, error handling, and functional decomposition.

## Running the Application

```bash
python3 calculator.py
```

The calculator prompts the user for two numbers and an operation (+, -, *, /), then displays the result.

## Testing the Application

Test with standard input piping:
```bash
echo -e "5\n3\n+" | python3 calculator.py
```

Test error scenarios:
```bash
# Invalid number input
echo -e "abc\n5\n5\n+" | python3 calculator.py

# Division by zero
echo -e "10\n0\n/" | python3 calculator.py

# Invalid operation
echo -e "10\n5\n%\n+" | python3 calculator.py
```

## Code Architecture

The calculator.py file is organized into functional layers:

1. **Input Validation Functions**
   - `validate_number(value)` - Converts and validates numeric input
   - `validate_operation(operation)` - Checks if operation is in the supported set (+, -, *, /)

2. **Operation Functions**
   - Individual functions for each operation: `add()`, `subtract()`, `multiply()`, `divide()`
   - `divide()` includes zero-check logic (returns None if dividing by zero)

3. **Operation Dispatch**
   - `get_operation_function(operation)` - Maps operation symbols to their corresponding functions via dictionary lookup

4. **Main Loop**
   - `calculator()` - Entry point that orchestrates user prompts, validation loops, and result display
   - Uses `if __name__ == "__main__"` guard for direct execution

## Key Design Decisions

- **Single File**: Entire application in one file for beginner accessibility
- **Separation of Concerns**: Input validation, operations, and main logic are separate functions
- **Error Recovery**: Invalid input triggers a retry loop rather than exiting
- **Division by Zero Handling**: Returns None from divide() and displays an error message (doesn't crash)
- **Float Arithmetic**: All numbers are converted to float for consistent decimal handling

## Future Enhancements

Potential areas for expansion if issues are created:
- Command-line argument support for non-interactive operation
- History of calculations
- Additional operations (power, modulo, etc.)
- Unit tests using pytest or unittest
- Batch mode for multiple calculations

## Development Notes

- No external dependencies required - uses only Python standard library
- Python 3.x required (f-strings are used in some contexts)
- The application is intentionally simple - modifications should maintain beginner-friendly readability
