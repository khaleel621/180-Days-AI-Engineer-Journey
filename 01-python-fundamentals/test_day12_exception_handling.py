"""
Tests for Day 12 - Exception Handling in day12-exception-handling.py.

Covers: safe_divide (normal division, division by zero) and
convert_to_integer (positive, negative, zero, and invalid input).
"""

import importlib.util
import os

# Load day12-exception-handling.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day12-exception-handling.py")
_spec = importlib.util.spec_from_file_location("day12_exception_handling", _module_path)
_day12_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day12_module)

safe_divide = _day12_module.safe_divide
convert_to_integer = _day12_module.convert_to_integer


# ------------------------------------------------------------
# safe_divide tests
# ------------------------------------------------------------


def test_safe_divide_normal():
    """10 / 2 should return 5.0."""
    assert safe_divide(10, 2) == 5.0


def test_safe_divide_float_result():
    """7 / 2 should return 3.5."""
    assert safe_divide(7, 2) == 3.5


def test_safe_divide_negative_numbers():
    """-10 / 2 should return -5.0."""
    assert safe_divide(-10, 2) == -5.0


def test_safe_divide_by_zero():
    """Dividing by zero must not crash; a clear message should be returned."""
    result = safe_divide(10, 0)
    assert isinstance(result, str)
    assert "zero" in result.lower()


def test_safe_divide_zero_dividend():
    """0 / 5 should return 0.0."""
    assert safe_divide(0, 5) == 0.0


# ------------------------------------------------------------
# convert_to_integer tests
# ------------------------------------------------------------


def test_convert_to_integer_positive():
    """'42' should convert to the integer 42."""
    assert convert_to_integer("42") == 42


def test_convert_to_integer_negative():
    """'-7' should convert to the integer -7."""
    assert convert_to_integer("-7") == -7


def test_convert_to_integer_zero():
    """'0' should convert to the integer 0."""
    assert convert_to_integer("0") == 0


def test_convert_to_integer_invalid_string():
    """'abc' must not crash; a clear message should be returned."""
    result = convert_to_integer("abc")
    assert isinstance(result, str)
    assert "not a valid integer" in result


def test_convert_to_integer_invalid_float_string():
    """'3.14' cannot be converted with int(); a clear message should be returned."""
    result = convert_to_integer("3.14")
    assert isinstance(result, str)
    assert "not a valid integer" in result


if __name__ == "__main__":
    test_safe_divide_normal()
    test_safe_divide_float_result()
    test_safe_divide_negative_numbers()
    test_safe_divide_by_zero()
    test_safe_divide_zero_dividend()

    test_convert_to_integer_positive()
    test_convert_to_integer_negative()
    test_convert_to_integer_zero()
    test_convert_to_integer_invalid_string()
    test_convert_to_integer_invalid_float_string()

    print("All day12-exception-handling tests passed!")