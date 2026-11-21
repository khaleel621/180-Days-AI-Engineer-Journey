"""
Tests for Day 22 - DSA Top K Frequent Elements in
02-data-structures-algorithms/heaps/day22-top-k-frequent-elements.py.

Covers:
  - Normal example: nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
  - All elements identical
  - All elements have equal frequency
  - Negative numbers
  - Single-element array
  - k = 1
  - k equal to the number of distinct elements
  - Result has no duplicate numbers
  - Invalid k values (0, negative, too large, non-integer)
  - Both implementations: top_k_frequent_sorting and top_k_frequent_heap

Because several correct answers can exist when frequencies are tied,
results are compared as sets.
"""

import importlib.util
import os

# Load day22-top-k-frequent-elements.py by file path.
_module_path = os.path.join(
    os.path.dirname(__file__), "day22-top-k-frequent-elements.py"
)
_spec = importlib.util.spec_from_file_location(
    "day22_top_k_frequent_elements", _module_path
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

top_k_frequent_sorting = _module.top_k_frequent_sorting
top_k_frequent_heap = _module.top_k_frequent_heap

BOTH = [top_k_frequent_sorting, top_k_frequent_heap]


def _result_set(func, nums, k):
    """Return the result of func as a set (order-independent comparison)."""
    return set(func(nums, k))


# -----------------------------------------------------------
# Normal example
# -----------------------------------------------------------

def test_normal_example():
    """nums = [1, 1, 1, 2, 2, 3], k = 2 -> {1, 2}."""
    nums = [1, 1, 1, 2, 2, 3]
    for func in BOTH:
        assert _result_set(func, nums, 2) == {1, 2}


# -----------------------------------------------------------
# All elements identical
# -----------------------------------------------------------

def test_all_elements_identical():
    """Only one distinct element exists, so k = 1 returns it."""
    nums = [5, 5, 5, 5]
    for func in BOTH:
        assert _result_set(func, nums, 1) == {5}



def test_all_elements_equal_frequency():
    """Any valid set of k distinct elements is correct on a tie."""
    nums = [1, 2, 3, 4]
    for func in BOTH:
        result = _result_set(func, nums, 2)
        assert len(result) == 2
        assert result <= {1, 2, 3, 4}


# -----------------------------------------------------------
# All elements have equal frequency
# -----------------------------------------------------------

# -----------------------------------------------------------
# Negative numbers
# -----------------------------------------------------------

def test_negative_numbers():
    """Negative numbers are just dictionary keys."""
    nums = [-1, -1, -2, -2, -2, 3]
    for func in BOTH:
        assert _result_set(func, nums, 1) == {-2}


# -----------------------------------------------------------
# Single-element array
# -----------------------------------------------------------

def test_single_element_array():
    """nums = [7], k = 1 -> {7}."""
    for func in BOTH:
        assert _result_set(func, [7], 1) == {7}


# -----------------------------------------------------------
# k = 1
# -----------------------------------------------------------

def test_k_is_one():
    """k = 1 returns the most frequent element."""
    nums = [1, 1, 1, 2, 2, 3]
    for func in BOTH:
        assert _result_set(func, nums, 1) == {1}


# -----------------------------------------------------------
# k equal to the number of distinct elements
# -----------------------------------------------------------

def test_k_equals_distinct_count():
    """k = 3 with distinct elements {1, 2, 3} returns all of them."""
    nums = [1, 1, 1, 2, 2, 3]
    for func in BOTH:
        assert _result_set(func, nums, 3) == {1, 2, 3}


# -----------------------------------------------------------
# No duplicate numbers in the result
# -----------------------------------------------------------

def test_result_has_no_duplicates():
    """The result contains distinct numbers only."""
    nums = [1, 1, 1, 2, 2, 3]
    for func in BOTH:
        result = func(nums, 2)
        assert len(result) == len(set(result)) == 2


# -----------------------------------------------------------
# Invalid k values
# -----------------------------------------------------------

def test_invalid_k_zero():
    for func in BOTH:
        try:
            func([1, 2, 3], 0)
        except ValueError:
            pass
        else:
            raise AssertionError("k = 0 did not raise ValueError")


def test_invalid_k_negative():
    for func in BOTH:
        try:
            func([1, 2, 3], -2)
        except ValueError:
            pass
        else:
            raise AssertionError("k = -2 did not raise ValueError")


def test_invalid_k_too_large():
    """k = 5 is greater than the 3 distinct elements in [1, 2, 3]."""
    for func in BOTH:
        try:
            func([1, 2, 3], 5)
        except ValueError:
            pass
        else:
            raise AssertionError("k = 5 did not raise ValueError")


def test_invalid_k_non_integer():
    for func in BOTH:
        try:
            func([1, 2, 3], 2.5)
        except TypeError:
            pass
        else:
            raise AssertionError("k = 2.5 did not raise TypeError")


# -----------------------------------------------------------
# Return type
# -----------------------------------------------------------

def test_return_type_is_list():
    """Both implementations return a list."""
    nums = [1, 1, 1, 2, 2, 3]
    for func in BOTH:
        assert isinstance(func(nums, 2), list)


if __name__ == "__main__":
    test_normal_example()
    test_all_elements_identical()
    test_all_elements_equal_frequency()
    test_negative_numbers()
    test_single_element_array()
    test_k_is_one()
    test_k_equals_distinct_count()
    test_result_has_no_duplicates()
    test_invalid_k_zero()
    test_invalid_k_negative()
    test_invalid_k_too_large()
    test_invalid_k_non_integer()
    test_return_type_is_list()
    print("All test_day22_top_k_frequent_elements tests passed!")
