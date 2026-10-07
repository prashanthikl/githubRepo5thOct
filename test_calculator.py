import pytest
from calculator import (
    validate_number,
    validate_operation,
    add,
    subtract,
    multiply,
    divide,
    get_operation_function
)


# ==================== PYTEST MARKERS ====================
# Register custom markers to avoid warnings
def pytest_configure(config):
    """Register custom pytest markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test for individual functions"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test combining multiple functions"
    )
    config.addinivalue_line(
        "markers", "edge_case: mark test as testing edge cases and boundary values"
    )
    config.addinivalue_line(
        "markers", "parametrized: mark test as using parametrization for multiple inputs"
    )


class TestValidateNumber:
    """Test cases for validate_number function."""

    @pytest.mark.unit
    def test_validate_integer_string(self):
        """Test validation of integer strings."""
        assert validate_number("42") == 42.0

    @pytest.mark.unit
    def test_validate_float_string(self):
        """Test validation of float strings."""
        assert validate_number("3.14") == 3.14

    @pytest.mark.unit
    def test_validate_negative_number(self):
        """Test validation of negative numbers."""
        assert validate_number("-10") == -10.0

    @pytest.mark.unit
    def test_validate_negative_float(self):
        """Test validation of negative floats."""
        assert validate_number("-3.14") == -3.14

    @pytest.mark.unit
    def test_validate_zero(self):
        """Test validation of zero."""
        assert validate_number("0") == 0.0

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_scientific_notation(self):
        """Test validation of scientific notation."""
        assert validate_number("1e5") == 100000.0

    @pytest.mark.unit
    def test_validate_invalid_string(self):
        """Test validation of non-numeric strings."""
        assert validate_number("abc") is None

    @pytest.mark.unit
    def test_validate_empty_string(self):
        """Test validation of empty string."""
        assert validate_number("") is None

    @pytest.mark.unit
    def test_validate_special_characters(self):
        """Test validation of special characters."""
        assert validate_number("!@#$") is None

    @pytest.mark.unit
    def test_validate_mixed_alphanumeric(self):
        """Test validation of mixed alphanumeric strings."""
        assert validate_number("123abc") is None

    @pytest.mark.unit
    def test_validate_space_in_string(self):
        """Test validation of strings with spaces."""
        assert validate_number("12 34") is None

    @pytest.mark.unit
    def test_validate_multiple_decimals(self):
        """Test validation of strings with multiple decimal points."""
        assert validate_number("3.14.15") is None

    @pytest.mark.unit
    @pytest.mark.parametrized
    @pytest.mark.edge_case
    @pytest.mark.parametrize("input_str,expected", [
        ("1e-10", 1e-10),  # Very small scientific notation
        ("1e10", 1e10),    # Very large scientific notation
        ("-1e5", -100000.0),  # Negative scientific notation
        ("0.0", 0.0),      # Float zero
        ("-0", 0.0),       # Negative zero
        ("999999999999.999", 999999999999.999),  # Very large float
        ("0.000000001", 1e-9),  # Very small float
        ("+42", 42.0),     # Leading plus sign
    ])
    def test_validate_number_parametrized_edge_cases(self, input_str, expected):
        """Parametrized test for edge case number validations.

        Tests boundary values, scientific notation, and special float formats.
        Uses parametrize decorator to test multiple inputs efficiently.
        """
        result = validate_number(input_str)
        if expected is not None:
            assert abs(result - expected) < 1e-10 if result else result == expected
        else:
            assert result is None


class TestValidateOperation:
    """Test cases for validate_operation function."""

    @pytest.mark.unit
    def test_validate_addition_operator(self):
        """Test validation of addition operator."""
        assert validate_operation("+") is True

    @pytest.mark.unit
    def test_validate_subtraction_operator(self):
        """Test validation of subtraction operator."""
        assert validate_operation("-") is True

    @pytest.mark.unit
    def test_validate_multiplication_operator(self):
        """Test validation of multiplication operator."""
        assert validate_operation("*") is True

    @pytest.mark.unit
    def test_validate_division_operator(self):
        """Test validation of division operator."""
        assert validate_operation("/") is True

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_invalid_operator(self):
        """Test validation of invalid operator."""
        assert validate_operation("^") is False

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_empty_string_operator(self):
        """Test validation of empty string as operator."""
        assert validate_operation("") is False

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_word_operator(self):
        """Test validation of word as operator."""
        assert validate_operation("add") is False

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_multiple_characters(self):
        """Test validation of multiple characters as operator."""
        assert validate_operation("++") is False

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_percent_operator(self):
        """Test validation of percent operator."""
        assert validate_operation("%") is False

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_space_operator(self):
        """Test validation of space as operator."""
        assert validate_operation(" ") is False

    @pytest.mark.unit
    @pytest.mark.parametrized
    @pytest.mark.edge_case
    @pytest.mark.parametrize("operation,expected", [
        ("+", True),
        ("-", True),
        ("*", True),
        ("/", True),
        ("^", False),
        ("%", False),
        ("//", False),
        ("**", False),
        ("mod", False),
        ("", False),
        (" ", False),
        ("1", False),
        ("(", False),
        (")", False),
        ("&", False),
        ("|", False),
    ])
    def test_validate_operation_parametrized(self, operation, expected):
        """Parametrized test for operation validation with various inputs.

        Tests all supported operations and various invalid operators including
        mathematical symbols, double operators, and special characters.
        """
        assert validate_operation(operation) is expected


class TestAddition:
    """Test cases for add function."""

    @pytest.mark.unit
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5

    @pytest.mark.unit
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        assert add(-2, -3) == -5

    @pytest.mark.unit
    def test_add_positive_and_negative(self):
        """Test addition of positive and negative numbers."""
        assert add(5, -3) == 2

    @pytest.mark.unit
    def test_add_zero(self):
        """Test addition with zero."""
        assert add(5, 0) == 5

    @pytest.mark.unit
    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_add_large_numbers(self):
        """Test addition of large numbers."""
        assert add(1000000, 2000000) == 3000000

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_add_very_small_numbers(self):
        """Test addition of very small numbers."""
        result = add(0.0001, 0.0002)
        assert abs(result - 0.0003) < 1e-10

    @pytest.mark.unit
    @pytest.mark.parametrized
    @pytest.mark.edge_case
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),                              # Zero + Zero
        (1, 0, 1),                              # Identity element
        (0, 1, 1),                              # Identity element (reverse)
        (1e308, 1e-308, 1e308),                 # Very large and very small
        (-1, 1, 0),                             # Additive inverse
        (0.1, 0.2, 0.3),                        # Floating-point precision test
        (999999999, 999999999, 1999999998),     # Large integers
        (-999999999, -999999999, -1999999998),  # Large negative integers
        (1.5, 2.5, 4.0),                        # Float addition
        (-0.5, 0.5, 0.0),                       # Negative and positive float
    ])
    def test_add_parametrized_comprehensive(self, a, b, expected):
        """Parametrized test for addition with various edge cases.

        Tests boundary values including zero, identity elements, very large/small
        numbers, floating-point precision edge cases, and inverses.
        """
        result = add(a, b)
        # For floating-point comparisons, use approximate equality
        if abs(expected) < 1e-10:
            assert abs(result) < 1e-9
        else:
            assert abs(result - expected) < max(1e-9, abs(expected) * 1e-9)


class TestSubtraction:
    """Test cases for subtract function."""

    @pytest.mark.unit
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2

    @pytest.mark.unit
    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        assert subtract(-5, -3) == -2

    @pytest.mark.unit
    def test_subtract_negative_from_positive(self):
        """Test subtraction of negative from positive."""
        assert subtract(5, -3) == 8

    @pytest.mark.unit
    def test_subtract_positive_from_negative(self):
        """Test subtraction of positive from negative."""
        assert subtract(-5, 3) == -8

    @pytest.mark.unit
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5

    @pytest.mark.unit
    def test_subtract_same_numbers(self):
        """Test subtraction of same numbers."""
        assert subtract(5, 5) == 0

    @pytest.mark.unit
    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0

    @pytest.mark.unit
    @pytest.mark.parametrized
    @pytest.mark.edge_case
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),                      # Zero - Zero
        (1, 0, 1),                      # Subtract zero
        (0, 1, -1),                     # Zero minus positive
        (1, 1, 0),                      # Same numbers
        (-1, -1, 0),                    # Same negative numbers
        (1e308, 1, 1e308 - 1),          # Very large number
        (-1e308, 1, -1e308 - 1),        # Very negative number
        (1.5, 2.5, -1.0),               # Negative result
        (-0.5, -0.5, 0),                # Negative floats
        (100, -100, 200),               # Subtracting negative (addition effect)
    ])
    def test_subtract_parametrized_comprehensive(self, a, b, expected):
        """Parametrized test for subtraction with various edge cases.

        Tests boundary values including zero, identity properties, very large/small
        numbers, negative results, and double negatives.
        """
        result = subtract(a, b)
        # For floating-point comparisons, use approximate equality
        if abs(expected) < 1e-10:
            assert abs(result) < 1e-10
        else:
            assert abs(result - expected) < 1e-9


class TestMultiplication:
    """Test cases for multiply function."""

    @pytest.mark.unit
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(3, 4) == 12

    @pytest.mark.unit
    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert multiply(-3, -4) == 12

    @pytest.mark.unit
    def test_multiply_positive_and_negative(self):
        """Test multiplication of positive and negative numbers."""
        assert multiply(3, -4) == -12

    @pytest.mark.unit
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0

    @pytest.mark.unit
    def test_multiply_by_one(self):
        """Test multiplication by one."""
        assert multiply(5, 1) == 5

    @pytest.mark.unit
    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 4.0) == 10.0

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_multiply_large_numbers(self):
        """Test multiplication of large numbers."""
        assert multiply(1000, 2000) == 2000000

    @pytest.mark.unit
    def test_multiply_negative_by_one(self):
        """Test multiplication of negative by one."""
        assert multiply(-5, 1) == -5

    @pytest.mark.unit
    @pytest.mark.parametrized
    @pytest.mark.edge_case
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),                      # Zero × Zero
        (1, 1, 1),                      # Identity
        (1, 0, 0),                      # Multiply by zero
        (0, 1, 0),                      # Zero times positive
        (-1, 1, -1),                    # Negative identity
        (-1, -1, 1),                    # Two negatives make positive
        (2, 3, 6),                      # Simple positive
        (-2, -3, 6),                    # Two negatives
        (-2, 3, -6),                    # Mixed signs
        (0.5, 0.5, 0.25),               # Float multiplication
        (1e-5, 1e5, 1.0),               # Scientific notation
        (10, 10, 100),                  # Perfect square
        (-10, -10, 100),                # Negative perfect square
        (1e308, 0, 0),                  # Very large times zero
    ])
    def test_multiply_parametrized_comprehensive(self, a, b, expected):
        """Parametrized test for multiplication with various edge cases.

        Tests boundary values including zero, identity elements, sign behavior,
        floating-point multiplication, and very large/small numbers.
        """
        result = multiply(a, b)
        # For floating-point comparisons, use approximate equality
        if abs(expected) < 1e-10:
            assert abs(result) < 1e-10
        else:
            assert abs(result - expected) < max(1e-9, abs(expected) * 1e-9)


class TestDivision:
    """Test cases for divide function."""

    @pytest.mark.unit
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5.0

    @pytest.mark.unit
    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        assert divide(-10, -2) == 5.0

    @pytest.mark.unit
    def test_divide_positive_by_negative(self):
        """Test division of positive by negative."""
        assert divide(10, -2) == -5.0

    @pytest.mark.unit
    def test_divide_negative_by_positive(self):
        """Test division of negative by positive."""
        assert divide(-10, 2) == -5.0

    @pytest.mark.unit
    def test_divide_by_one(self):
        """Test division by one."""
        assert divide(5, 1) == 5.0

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_divide_by_zero_returns_none(self):
        """Test division by zero returns None."""
        assert divide(10, 0) is None

    @pytest.mark.unit
    def test_divide_zero_by_number(self):
        """Test division of zero by number."""
        assert divide(0, 5) == 0.0

    @pytest.mark.unit
    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(7.5, 2.5) == 3.0

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_divide_results_in_float(self):
        """Test that division results in float."""
        result = divide(5, 2)
        assert result == 2.5
        assert isinstance(result, float)

    @pytest.mark.unit
    @pytest.mark.parametrized
    @pytest.mark.edge_case
    @pytest.mark.parametrize("a,b,expected", [
        (0, 1, 0.0),                    # Zero division (valid)
        (0, -1, 0.0),                   # Zero divided by negative
        (1, 1, 1.0),                    # Identity
        (1, -1, -1.0),                  # Positive by negative one
        (-1, -1, 1.0),                  # Two negatives
        (10, 2, 5.0),                   # Simple division
        (10, 4, 2.5),                   # Non-integer result
        (1, 3, 1/3),                    # Repeating decimal
        (1, 2, 0.5),                    # Half
        (1e-10, 1e-10, 1.0),            # Very small numbers
        (1e10, 1e5, 1e5),               # Very large numbers
        (0.1, 0.1, 1.0),                # Float identity
        (-10, 2, -5.0),                 # Negative dividend
        (10, -2, -5.0),                 # Negative divisor
    ])
    def test_divide_parametrized_comprehensive(self, a, b, expected):
        """Parametrized test for division with various edge cases.

        Tests boundary values, zero division (valid), identity elements, sign behavior,
        non-integer results, repeating decimals, and very large/small numbers.
        """
        if b == 0:
            assert divide(a, b) is None
        else:
            result = divide(a, b)
            assert abs(result - expected) < max(1e-9, abs(expected) * 1e-9)

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_divide_by_very_small_nonzero_number(self):
        """Test division by very small but non-zero divisor.

        This tests the edge case where divisor approaches zero but is not zero.
        Should return a very large number, not None.
        """
        result = divide(1, 1e-308)
        assert result is not None
        assert result > 1e307


class TestGetOperationFunction:
    """Test cases for get_operation_function function."""

    @pytest.mark.unit
    def test_get_add_function(self):
        """Test retrieving addition function."""
        func = get_operation_function("+")
        assert func is not None
        assert func(2, 3) == 5

    @pytest.mark.unit
    def test_get_subtract_function(self):
        """Test retrieving subtraction function."""
        func = get_operation_function("-")
        assert func is not None
        assert func(5, 3) == 2

    @pytest.mark.unit
    def test_get_multiply_function(self):
        """Test retrieving multiplication function."""
        func = get_operation_function("*")
        assert func is not None
        assert func(3, 4) == 12

    @pytest.mark.unit
    def test_get_divide_function(self):
        """Test retrieving division function."""
        func = get_operation_function("/")
        assert func is not None
        assert func(10, 2) == 5.0

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_get_invalid_operation_returns_none(self):
        """Test retrieving invalid operation returns None."""
        func = get_operation_function("^")
        assert func is None

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_get_operation_from_empty_string(self):
        """Test retrieving operation from empty string."""
        func = get_operation_function("")
        assert func is None

    @pytest.mark.unit
    @pytest.mark.parametrized
    @pytest.mark.edge_case
    @pytest.mark.parametrize("operation,should_exist", [
        ("+", True),
        ("-", True),
        ("*", True),
        ("/", True),
        ("^", False),
        ("%", False),
        ("mod", False),
        ("add", False),
        ("", False),
        ("++", False),
    ])
    def test_get_operation_function_parametrized(self, operation, should_exist):
        """Parametrized test for operation function retrieval.

        Tests that valid operations return callable functions and invalid
        operations return None.
        """
        func = get_operation_function(operation)
        if should_exist:
            assert func is not None
            assert callable(func)
        else:
            assert func is None


class TestErrorHandling:
    """Test cases for error handling scenarios."""

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_division_by_zero_error(self):
        """Test handling of division by zero."""
        result = divide(5, 0)
        assert result is None

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_divide_function_with_very_small_divisor(self):
        """Test division with very small but non-zero divisor."""
        result = divide(1, 1e-10)
        assert result is not None
        assert abs(result - 1e10) < 1

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_validate_number_with_none_input(self):
        """Test validate_number doesn't crash with edge cases."""
        # Test with valid numeric strings that might be edge cases
        assert validate_number("0.0") == 0.0
        assert validate_number("-0") == 0.0

    @pytest.mark.integration
    def test_multiple_operations_consistency(self):
        """Test that operations maintain consistency across multiple calls.

        Tests mathematical properties:
        - a + b - b should equal a
        - (a * b) / b should equal a
        """
        # a + b - b should equal a
        a, b = 10, 3
        result = subtract(add(a, b), b)
        assert result == a

        # (a * b) / b should equal a (when b != 0)
        result = divide(multiply(a, b), b)
        assert result == float(a)

    @pytest.mark.unit
    @pytest.mark.edge_case
    @pytest.mark.parametrized
    @pytest.mark.parametrize("numerator,denominator", [
        (10, 0),
        (0, 0),
        (1, 0),
        (-5, 0),
        (1e100, 0),
    ])
    def test_division_by_zero_parametrized(self, numerator, denominator):
        """Parametrized test for division by zero with various numerators.

        Ensures all division by zero cases return None, regardless of numerator.
        """
        assert divide(numerator, denominator) is None


class TestIntegration:
    """Integration tests combining multiple functions."""

    @pytest.mark.integration
    def test_full_calculation_addition(self):
        """Test full calculation flow with addition.

        Validates the complete workflow: input validation, operation validation,
        and function execution with addition operator.
        """
        first = validate_number("5")
        second = validate_number("3")
        operation = "+"

        assert first is not None
        assert second is not None
        assert validate_operation(operation) is True

        func = get_operation_function(operation)
        result = func(first, second)
        assert result == 8.0

    @pytest.mark.integration
    def test_full_calculation_division(self):
        """Test full calculation flow with division.

        Validates the complete workflow with division operator.
        """
        first = validate_number("10")
        second = validate_number("2")
        operation = "/"

        assert first is not None
        assert second is not None
        assert validate_operation(operation) is True

        func = get_operation_function(operation)
        result = func(first, second)
        assert result == 5.0

    @pytest.mark.integration
    @pytest.mark.edge_case
    def test_full_calculation_division_by_zero(self):
        """Test full calculation flow with division by zero.

        Validates error handling in the complete workflow.
        """
        first = validate_number("10")
        second = validate_number("0")
        operation = "/"

        assert first is not None
        assert second is not None
        assert validate_operation(operation) is True

        func = get_operation_function(operation)
        result = func(first, second)
        assert result is None

    @pytest.mark.integration
    def test_invalid_input_handling(self):
        """Test handling of invalid inputs in workflow.

        Validates that invalid number and operation strings are properly rejected.
        """
        first = validate_number("abc")
        operation = validate_operation("^")

        assert first is None
        assert operation is False

    @pytest.mark.integration
    def test_chained_calculations(self):
        """Test performing multiple calculations in sequence.

        Tests operation chaining (using output as input for next calculation):
        - (5 + 3) * 2 = 16
        - (20 - 5) / 3 = 5
        """
        # Calculate (5 + 3) * 2
        add_result = add(5, 3)  # 8
        multiply_result = multiply(add_result, 2)  # 16
        assert multiply_result == 16

        # Calculate (20 - 5) / 3
        subtract_result = subtract(20, 5)  # 15
        divide_result = divide(subtract_result, 3)  # 5
        assert divide_result == 5.0

    @pytest.mark.integration
    def test_all_operations_with_same_inputs(self):
        """Test all operations with the same input values.

        Tests consistency across all four operations with identical inputs.
        """
        a, b = 10, 2

        add_result = add(a, b)
        subtract_result = subtract(a, b)
        multiply_result = multiply(a, b)
        divide_result = divide(a, b)

        assert add_result == 12
        assert subtract_result == 8
        assert multiply_result == 20
        assert divide_result == 5.0

    @pytest.mark.integration
    @pytest.mark.parametrized
    @pytest.mark.parametrize("operation_symbol,func_to_call,a,b,expected", [
        ("+", add, 5, 3, 8),
        ("-", subtract, 10, 3, 7),
        ("*", multiply, 4, 5, 20),
        ("/", divide, 20, 4, 5.0),
        ("+", add, -5, 5, 0),
        ("-", subtract, 0, 5, -5),
        ("*", multiply, 0, 100, 0),
    ])
    def test_all_operations_parametrized(self, operation_symbol, func_to_call, a, b, expected):
        """Parametrized integration test for all operations.

        Tests complete workflow with various operations and input combinations.
        Uses parametrize to test all four operations systematically.
        """
        # Validate inputs and operation
        first = validate_number(str(a))
        second = validate_number(str(b))
        assert validate_operation(operation_symbol) is True

        # Get and execute function
        func = get_operation_function(operation_symbol)
        assert func == func_to_call

        result = func(first, second)
        if isinstance(expected, float):
            assert abs(result - expected) < 1e-9
        else:
            assert result == expected
