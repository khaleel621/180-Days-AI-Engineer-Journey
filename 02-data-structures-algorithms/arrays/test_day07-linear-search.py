"""
Tests for Day 7 — linear_search() in day07-linear-search.py.

Covers: target exists, target missing, first element, last element,
empty list, and single-element list (found and not found).

The function uses a for loop and checks each element one by one;
list.index() is intentionally not used so the search pattern is explicit.
"""

import importlib.util
import os

# Load day07-linear-search.py by file path so the test works regardless of
# the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day07-linear-search.py")
_spec = importlib.util.spec_from_file_location("day07_linear_search", _module_path)
_day07_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day07_module)

linear_search = _day07_module.linear_search


def test_linear_search_target_exists():
    """[10, 20, 30, 40, 50] with target 30 should return index 2."""
    assert linear_search([10, 20, 30, 40, 50], 30) == 2


def test_linear_search_target_missing():
    """A target not in the list should return -1."""
    assert linear_search([10, 20, 30, 40, 50], 100) == -1


def test_linear_search_target_is_first_element():
    """Searching for the first element should return index 0."""
    assert linear_search([10, 20, 30, 40, 50], 10) == 0


def test_linear_search_target_is_last_element():
    """Searching for the last element should return the last index."""
    assert linear_search([10, 20, 30, 40, 50], 50) == 4


def test_linear_search_empty_list():
    """An empty list should return -1 for any target."""
    assert linear_search([], 10) == -1


def test_linear_search_single_element_found():
    """A single-element list containing the target should return index 0."""
    assert linear_search([42], 42) == 0


def test_linear_search_single_element_not_found():
    """A single-element list not containing the target should return -1."""
    assert linear_search([42], 7) == -1


if __name__ == "__main__":
    test_linear_search_target_exists()
    test_linear_search_target_missing()
    test_linear_search_target_is_first_element()
    test_linear_search_target_is_last_element()
    test_linear_search_empty_list()
    test_linear_search_single_element_found()
    test_linear_search_single_element_not_found()
    print("All day07-linear-search tests passed!")