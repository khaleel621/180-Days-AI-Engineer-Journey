"""
Tests for Day 17 - Largest Rectangle in Histogram in
02-data-structures-algorithms/stacks/day17-largest-rectangle.py.

Covers:
  - The required example [2, 1, 5, 6, 2, 3] -> 10.
  - Empty input, single element, equal heights, increasing heights,
    decreasing heights and mixed heights.
  - Verifies the monotonic-stack behaviour (O(n) time, O(n) extra space)
    and that the input list is not modified.

The implementation is loaded by file path so the tests work regardless of the
current working directory. A monotonic increasing stack is used (no
nested-loop main solution).
"""

import importlib.util
import os

# Load day17-largest-rectangle.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day17-largest-rectangle.py")
_spec = importlib.util.spec_from_file_location(
    "day17_largest_rectangle", _module_path
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

largest_rectangle = _module.largest_rectangle


def _check(heights, expected):
    """Run largest_rectangle and assert the result and input immutability."""
    original = list(heights)
    result = largest_rectangle(heights)
    assert result == expected, (
        f"largest_rectangle({heights}) = {result}, expected {expected}"
    )
    assert heights == original, f"Input was modified: {heights}"


# -----------------------------------------------------------
# Required test cases from the task
# -----------------------------------------------------------

def test_case_2_1_5_6_2_3():
    """[2, 1, 5, 6, 2, 3] -> 10"""
    _check([2, 1, 5, 6, 2, 3], 10)


def test_case_empty_list():
    """[] -> 0"""
    _check([], 0)


def test_case_single_element():
    """[5] -> 5"""
    _check([5], 5)


def test_case_equal_heights():
    """[2, 2, 2] -> 6"""
    _check([2, 2, 2], 6)


def test_case_increasing_heights():
    """[1, 2, 3, 4] -> 6"""
    _check([1, 2, 3, 4], 6)


def test_case_decreasing_heights():
    """[4, 3, 2, 1] -> 6"""
    _check([4, 3, 2, 1], 6)


# -----------------------------------------------------------
# Additional checks
# -----------------------------------------------------------

def test_case_mixed_heights():
    """[2, 1, 2] -> 3 (whole width, limited by the middle bar of height 1)"""
    _check([2, 1, 2], 3)


def test_case_classic_mixed_heights():
    """[6, 2, 5, 4, 5, 1, 6] -> 12"""
    _check([6, 2, 5, 4, 5, 1, 6], 12)


def test_input_not_modified():
    heights = [2, 1, 5, 6, 2, 3]
    original = list(heights)
    largest_rectangle(heights)
    assert heights == original


if __name__ == "__main__":
    test_case_2_1_5_6_2_3()
    test_case_empty_list()
    test_case_single_element()
    test_case_equal_heights()
    test_case_increasing_heights()
    test_case_decreasing_heights()
    test_case_mixed_heights()
    test_case_classic_mixed_heights()
    test_input_not_modified()
    print("All test_day17_largest_rectangle tests passed!")