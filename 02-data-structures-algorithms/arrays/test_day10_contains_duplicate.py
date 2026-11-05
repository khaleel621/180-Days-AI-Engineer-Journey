"""
Tests for Day 10 — contains_duplicate() in
day10-contains-duplicate.py.

Covers: duplicate values, no duplicates, empty list, one element,
negative numbers, repeated values, and larger input.
"""

import importlib.util
import os

# Load day10-contains-duplicate.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day10-contains-duplicate.py")
_spec = importlib.util.spec_from_file_location("day10_contains_duplicate", _module_path)
_day10_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day10_module)

contains_duplicate = _day10_module.contains_duplicate


def test_contains_duplicate_duplicate_values():
    """A list with a duplicate returns True."""
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_contains_duplicate_no_duplicates():
    """A list with all unique values returns False."""
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_contains_duplicate_empty_list():
    """An empty list returns False."""
    assert contains_duplicate([]) is False


def test_contains_duplicate_one_element():
    """A single-element list returns False."""
    assert contains_duplicate([42]) is False


def test_contains_duplicate_negative_numbers():
    """Negative numbers with a duplicate return True."""
    assert contains_duplicate([-1, -2, -3, -1]) is True


def test_contains_duplicate_repeated_values():
    """A list where all values are the same returns True."""
    assert contains_duplicate([5, 5]) is True


def test_contains_duplicate_larger_input():
    """A larger list without duplicates returns False."""
    assert contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is False


def test_contains_duplicate_duplicate_at_end():
    """A duplicate appearing at the end is detected."""
    assert contains_duplicate([1, 2, 3, 4, 5, 1]) is True


def test_contains_duplicate_duplicate_adjacent():
    """Adjacent duplicates are detected."""
    assert contains_duplicate([1, 1, 2, 3]) is True


if __name__ == "__main__":
    test_contains_duplicate_duplicate_values()
    test_contains_duplicate_no_duplicates()
    test_contains_duplicate_empty_list()
    test_contains_duplicate_one_element()
    test_contains_duplicate_negative_numbers()
    test_contains_duplicate_repeated_values()
    test_contains_duplicate_larger_input()
    test_contains_duplicate_duplicate_at_end()
    test_contains_duplicate_duplicate_adjacent()

    print("All day10-contains-duplicate tests passed!")