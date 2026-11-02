"""
Tests for Day 8 — bubble_sort() in day08-bubble-sort.py.

Covers: normal unsorted list, already sorted list, reverse-sorted list,
empty list, single-element list, duplicate numbers, negative numbers,
and lists containing zero.

The function returns a new sorted list and does not modify the original.
"""

import importlib.util
import os

# Load day08-bubble-sort.py by file path so the test works regardless of
# the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day08-bubble-sort.py")
_spec = importlib.util.spec_from_file_location("day08_bubble_sort", _module_path)
_day08_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day08_module)

bubble_sort = _day08_module.bubble_sort


def test_bubble_sort_normal_unsorted():
    """A typical unsorted list should be sorted ascending."""
    assert bubble_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]


def test_bubble_sort_already_sorted():
    """An already sorted list should remain unchanged."""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_reverse_sorted():
    """A reverse-sorted list should be sorted ascending."""
    assert bubble_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]


def test_bubble_sort_empty_list():
    """An empty list should return an empty list."""
    assert bubble_sort([]) == []


def test_bubble_sort_single_element():
    """A single-element list should return the same list."""
    assert bubble_sort([42]) == [42]


def test_bubble_sort_duplicates():
    """A list with duplicate values should handle them correctly."""
    assert bubble_sort([3, 1, 2, 1, 3, 2]) == [1, 1, 2, 2, 3, 3]


def test_bubble_sort_negative_numbers():
    """A list with negative numbers should sort them correctly."""
    assert bubble_sort([-3, 5, -1, 0, 2]) == [-3, -1, 0, 2, 5]


def test_bubble_sort_with_zero():
    """A list containing zero should place it in the correct position."""
    assert bubble_sort([0, -1, 3, 0, 2]) == [-1, 0, 0, 2, 3]


def test_bubble_sort_original_not_modified():
    """The original list should not be modified by bubble_sort."""
    original = [5, 3, 8, 1, 2]
    bubble_sort(original)
    assert original == [5, 3, 8, 1, 2]


if __name__ == "__main__":
    test_bubble_sort_normal_unsorted()
    test_bubble_sort_already_sorted()
    test_bubble_sort_reverse_sorted()
    test_bubble_sort_empty_list()
    test_bubble_sort_single_element()
    test_bubble_sort_duplicates()
    test_bubble_sort_negative_numbers()
    test_bubble_sort_with_zero()
    test_bubble_sort_original_not_modified()
    print("All day08-bubble-sort tests passed!")