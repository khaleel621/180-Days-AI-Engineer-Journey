"""
Beginner-friendly tests for Two Sum (nested loop approach).

These tests verify the two_sum function works correctly for basic cases.
"""

import importlib.util
import os

# Load the two_sum module by file path (hyphenated name)
_module_path = os.path.join(os.path.dirname(__file__), "two-sum.py")
_spec = importlib.util.spec_from_file_location("two_sum", _module_path)
_two_sum_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_two_sum_module)
two_sum = _two_sum_module.two_sum


def test_two_sum_basic_case():
    """Standard example: [2, 7, 11, 15] with target 9 should return (0, 1)."""
    result = two_sum([2, 7, 11, 15], 9)
    assert result == (0, 1)


def test_two_sum_no_solution():
    """When no pair sums to target, return None."""
    result = two_sum([1, 2, 3], 10)
    assert result is None


def test_two_sum_negative_numbers():
    """Should work with negative numbers."""
    result = two_sum([-3, 4, 5, 1], 1)
    assert result is not None
    i, j = result
    assert (-3 + 4) == 1 or (-3 + 5) == 1 or (-3 + 1) == 1 or (4 + 5) == 1 or (4 + 1) == 1 or (5 + 1) == 1


def test_two_sum_same_value_different_indices():
    """Same value at different indices should be handled correctly."""
    result = two_sum([3, 3], 6)
    assert result == (0, 1)


def test_two_sum_returns_distinct_indices():
    """The returned indices should never be the same."""
    result = two_sum([1, 2, 3, 4, 5], 7)
    assert result is not None
    i, j = result
    assert i != j


def test_two_sum_pair_sums_to_target():
    """The values at returned indices should sum to the target."""
    nums = [10, 20, 30, 40]
    target = 50
    result = two_sum(nums, target)
    assert result is not None
    i, j = result
    assert nums[i] + nums[j] == target


if __name__ == "__main__":
    test_two_sum_basic_case()
    test_two_sum_no_solution()
    test_two_sum_negative_numbers()
    test_two_sum_same_value_different_indices()
    test_two_sum_returns_distinct_indices()
    test_two_sum_pair_sums_to_target()
    print("All Two Sum tests passed!")