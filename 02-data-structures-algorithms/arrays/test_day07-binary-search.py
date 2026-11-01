"""
Tests for Day 7 — binary_search() in day07-binary-search.py.

Covers: target exists, target missing, first element, last element,
empty list, single-element list, an even-length list, and an odd-length list.

IMPORTANT: binary_search requires a sorted list. All lists below are sorted.
"""

import importlib.util
import os

# Load day07-binary-search.py by file path so the test works regardless of
# the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day07-binary-search.py")
_spec = importlib.util.spec_from_file_location("day07_binary_search", _module_path)
_day07_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day07_module)

binary_search = _day07_module.binary_search


def test_binary_search_target_exists_odd_length():
    """[10, 20, 30, 40, 50, 60, 70] with target 50 should return index 4."""
    assert binary_search([10, 20, 30, 40, 50, 60, 70], 50) == 4


def test_binary_search_target_missing():
    """A target not in the sorted list should return -1."""
    assert binary_search([10, 20, 30, 40, 50, 60, 70], 35) == -1


def test_binary_search_target_is_first_element():
    """Searching for the first element should return index 0."""
    assert binary_search([10, 20, 30, 40, 50, 60, 70], 10) == 0


def test_binary_search_target_is_last_element():
    """Searching for the last element should return the last index."""
    assert binary_search([10, 20, 30, 40, 50, 60, 70], 70) == 6


def test_binary_search_empty_list():
    """An empty list should return -1 for any target."""
    assert binary_search([], 10) == -1


def test_binary_search_single_element_found():
    """A single-element list containing the target should return index 0."""
    assert binary_search([99], 99) == 0


def test_binary_search_single_element_not_found():
    """A single-element list not containing the target should return -1."""
    assert binary_search([99], 5) == -1


def test_binary_search_even_number_of_elements():
    """An even-length sorted list [5, 15, 25, 35] with target 25 -> index 2."""
    assert binary_search([5, 15, 25, 35], 25) == 2
    # Target between two middle elements is absent in an even-length list.
    assert binary_search([5, 15, 25, 35], 20) == -1


def test_binary_search_odd_number_of_elements():
    """An odd-length sorted list [5, 15, 25] with target 15 -> index 1."""
    assert binary_search([5, 15, 25], 15) == 1


if __name__ == "__main__":
    test_binary_search_target_exists_odd_length()
    test_binary_search_target_missing()
    test_binary_search_target_is_first_element()
    test_binary_search_target_is_last_element()
    test_binary_search_empty_list()
    test_binary_search_single_element_found()
    test_binary_search_single_element_not_found()
    test_binary_search_even_number_of_elements()
    test_binary_search_odd_number_of_elements()
    print("All day07-binary-search tests passed!")