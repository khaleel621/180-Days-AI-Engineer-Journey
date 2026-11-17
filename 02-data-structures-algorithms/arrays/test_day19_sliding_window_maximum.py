"""
Tests for Day 19 - Sliding Window Maximum in
02-data-structures-algorithms/arrays/day19-sliding-window-maximum.py.

Covers:
  - The five required example test cases.
  - Empty input returns an empty list.
  - Invalid window sizes raise ValueError (k <= 0, k > len(numbers), non-int k).
  - Time complexity O(n), space complexity O(k) via monotonic deque.

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day19-sliding-window-maximum.py by file path.
_module_path = os.path.join(
    os.path.dirname(__file__), "day19-sliding-window-maximum.py"
)
_spec = importlib.util.spec_from_file_location(
    "day19_sliding_window_maximum", _module_path
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

max_sliding_window = _module.max_sliding_window


# -----------------------------------------------------------
# Required test cases from the task
# -----------------------------------------------------------

def test_case_1():
    """[1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]"""
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_case_2():
    """[1,2,3,4,5], k=2 -> [2,3,4,5]"""
    assert max_sliding_window([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5]


def test_case_3():
    """[5,5,5,5], k=2 -> [5,5,5]"""
    assert max_sliding_window([5, 5, 5, 5], 2) == [5, 5, 5]


def test_case_4():
    """[7], k=1 -> [7]"""
    assert max_sliding_window([7], 1) == [7]


def test_case_5():
    """[9,-1,4], k=2 -> [9,4]"""
    assert max_sliding_window([9, -1, 4], 2) == [9, 4]


# -----------------------------------------------------------
# Edge cases
# -----------------------------------------------------------

def test_empty_input():
    """Empty list returns an empty list."""
    assert max_sliding_window([], 3) == []


def test_k_zero_raises_value_error():
    """k=0 raises ValueError."""
    try:
        max_sliding_window([1, 2, 3], 0)
    except ValueError:
        pass
    else:
        raise AssertionError("max_sliding_window([1, 2, 3], 0) did not raise ValueError")


def test_k_negative_raises_value_error():
    """k=-1 raises ValueError."""
    try:
        max_sliding_window([1, 2, 3], -1)
    except ValueError:
        pass
    else:
        raise AssertionError("max_sliding_window([1, 2, 3], -1) did not raise ValueError")


def test_k_larger_than_list_raises_value_error():
    """k > len(numbers) raises ValueError."""
    try:
        max_sliding_window([1, 2, 3], 10)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "max_sliding_window([1, 2, 3], 10) did not raise ValueError"
        )


def test_k_bool_raises_value_error():
    """k=True (a bool) raises ValueError."""
    try:
        max_sliding_window([1, 2, 3], True)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "max_sliding_window([1, 2, 3], True) did not raise ValueError"
        )


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_empty_input()
    test_k_zero_raises_value_error()
    test_k_negative_raises_value_error()
    test_k_larger_than_list_raises_value_error()
    test_k_bool_raises_value_error()
    print("All test_day19_sliding_window_maximum tests passed!")