"""
Tests for Day 6 — count_frequency() and find_duplicates() in
day06-frequency-and-duplicates.py.

Both functions use a loop and a dictionary/set (not list.count() or
collections.Counter).
"""

import importlib.util
import os

# Load day06-frequency-and-duplicates.py by file path so the test works
# regardless of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day06-frequency-and-duplicates.py")
_spec = importlib.util.spec_from_file_location("day06_frequency_and_duplicates", _module_path)
_day06_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day06_module)

count_frequency = _day06_module.count_frequency
find_duplicates = _day06_module.find_duplicates


def test_count_frequency_example():
    """[2, 5, 2, 8, 2, 5, 9] -> {2: 3, 5: 2, 8: 1, 9: 1}."""
    numbers = [2, 5, 2, 8, 2, 5, 9]
    assert count_frequency(numbers) == {2: 3, 5: 2, 8: 1, 9: 1}


def test_count_frequency_empty_list():
    """An empty list returns an empty dictionary."""
    assert count_frequency([]) == {}


def test_count_frequency_zeros_and_negatives():
    """Zero and negative numbers are counted like any other number."""
    numbers = [0, -1, 0, -1, -3]
    assert count_frequency(numbers) == {0: 2, -1: 2, -3: 1}


def test_find_duplicates_example():
    """[2, 5, 2, 8, 2, 5, 9] -> [2, 5] (order of first repeated detection)."""
    numbers = [2, 5, 2, 8, 2, 5, 9]
    assert find_duplicates(numbers) == [2, 5]


def test_find_duplicates_empty_list():
    """An empty list has no duplicates."""
    assert find_duplicates([]) == []


def test_find_duplicates_only_unique_values():
    """A list where every value is unique produces no duplicates."""
    assert find_duplicates([1, 2, 3, 4]) == []


def test_find_duplicates_all_values_same():
    """A list where every value is the same reports that value once."""
    assert find_duplicates([7, 7, 7, 7]) == [7]


def test_find_duplicates_multiple_duplicates():
    """Multiple repeated values are reported once each, in detection order."""
    assert find_duplicates([1, 2, 1, 3, 2, 4, 3]) == [1, 2, 3]


def test_find_duplicates_zeros_and_negatives():
    """Zero and negative numbers are detected as duplicates correctly."""
    numbers = [0, -2, 0, 5, -2, -2, 0]
    assert find_duplicates(numbers) == [0, -2]


def test_find_duplicates_each_duplicate_once():
    """A value repeated many times still appears only once in the result."""
    assert find_duplicates([2, 2, 2]) == [2]


if __name__ == "__main__":
    test_count_frequency_example()
    test_count_frequency_empty_list()
    test_count_frequency_zeros_and_negatives()
    test_find_duplicates_example()
    test_find_duplicates_empty_list()
    test_find_duplicates_only_unique_values()
    test_find_duplicates_all_values_same()
    test_find_duplicates_multiple_duplicates()
    test_find_duplicates_zeros_and_negatives()
    test_find_duplicates_each_duplicate_once()
    print("All day06-frequency-and-duplicates tests passed!")