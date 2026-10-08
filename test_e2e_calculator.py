import subprocess
import pytest


class TestCalculatorE2E:
    """End-to-end tests for the calculator application"""

    @staticmethod
    def run_calculator(input_str):
        """Run the calculator with given input and return output"""
        process = subprocess.run(
            ["python3", "calculator.py"],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=5
        )
        return process.stdout, process.stderr, process.returncode

    def test_basic_addition(self):
        """Test basic addition operation"""
        output, stderr, code = self.run_calculator("5\n3\n+\n")
        assert code == 0, f"Process failed with stderr: {stderr}"
        assert "8" in output, f"Expected '8' in output, got: {output}"

    def test_basic_subtraction(self):
        """Test basic subtraction operation"""
        output, stderr, code = self.run_calculator("10\n4\n-\n")
        assert code == 0
        assert "6" in output

    def test_basic_multiplication(self):
        """Test basic multiplication operation"""
        output, stderr, code = self.run_calculator("7\n6\n*\n")
        assert code == 0
        assert "42" in output

    def test_basic_division(self):
        """Test basic division operation"""
        output, stderr, code = self.run_calculator("20\n4\n/\n")
        assert code == 0
        assert "5" in output

    def test_division_with_decimal(self):
        """Test division resulting in decimal"""
        output, stderr, code = self.run_calculator("10\n3\n/\n")
        assert code == 0
        assert "3.333" in output or "3.3" in output

    def test_division_by_zero(self):
        """Test division by zero handling"""
        output, stderr, code = self.run_calculator("10\n0\n/\n")
        assert code == 0
        assert "error" in output.lower() or "cannot" in output.lower()

    def test_negative_numbers(self):
        """Test operations with negative numbers"""
        output, stderr, code = self.run_calculator("-5\n3\n+\n")
        assert code == 0
        assert "-2" in output

    def test_invalid_operation_retry(self):
        """Test that invalid operation prompts for retry"""
        output, stderr, code = self.run_calculator("5\n3\n%\n+\n")
        assert code == 0
        assert "5" in output or "8" in output  # Should retry and eventually add

    def test_invalid_number_retry(self):
        """Test that invalid number input prompts for retry"""
        output, stderr, code = self.run_calculator("abc\n5\n5\n+\n")
        assert code == 0
        assert "10" in output  # Should skip invalid input and use second set

    def test_float_inputs(self):
        """Test operations with floating-point inputs"""
        output, stderr, code = self.run_calculator("2.5\n3.5\n+\n")
        assert code == 0
        assert "6" in output

    def test_large_numbers(self):
        """Test operations with large numbers"""
        output, stderr, code = self.run_calculator("1000000\n2000000\n+\n")
        assert code == 0
        assert "3000000" in output

    def test_zero_operations(self):
        """Test operations with zero"""
        output, stderr, code = self.run_calculator("0\n5\n+\n")
        assert code == 0
        assert "5" in output

    def test_multiply_by_zero(self):
        """Test multiplication by zero"""
        output, stderr, code = self.run_calculator("999\n0\n*\n")
        assert code == 0
        assert "0" in output
