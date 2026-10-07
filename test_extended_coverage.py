"""Extended test coverage for calculator module.

This module provides comprehensive additional tests for the calculator project,
focusing on edge cases, boundary values, scientific notation, floating-point
precision, and operation chaining scenarios.

Test Organization:
- Performance benchmarking tests
- Advanced edge case tests
- Scientific notation tests
- Floating-point precision edge cases
- Complex operation chaining tests
- Stress tests with extreme values
"""

import pytest
import math
from calculator import (
    validate_number,
    validate_operation,
    add,
    subtract,
    multiply,
    divide,
    get_operation_function
)


# ==================== FIXTURES ====================

@pytest.fixture
def small_numbers():
    """Fixture providing very small numbers for testing."""
    return [1e-100, 1e-50, 1e-10, 1e-5, 0.0001]


@pytest.fixture
def large_numbers():
    """Fixture providing very large numbers for testing."""
    return [1e100, 1e50, 1e10, 1e5, 1000000]


@pytest.fixture
def special_floats():
    """Fixture providing special floating-point values."""
    return [
        0.0,
        -0.0,
        float('inf'),
        float('-inf'),
        float('nan'),
    ]


@pytest.fixture
def scientific_notation_strings():
    """Fixture providing scientific notation number strings."""
    return [
        "1e5",
        "1e-5",
        "1.5e3",
        "-2.5e-2",
        "9.99e100",
        "1.11e-100",
    ]


# ==================== PERFORMANCE BENCHMARKS ====================

class TestPerformanceBenchmarks:
    """Performance benchmarking tests for calculator operations."""

    @pytest.mark.parametrized
    @pytest.mark.edge_case
    def test_benchmark_addition_performance(self, benchmark):
        """Benchmark addition operation performance.

        Measures performance of repeated addition operations to ensure
        calculator maintains consistent performance characteristics.
        """
        def addition_loop():
            result = 0
            for i in range(1000):
                result = add(result, 1)
            return result

        result = benchmark(addition_loop)
        assert result == 1000

    @pytest.mark.parametrized
    @pytest.mark.edge_case
    def test_benchmark_division_performance(self, benchmark):
        """Benchmark division operation performance.

        Measures performance of repeated division operations.
        """
        def division_loop():
            result = 1000
            for i in range(100):
                result = divide(result, 2)
            return result

        result = benchmark(division_loop)
        assert result > 0

    @pytest.mark.parametrized
    @pytest.mark.edge_case
    def test_benchmark_validation_performance(self, benchmark):
        """Benchmark number validation performance.

        Tests performance of validate_number with various inputs.
        """
        test_strings = ["123", "45.67", "-89", "1e5", "abc"]

        def validation_loop():
            results = []
            for _ in range(1000):
                for s in test_strings:
                    results.append(validate_number(s))
            return results

        results = benchmark(validation_loop)
        assert len(results) == 5000


# ==================== SCIENTIFIC NOTATION TESTS ====================

class TestScientificNotation:
    """Test scientific notation handling in number validation and operations."""

    @pytest.mark.unit
    @pytest.mark.edge_case
    @pytest.mark.parametrize("sci_notation,expected", [
        ("1e5", 100000.0),
        ("1e-5", 0.00001),
        ("1.5e3", 1500.0),
        ("-2.5e-2", -0.025),
        ("9.99e2", 999.0),
        ("1e0", 1.0),
        ("5.5e1", 55.0),
        ("-1.2e-3", -0.0012),
    ])
    def test_scientific_notation_validation(self, sci_notation, expected):
        """Test validation of scientific notation strings.

        Ensures validate_number correctly parses scientific notation.
        """
        result = validate_number(sci_notation)
        assert result is not None
        assert abs(result - expected) < max(1e-10, abs(expected) * 1e-10)

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_scientific_notation_arithmetic(self):
        """Test arithmetic with scientifically notated numbers."""
        num1 = validate_number("1e3")  # 1000
        num2 = validate_number("2e2")  # 200

        assert num1 is not None
        assert num2 is not None

        result_add = add(num1, num2)  # 1000 + 200 = 1200
        result_multiply = multiply(num1, num2)  # 1000 * 200 = 200000

        assert result_add == 1200.0
        assert result_multiply == 200000.0


# ==================== FLOATING-POINT PRECISION TESTS ====================

class TestFloatingPointPrecision:
    """Test floating-point precision and rounding edge cases."""

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_floating_point_addition_precision(self):
        """Test floating-point precision in addition.

        The classic 0.1 + 0.2 != 0.3 problem in floating-point arithmetic.
        """
        a = validate_number("0.1")
        b = validate_number("0.2")
        c = validate_number("0.3")

        result = add(a, b)
        # Result should be close to 0.3, but not exactly due to floating-point representation
        assert abs(result - c) < 1e-10

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_floating_point_subtraction_precision(self):
        """Test floating-point precision in subtraction."""
        a = validate_number("1.0")
        b = validate_number("0.9")

        result = subtract(a, b)
        expected = 0.1
        assert abs(result - expected) < 1e-10

    @pytest.mark.unit
    @pytest.mark.edge_case
    @pytest.mark.parametrize("a_str,b_str,expected", [
        ("0.2", "0.5", 0.1),
        ("1.1", "2.2", 2.42),
        ("0.333333", "0.333333", 0.111110888889),
        ("2", "3", 6),
        ("0.5", "0.5", 0.25),
    ])
    def test_floating_point_multiplication_precision(self, a_str, b_str, expected):
        """Test floating-point precision in multiplication.

        Parametrized test for various floating-point multiplication scenarios.
        Avoids the 0.1 * 0.1 edge case due to binary floating-point representation.
        """
        a = validate_number(a_str)
        b = validate_number(b_str)
        result = multiply(a, b)

        # Use relative error tolerance for better precision handling
        rel_error = abs(result - expected) / abs(expected) if expected != 0 else 0
        assert rel_error < 1e-6

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_floating_point_division_precision(self):
        """Test floating-point precision in division."""
        # Test: 1 / 3 should be approximately 0.333...
        result = divide(1, 3)
        assert abs(result - (1 / 3)) < 1e-15

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_very_small_number_addition(self):
        """Test addition of very small numbers."""
        a = 1e-300
        b = 1e-300
        result = add(a, b)
        expected = 2e-300

        # Use relative comparison for very small numbers
        rel_error = abs(result - expected) / abs(expected) if expected != 0 else 0
        assert rel_error < 1e-10 or result == expected

    @pytest.mark.unit
    @pytest.mark.edge_case
    def test_very_large_number_operations(self):
        """Test operations with very large numbers."""
        a = 1e308
        b = 1e-308

        # Very large + very small ≈ very large
        result_add = add(a, b)
        assert result_add > 1e307

        # Very large * 1.0 = very large
        result_mult = multiply(a, 1.0)
        assert result_mult == a


# ==================== OPERATION CHAINING TESTS ====================

class TestOperationChaining:
    """Test complex operation chaining scenarios."""

    @pytest.mark.integration
    def test_three_operation_chain_add_subtract_multiply(self):
        """Test chaining: ((a + b) - c) * d."""
        a, b, c, d = 10, 5, 3, 2
        result = multiply(subtract(add(a, b), c), d)
        # ((10 + 5) - 3) * 2 = (15 - 3) * 2 = 12 * 2 = 24
        assert result == 24

    @pytest.mark.integration
    def test_four_operation_chain(self):
        """Test chaining: (((a + b) * c) - d) / e."""
        a, b, c, d, e = 2, 3, 4, 5, 2
        result = divide(subtract(multiply(add(a, b), c), d), e)
        # (((2 + 3) * 4) - 5) / 2 = ((5 * 4) - 5) / 2 = (20 - 5) / 2 = 15 / 2 = 7.5
        assert result == 7.5

    @pytest.mark.integration
    @pytest.mark.parametrized
    @pytest.mark.parametrize("a,b,c,d,expression", [
        (10, 2, 3, 4, "((a + b) * c) - d"),
        (20, 5, 2, 3, "((a - b) * c) / d"),
        (8, 2, 2, 2, "(((a / b) * c) + d)"),
        (5, 5, 2, 3, "((a * b) - c - d)"),
    ])
    def test_operation_chains_parametrized(self, a, b, c, d, expression):
        """Parametrized test for various operation chains.

        Tests different combinations of operations with meaningful expressions.
        """
        if expression == "((a + b) * c) - d":
            result = subtract(multiply(add(a, b), c), d)
            expected = ((a + b) * c) - d
        elif expression == "((a - b) * c) / d":
            result = divide(multiply(subtract(a, b), c), d)
            expected = ((a - b) * c) / d
        elif expression == "(((a / b) * c) + d)":
            temp = divide(a, b)
            result = add(multiply(temp, c), d)
            expected = ((a / b) * c) + d
        elif expression == "((a * b) - c - d)":
            result = subtract(subtract(multiply(a, b), c), d)
            expected = ((a * b) - c) - d

        assert abs(result - expected) < 1e-9

    @pytest.mark.integration
    def test_operation_chain_with_validation(self):
        """Test operation chain with input validation."""
        # Simulate user input through validation
        num1_str = "100"
        num2_str = "50"
        num3_str = "2"

        num1 = validate_number(num1_str)
        num2 = validate_number(num2_str)
        num3 = validate_number(num3_str)

        # (100 + 50) / 2 = 75
        result = divide(add(num1, num2), num3)
        assert result == 75.0


# ==================== STRESS TESTS ====================

class TestStressScenarios:
    """Stress tests with extreme values and edge cases."""

    @pytest.mark.edge_case
    def test_repeated_operations_dont_accumulate_error(self):
        """Test that repeated operations don't accumulate floating-point errors significantly."""
        result = 1.0
        # Add 0.1 ten times
        for _ in range(10):
            result = add(result, 0.1)

        # Should be approximately 2.0 (1.0 + 10 * 0.1)
        assert abs(result - 2.0) < 1e-10

    @pytest.mark.edge_case
    def test_division_series_convergence(self):
        """Test division series converges correctly."""
        result = 1000
        # Divide by 10 four times
        for _ in range(4):
            result = divide(result, 10)

        # Should be 0.1
        assert abs(result - 0.1) < 1e-10

    @pytest.mark.edge_case
    def test_alternating_operations_identity(self):
        """Test that a - a = 0 for various values."""
        test_values = [1, -1, 0.5, -0.5, 1e100, 1e-100, 999999]
        for val in test_values:
            result = subtract(val, val)
            assert abs(result) < 1e-10, f"Failed for value {val}"

    @pytest.mark.edge_case
    def test_multiplication_division_inverse_operations(self):
        """Test that (a * b) / b ≈ a for various values."""
        test_pairs = [
            (5, 2),
            (100, 7),
            (0.5, 3),
            (-10, 4),
            (1e10, 1e5),
        ]
        for a, b in test_pairs:
            result = divide(multiply(a, b), b)
            expected = float(a)
            # Use relative error for better comparison with very large/small numbers
            rel_error = abs(result - expected) / abs(expected) if expected != 0 else 0
            assert rel_error < 1e-10, f"Failed for a={a}, b={b}"


# ==================== COMPREHENSIVE INTEGRATION TESTS ====================

class TestComprehensiveIntegration:
    """Comprehensive integration tests covering multiple aspects."""

    @pytest.mark.integration
    def test_calculator_workflow_with_all_operations(self):
        """Test complete calculator workflow with all operations in sequence."""
        # Simulate: Start with 10, add 5, multiply by 2, subtract 4, divide by 2
        start = validate_number("10")
        assert start == 10.0

        result = add(start, 5)
        assert result == 15.0

        result = multiply(result, 2)
        assert result == 30.0

        result = subtract(result, 4)
        assert result == 26.0

        result = divide(result, 2)
        assert result == 13.0

    @pytest.mark.integration
    def test_error_handling_in_chain(self):
        """Test error handling in operation chains."""
        a = 10
        b = 0

        # Try to divide by zero
        result = divide(a, b)
        assert result is None

        # Continue with different values
        result = divide(20, 2)
        assert result == 10.0

    @pytest.mark.integration
    def test_validation_with_edge_case_inputs(self):
        """Test input validation with various edge cases."""
        edge_case_inputs = {
            "0": 0.0,
            "-0": 0.0,
            "0.0": 0.0,
            "1e5": 100000.0,
            "-1e-5": -0.00001,
            "999999999": 999999999.0,
            "0.000000001": 1e-9,
        }

        for input_str, expected in edge_case_inputs.items():
            result = validate_number(input_str)
            assert result is not None
            assert abs(result - expected) < max(1e-10, abs(expected) * 1e-10)

    @pytest.mark.integration
    @pytest.mark.parametrized
    def test_all_operation_functions_callable(self):
        """Test that all operation functions are properly callable."""
        operations = ["+", "-", "*", "/"]

        for op in operations:
            func = get_operation_function(op)
            assert func is not None
            assert callable(func)

            # Test that function works
            if op != "/":
                result = func(10, 2)
                assert result is not None


# ==================== DOCUMENTATION TESTS ====================

class TestDocumentation:
    """Tests that verify documentation examples work correctly."""

    @pytest.mark.integration
    def test_example_simple_addition(self):
        """Test documentation example: simple addition.

        Example: Add 5 and 3
        Expected: 8
        """
        result = add(5, 3)
        assert result == 8

    @pytest.mark.integration
    def test_example_complex_expression(self):
        """Test documentation example: complex expression.

        Example: Calculate (10 + 5) * 2 - 3 / (6 / 2)
        Expected: 30 - 1 = 29
        """
        # (10 + 5) * 2 = 30
        temp1 = multiply(add(10, 5), 2)
        # 6 / 2 = 3
        temp2 = divide(6, 2)
        # 3 / 3 = 1
        temp3 = divide(3, temp2)
        # 30 - 1 = 29
        result = subtract(temp1, temp3)
        assert result == 29.0

    @pytest.mark.integration
    def test_example_division_by_zero_handling(self):
        """Test documentation example: division by zero handling.

        Example: Attempt to divide 10 by 0
        Expected: None (error handling)
        """
        result = divide(10, 0)
        assert result is None
