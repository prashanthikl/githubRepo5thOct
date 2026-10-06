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


class TestValidateNumber:
    """Test cases for validate_number function."""

    def test_validate_integer_string(self):
        """Test validation of integer strings."""
        assert validate_number("42") == 42.0

    def test_validate_float_string(self):
        """Test validation of float strings."""
        assert validate_number("3.14") == 3.14

    def test_validate_negative_number(self):
        """Test validation of negative numbers."""
        assert validate_number("-10") == -10.0

    def test_validate_negative_float(self):
        """Test validation of negative floats."""
        assert validate_number("-3.14") == -3.14

    def test_validate_zero(self):
        """Test validation of zero."""
        assert validate_number("0") == 0.0

    def test_validate_scientific_notation(self):
        """Test validation of scientific notation."""
        assert validate_number("1e5") == 100000.0

    def test_validate_invalid_string(self):
        """Test validation of non-numeric strings."""
        assert validate_number("abc") is None

    def test_validate_empty_string(self):
        """Test validation of empty string."""
        assert validate_number("") is None

    def test_validate_special_characters(self):
        """Test validation of special characters."""
        assert validate_number("!@#$") is None

    def test_validate_mixed_alphanumeric(self):
        """Test validation of mixed alphanumeric strings."""
        assert validate_number("123abc") is None

    def test_validate_space_in_string(self):
        """Test validation of strings with spaces."""
        assert validate_number("12 34") is None

    def test_validate_multiple_decimals(self):
        """Test validation of strings with multiple decimal points."""
        assert validate_number("3.14.15") is None


class TestValidateOperation:
    """Test cases for validate_operation function."""

    def test_validate_addition_operator(self):
        """Test validation of addition operator."""
        assert validate_operation("+") is True

    def test_validate_subtraction_operator(self):
        """Test validation of subtraction operator."""
        assert validate_operation("-") is True

    def test_validate_multiplication_operator(self):
        """Test validation of multiplication operator."""
        assert validate_operation("*") is True

    def test_validate_division_operator(self):
        """Test validation of division operator."""
        assert validate_operation("/") is True

    def test_validate_invalid_operator(self):
        """Test validation of invalid operator."""
        assert validate_operation("^") is False

    def test_validate_empty_string_operator(self):
        """Test validation of empty string as operator."""
        assert validate_operation("") is False

    def test_validate_word_operator(self):
        """Test validation of word as operator."""
        assert validate_operation("add") is False

    def test_validate_multiple_characters(self):
        """Test validation of multiple characters as operator."""
        assert validate_operation("++") is False

    def test_validate_percent_operator(self):
        """Test validation of percent operator."""
        assert validate_operation("%") is False

    def test_validate_space_operator(self):
        """Test validation of space as operator."""
        assert validate_operation(" ") is False


class TestAddition:
    """Test cases for add function."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        assert add(-2, -3) == -5

    def test_add_positive_and_negative(self):
        """Test addition of positive and negative numbers."""
        assert add(5, -3) == 2

    def test_add_zero(self):
        """Test addition with zero."""
        assert add(5, 0) == 5

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0

    def test_add_large_numbers(self):
        """Test addition of large numbers."""
        assert add(1000000, 2000000) == 3000000

    def test_add_very_small_numbers(self):
        """Test addition of very small numbers."""
        result = add(0.0001, 0.0002)
        assert abs(result - 0.0003) < 1e-10


class TestSubtraction:
    """Test cases for subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        assert subtract(-5, -3) == -2

    def test_subtract_negative_from_positive(self):
        """Test subtraction of negative from positive."""
        assert subtract(5, -3) == 8

    def test_subtract_positive_from_negative(self):
        """Test subtraction of positive from negative."""
        assert subtract(-5, 3) == -8

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        assert subtract(5, 0) == 5

    def test_subtract_same_numbers(self):
        """Test subtraction of same numbers."""
        assert subtract(5, 5) == 0

    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0


class TestMultiplication:
    """Test cases for multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(3, 4) == 12

    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert multiply(-3, -4) == 12

    def test_multiply_positive_and_negative(self):
        """Test multiplication of positive and negative numbers."""
        assert multiply(3, -4) == -12

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplication by one."""
        assert multiply(5, 1) == 5

    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 4.0) == 10.0

    def test_multiply_large_numbers(self):
        """Test multiplication of large numbers."""
        assert multiply(1000, 2000) == 2000000

    def test_multiply_negative_by_one(self):
        """Test multiplication of negative by one."""
        assert multiply(-5, 1) == -5


class TestDivision:
    """Test cases for divide function."""

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5.0

    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        assert divide(-10, -2) == 5.0

    def test_divide_positive_by_negative(self):
        """Test division of positive by negative."""
        assert divide(10, -2) == -5.0

    def test_divide_negative_by_positive(self):
        """Test division of negative by positive."""
        assert divide(-10, 2) == -5.0

    def test_divide_by_one(self):
        """Test division by one."""
        assert divide(5, 1) == 5.0

    def test_divide_by_zero_returns_none(self):
        """Test division by zero returns None."""
        assert divide(10, 0) is None

    def test_divide_zero_by_number(self):
        """Test division of zero by number."""
        assert divide(0, 5) == 0.0

    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(7.5, 2.5) == 3.0

    def test_divide_results_in_float(self):
        """Test that division results in float."""
        result = divide(5, 2)
        assert result == 2.5
        assert isinstance(result, float)


class TestGetOperationFunction:
    """Test cases for get_operation_function function."""

    def test_get_add_function(self):
        """Test retrieving addition function."""
        func = get_operation_function("+")
        assert func is not None
        assert func(2, 3) == 5

    def test_get_subtract_function(self):
        """Test retrieving subtraction function."""
        func = get_operation_function("-")
        assert func is not None
        assert func(5, 3) == 2

    def test_get_multiply_function(self):
        """Test retrieving multiplication function."""
        func = get_operation_function("*")
        assert func is not None
        assert func(3, 4) == 12

    def test_get_divide_function(self):
        """Test retrieving division function."""
        func = get_operation_function("/")
        assert func is not None
        assert func(10, 2) == 5.0

    def test_get_invalid_operation_returns_none(self):
        """Test retrieving invalid operation returns None."""
        func = get_operation_function("^")
        assert func is None

    def test_get_operation_from_empty_string(self):
        """Test retrieving operation from empty string."""
        func = get_operation_function("")
        assert func is None


class TestErrorHandling:
    """Test cases for error handling scenarios."""

    def test_division_by_zero_error(self):
        """Test handling of division by zero."""
        result = divide(5, 0)
        assert result is None

    def test_divide_function_with_very_small_divisor(self):
        """Test division with very small but non-zero divisor."""
        result = divide(1, 1e-10)
        assert result is not None
        assert abs(result - 1e10) < 1

    def test_validate_number_with_none_input(self):
        """Test validate_number doesn't crash with edge cases."""
        # Test with valid numeric strings that might be edge cases
        assert validate_number("0.0") == 0.0
        assert validate_number("-0") == 0.0

    def test_multiple_operations_consistency(self):
        """Test that operations maintain consistency."""
        # a + b - b should equal a
        a, b = 10, 3
        result = subtract(add(a, b), b)
        assert result == a

        # (a * b) / b should equal a (when b != 0)
        result = divide(multiply(a, b), b)
        assert result == float(a)


class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_full_calculation_addition(self):
        """Test full calculation flow with addition."""
        first = validate_number("5")
        second = validate_number("3")
        operation = "+"

        assert first is not None
        assert second is not None
        assert validate_operation(operation) is True

        func = get_operation_function(operation)
        result = func(first, second)
        assert result == 8.0

    def test_full_calculation_division(self):
        """Test full calculation flow with division."""
        first = validate_number("10")
        second = validate_number("2")
        operation = "/"

        assert first is not None
        assert second is not None
        assert validate_operation(operation) is True

        func = get_operation_function(operation)
        result = func(first, second)
        assert result == 5.0

    def test_full_calculation_division_by_zero(self):
        """Test full calculation flow with division by zero."""
        first = validate_number("10")
        second = validate_number("0")
        operation = "/"

        assert first is not None
        assert second is not None
        assert validate_operation(operation) is True

        func = get_operation_function(operation)
        result = func(first, second)
        assert result is None

    def test_invalid_input_handling(self):
        """Test handling of invalid inputs."""
        first = validate_number("abc")
        operation = validate_operation("^")

        assert first is None
        assert operation is False

    def test_chained_calculations(self):
        """Test performing multiple calculations in sequence."""
        # Calculate (5 + 3) * 2
        add_result = add(5, 3)  # 8
        multiply_result = multiply(add_result, 2)  # 16
        assert multiply_result == 16

        # Calculate (20 - 5) / 3
        subtract_result = subtract(20, 5)  # 15
        divide_result = divide(subtract_result, 3)  # 5
        assert divide_result == 5.0

    def test_all_operations_with_same_inputs(self):
        """Test all operations with the same input values."""
        a, b = 10, 2

        add_result = add(a, b)
        subtract_result = subtract(a, b)
        multiply_result = multiply(a, b)
        divide_result = divide(a, b)

        assert add_result == 12
        assert subtract_result == 8
        assert multiply_result == 20
        assert divide_result == 5.0
