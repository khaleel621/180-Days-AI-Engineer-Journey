"""
Tests for Day 18 - Trapping Rain Water (Two Pointers) in
02-data-structures-algorithms/two-pointers/day18-trapping-rain-water.py.

Covers:
  - The required test cases from the task.
  - Empty list, single element, increasing heights, decreasing heights,
    equal heights, and multiple water-trapping sections.
  - Input list immutability.

The implementation is loaded by file path so the tests work regardless of the
current working directory. A two-pointers approach is used (O(n) time,
O(1) additional space).
"""

import importlib.util
import os

# Load day18-trapping-rain-water.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day18-trapping-rain-water.py")
_spec = importlib.util.spec_from_file_location("day18_trapping_rain_water", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

trap = _module.trap


def _check(heights, expected):
    """Run trap and assert the result and input immutability."""
    original = list(heights)
    result = trap(heights)
    assert result == expected, (
        f"trap({heights}) = {result}, expected {expected}"
    )
    assert heights == original, f"Input was modified: {heights}"


# -----------------------------------------------------------
# Required test cases from the task
# -----------------------------------------------------------

def test_case_empty_list():
    """[] -> 0"""
    _check([], 0)


def test_case_single_element():
    """[5] -> 0"""
    _check([5], 0)


def test_case_increasing_heights():
    """[1, 2, 3, 4] -> 0"""
    _check([1, 2, 3, 4], 0)


def test_case_decreasing_heights():
    """[4, 3, 2, 1] -> 0"""
    _check([4, 3, 2, 1], 0)


def test_case_multiple_sections():
    """[3, 0, 2, 0, 4] -> 7"""
    _check([3, 0, 2, 0, 4], 7)


def test_case_classic():
    """[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> 6"""
    _check([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)


# -----------------------------------------------------------
# Additional checks
# -----------------------------------------------------------

def test_case_equal_heights():
    """[2, 2, 2] -> 0 (no water can be trapped on equal-height bars)"""
    _check([2, 2, 2], 0)


def test_case_two_bars():
    """[1, 2] -> 0 (less than 3 bars cannot trap water)"""
    _check([1, 2], 0)


def test_case_input_not_modified():
    """Input list must remain unchanged after trap()."""
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    original = list(heights)
    trap(heights)
    assert heights == original


def test_case_multiple_water_sections():
    """[4, 2, 0, 3, 2, 5] -> 9 (two separate water-trapping sections)"""
    _check([4, 2, 0, 3, 2, 5], 9)


if __name__ == "__main__":
    test_case_empty_list()
    test_case_single_element()
    test_case_increasing_heights()
    test_case_decreasing_heights()
    test_case_multiple_sections()
    test_case_classic()
    test_case_equal_heights()
    test_case_two_bars()
    test_case_multiple_water_sections()
    test_case_input_not_modified()
    print("All test_day18_trapping_rain_water tests passed!")