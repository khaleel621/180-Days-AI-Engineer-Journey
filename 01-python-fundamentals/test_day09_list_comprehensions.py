"""
Tests for Day 9 — square_numbers() and filter_even_numbers() in
day09-list-comprehensions.py.

Covers: normal input, empty input, negative numbers, zero, duplicate
numbers, no even values, and verification that the input list remains
unchanged.
"""

import importlib.util
import os

# Load day09-list-comprehensions.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day09-list-comprehensions.py")
_spec = importlib.util.spec_from_file_location("day09_list_comprehensions", _module_path)
_day09_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day09_module)

square_numbers = _day09_module.square_numbers
filter_even_numbers = _day09_module.filter_even_numbers


# ------------------------------------------------------------
# square_numbers tests
# ------------------------------------------------------------

def test_square_numbers_normal_input():
    """Squaring a normal list of positive numbers works."""
    assert square_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]


def test_square_numbers_empty_input():
    """Squaring an empty list returns an empty list."""
    assert square_numbers([]) == []


def test_square_numbers_negative_numbers():
    """Squaring negative numbers produces positive squares."""
    assert square_numbers([-3, -2, -1]) == [9, 4, 1]


def test_square_numbers_zero():
    """Squaring zero produces zero."""
    assert square_numbers([0]) == [0]


def test_square_numbers_duplicate_numbers():
    """Squaring a list with duplicate values works correctly."""
    assert square_numbers([2, 2, 3, 3]) == [4, 4, 9, 9]


def test_square_numbers_mixed_signs():
    """Squaring a mix of negative, zero, and positive values."""
    assert square_numbers([-2, 0, 2]) == [4, 0, 4]


def test_square_numbers_original_not_modified():
    """The original list must not be modified by square_numbers."""
    original = [1, 2, 3, 4]
    square_numbers(original)
    assert original == [1, 2, 3, 4]


# ------------------------------------------------------------
# filter_even_numbers tests
# ------------------------------------------------------------

def test_filter_even_numbers_normal_input():
    """Filtering even numbers from a mixed list works."""
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_filter_even_numbers_empty_input():
    """Filtering an empty list returns an empty list."""
    assert filter_even_numbers([]) == []


def test_filter_even_numbers_negative_numbers():
    """Negative even numbers are included; negative odd numbers are not."""
    assert filter_even_numbers([-4, -3, -2, -1, 0]) == [-4, -2, 0]


def test_filter_even_numbers_zero():
    """Zero is even and is included in the result."""
    assert filter_even_numbers([0]) == [0]


def test_filter_even_numbers_duplicate_numbers():
    """Duplicate even numbers are all kept."""
    assert filter_even_numbers([2, 2, 4, 4, 5]) == [2, 2, 4, 4]


def test_filter_even_numbers_no_even_values():
    """A list with no even values returns an empty list."""
    assert filter_even_numbers([1, 3, 5, 7]) == []


def test_filter_even_numbers_all_even():
    """A list where all values are even returns the same list."""
    assert filter_even_numbers([2, 4, 6]) == [2, 4, 6]


def test_filter_even_numbers_original_not_modified():
    """The original list must not be modified by filter_even_numbers."""
    original = [1, 2, 3, 4, 5, 6]
    filter_even_numbers(original)
    assert original == [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    test_square_numbers_normal_input()
    test_square_numbers_empty_input()
    test_square_numbers_negative_numbers()
    test_square_numbers_zero()
    test_square_numbers_duplicate_numbers()
    test_square_numbers_mixed_signs()
    test_square_numbers_original_not_modified()

    test_filter_even_numbers_normal_input()
    test_filter_even_numbers_empty_input()
    test_filter_even_numbers_negative_numbers()
    test_filter_even_numbers_zero()
    test_filter_even_numbers_duplicate_numbers()
    test_filter_even_numbers_no_even_values()
    test_filter_even_numbers_all_even()
    test_filter_even_numbers_original_not_modified()

    print("All day09-list-comprehensions tests passed!")