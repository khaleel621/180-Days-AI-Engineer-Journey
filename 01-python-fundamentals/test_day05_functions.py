"""
Tests for Day 5 — add_numbers() in day05-functions.py.

These tests verify that add_numbers returns the correct sum for
positive numbers, zeros, and a mix of negative and positive numbers.
"""

import importlib.util
import os

# Load day05-functions.py by file path so the test works regardless of
# the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day05-functions.py")
_spec = importlib.util.spec_from_file_location("day05_functions", _module_path)
_day05_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day05_module)
add_numbers = _day05_module.add_numbers


def test_add_numbers_ten_and_twenty():
    """10 + 20 should equal 30."""
    assert add_numbers(10, 20) == 30


def test_add_numbers_zeros():
    """0 + 0 should equal 0."""
    assert add_numbers(0, 0) == 0


def test_add_numbers_negative_and_positive():
    """-5 + 2 should equal -3."""
    assert add_numbers(-5, 2) == -3


if __name__ == "__main__":
    test_add_numbers_ten_and_twenty()
    test_add_numbers_zeros()
    test_add_numbers_negative_and_positive()
    print("All day05-functions tests passed!")
