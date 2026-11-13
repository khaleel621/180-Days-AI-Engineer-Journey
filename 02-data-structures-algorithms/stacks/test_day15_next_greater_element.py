"""
Tests for Day 15 - Next Greater Element in
02-data-structures-algorithms/stacks/day15-next-greater-element.py.

Covers all required examples, duplicates, empty input, single element, and
verifies the original input list is not modified.

The implementation is loaded by file path so the tests work regardless of the
current working directory. A stack is used (no nested-loop main solution).
"""

import importlib.util
import os

# Load day15-next-greater-element.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day15-next-greater-element.py")
_spec = importlib.util.spec_from_file_location("day15_next_greater_element", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

next_greater_element = _module.next_greater_element


def _check(numbers, expected):
    """Run next_greater_element and assert result and input immutability."""
    original = list(numbers)
    result = next_greater_element(numbers)
    assert result == expected, f"next_greater_element({numbers}) = {result}, expected {expected}"
    assert numbers == original, f"Input was modified: {numbers}"


# -----------------------------------------------------------
# Required test cases from the task
# -----------------------------------------------------------

def test_case_4_5_2_10_8():
    """[4, 5, 2, 10, 8] -> [5, 10, 10, -1, -1]"""
    _check([4, 5, 2, 10, 8], [5, 10, 10, -1, -1])


def test_case_1_2_3_4():
    """[1, 2, 3, 4] -> [2, 3, 4, -1]"""
    _check([1, 2, 3, 4], [2, 3, 4, -1])


def test_case_4_3_2_1():
    """[4, 3, 2, 1] -> [-1, -1, -1, -1]"""
    _check([4, 3, 2, 1], [-1, -1, -1, -1])


def test_case_5_5_5_duplicates():
    """[5, 5, 5] -> [-1, -1, -1] (duplicates: strictly greater required)"""
    _check([5, 5, 5], [-1, -1, -1])


def test_case_2_1_3():
    """[2, 1, 3] -> [3, 3, -1]"""
    _check([2, 1, 3], [3, 3, -1])


def test_case_empty_list():
    """[] -> []"""
    _check([], [])


# -----------------------------------------------------------
# Additional checks
# -----------------------------------------------------------

def test_single_element():
    _check([7], [-1])


def test_two_elements_increasing():
    _check([3, 7], [7, -1])


def test_two_elements_decreasing():
    _check([7, 3], [-1, -1])


def test_negative_numbers():
    _check([-3, -1, -2], [-1, -1, -1])


def test_input_not_modified():
    numbers = [4, 5, 2, 10, 8]
    original = list(numbers)
    next_greater_element(numbers)
    assert numbers == original


if __name__ == "__main__":
    test_case_4_5_2_10_8()
    test_case_1_2_3_4()
    test_case_4_3_2_1()
    test_case_5_5_5_duplicates()
    test_case_2_1_3()
    test_case_empty_list()
    test_single_element()
    test_two_elements_increasing()
    test_two_elements_decreasing()
    test_negative_numbers()
    test_input_not_modified()
    print("All test_day15_next_greater_element tests passed!")