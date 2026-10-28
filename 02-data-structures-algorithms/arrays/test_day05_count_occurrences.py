"""
Tests for Day 5 — count_occurrences() in day05-count-occurrences.py.

These tests verify that the function counts target occurrences using a
loop and counter (not list.count() or collections.Counter), including
edge cases such as empty lists and absent targets.
"""

import importlib.util
import os

# Load day05-count-occurrences.py by file path so the test works
# regardless of the current working directory when executed.
_module_path = os.path.join(os.path.dirname(__file__), "day05-count-occurrences.py")
_spec = importlib.util.spec_from_file_location("day05_count_occurrences", _module_path)
_day05_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day05_module)
count_occurrences = _day05_module.count_occurrences


def test_count_occurrences_basic_case():
    """[1, 2, 2, 3, 2] with target 2 should return 3."""
    assert count_occurrences([1, 2, 2, 3, 2], 2) == 3


def test_count_occurrences_all_match():
    """[4, 4, 4, 4] with target 4 should return 4."""
    assert count_occurrences([4, 4, 4, 4], 4) == 4


def test_count_occurrences_target_absent():
    """[1, 3, 5, 7] with target 2 should return 0."""
    assert count_occurrences([1, 3, 5, 7], 2) == 0


def test_count_occurrences_empty_list():
    """An empty list with any target should return 0."""
    assert count_occurrences([], 5) == 0


def test_count_occurrences_zeros_and_negatives():
    """[0, -1, 0, 2] with target 0 should return 2."""
    assert count_occurrences([0, -1, 0, 2], 0) == 2


if __name__ == "__main__":
    test_count_occurrences_basic_case()
    test_count_occurrences_all_match()
    test_count_occurrences_target_absent()
    test_count_occurrences_empty_list()
    test_count_occurrences_zeros_and_negatives()
    print("All day05-count-occurrences tests passed!")
