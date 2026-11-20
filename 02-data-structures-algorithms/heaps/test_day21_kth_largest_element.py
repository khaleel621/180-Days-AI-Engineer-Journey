"""
Tests for Day 21 - DSA Heap / Priority Queue in
02-data-structures-algorithms/heaps/day21-kth-largest-element.py.

Covers:
  - Normal example: nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
  - Array containing duplicates
  - K = 1 (the largest element)
  - K = len(nums) (the smallest element)
  - Single-element array
  - Invalid k values (0, negative, too large, non-integer)
  - Both implementations: find_kth_largest and find_kth_largest_using_nlargest

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day21-kth-largest-element.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day21-kth-largest-element.py")
_spec = importlib.util.spec_from_file_location("day21_kth_largest_element", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

find_kth_largest = _module.find_kth_largest
find_kth_largest_using_nlargest = _module.find_kth_largest_using_nlargest


# -----------------------------------------------------------
# Normal example
# -----------------------------------------------------------

def test_normal_example():
    """nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5."""
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


# -----------------------------------------------------------
# Duplicates
# -----------------------------------------------------------

def test_array_with_duplicates():
    """Duplicates count as separate elements."""
    # sorted [3, 4, 4, 5, 5]; 2nd largest = 5
    assert find_kth_largest([5, 5, 4, 4, 3], 2) == 5
    # sorted [1, 2, 2, 3]; 3rd largest = 2
    assert find_kth_largest([3, 2, 2, 1], 3) == 2
    # all identical
    assert find_kth_largest([7, 7, 7, 7], 2) == 7


# -----------------------------------------------------------
# K = 1 (largest)
# -----------------------------------------------------------

def test_k_is_one_returns_largest():
    """K = 1 should return the maximum element."""
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 1) == 6
    assert find_kth_largest([10, -5, 0, 100], 1) == 100


# -----------------------------------------------------------
# K = len(nums) (smallest)
# -----------------------------------------------------------

def test_k_equals_length_returns_smallest():
    """K = len(nums) should return the minimum element."""
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 6) == 1
    assert find_kth_largest([10, -5, 0, 100], 4) == -5


# -----------------------------------------------------------
# Single-element array
# -----------------------------------------------------------

def test_single_element_array():
    """A single-element array with k = 1 returns that element."""
    assert find_kth_largest([42], 1) == 42


# -----------------------------------------------------------
# Invalid k values
# -----------------------------------------------------------

def test_invalid_k_zero():
    """k = 0 should raise ValueError."""
    try:
        find_kth_largest([3, 2, 1], 0)
    except ValueError:
        pass
    else:
        raise AssertionError("find_kth_largest(..., 0) did not raise ValueError")


def test_invalid_k_negative():
    """k < 0 should raise ValueError."""
    try:
        find_kth_largest([3, 2, 1], -1)
    except ValueError:
        pass
    else:
        raise AssertionError("find_kth_largest(..., -1) did not raise ValueError")


def test_invalid_k_too_large():
    """k > len(nums) should raise ValueError."""
    try:
        find_kth_largest([3, 2, 1], 7)
    except ValueError:
        pass
    else:
        raise AssertionError("find_kth_largest(..., 7) did not raise ValueError")


def test_invalid_k_non_integer():
    """k that is not an integer should raise ValueError."""
    try:
        find_kth_largest([3, 2, 1], 2.5)
    except ValueError:
        pass
    else:
        raise AssertionError("find_kth_largest(..., 2.5) did not raise ValueError")


# -----------------------------------------------------------
# Both implementations agree
# -----------------------------------------------------------

def test_nlargest_implementation_matches():
    """find_kth_largest_using_nlargest should agree with find_kth_largest."""
    cases = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([5, 5, 4, 4, 3], 2),
        ([42], 1),
        ([10, -5, 0, 100], 4),
    ]
    for nums, k in cases:
        assert find_kth_largest(nums, k) == find_kth_largest_using_nlargest(nums, k)


if __name__ == "__main__":
    test_normal_example()
    test_array_with_duplicates()
    test_k_is_one_returns_largest()
    test_k_equals_length_returns_smallest()
    test_single_element_array()
    test_invalid_k_zero()
    test_invalid_k_negative()
    test_invalid_k_too_large()
    test_invalid_k_non_integer()
    test_nlargest_implementation_matches()
    print("All test_day21_kth_largest_element tests passed!")