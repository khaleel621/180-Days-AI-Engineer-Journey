"""
Tests for Day 10 — tuple_information() and remove_duplicates() in
day10-tuples-and-sets.py.

Covers: normal tuples, empty tuples, single-element tuples,
duplicate removal, ordering note, and input-not-modified.
"""

import importlib.util
import os

# Load day10-tuples-and-sets.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day10-tuples-and-sets.py")
_spec = importlib.util.spec_from_file_location("day10_tuples_and_sets", _module_path)
_day10_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day10_module)

tuple_information = _day10_module.tuple_information
remove_duplicates = _day10_module.remove_duplicates


# ------------------------------------------------------------
# tuple_information tests
# ------------------------------------------------------------

def test_tuple_information_normal_tuple():
    """A normal tuple returns count, first, and last correctly."""
    result = tuple_information((10, 20, 30))
    assert result == {"count": 3, "first": 10, "last": 30}


def test_tuple_information_single_element():
    """A single-element tuple returns count 1, first == last == that element."""
    result = tuple_information((42,))
    assert result == {"count": 1, "first": 42, "last": 42}


def test_tuple_information_empty_tuple():
    """An empty tuple returns count 0, first None, last None."""
    result = tuple_information(())
    assert result == {"count": 0, "first": None, "last": None}


def test_tuple_information_strings():
    """Tuple of strings works correctly."""
    result = tuple_information(("apple", "banana", "cherry"))
    assert result == {"count": 3, "first": "apple", "last": "cherry"}


def test_tuple_information_mixed_types():
    """Tuple of mixed types works correctly."""
    result = tuple_information((1, "hello", 3.14))
    assert result == {"count": 3, "first": 1, "last": 3.14}


def test_tuple_information_two_elements():
    """Tuple of two elements returns correct first and last."""
    result = tuple_information((100, 200))
    assert result == {"count": 2, "first": 100, "last": 200}


# ------------------------------------------------------------
# remove_duplicates tests
# ------------------------------------------------------------

def test_remove_duplicates_normal_input():
    """Duplicate values are removed, unique values returned."""
    result = remove_duplicates([1, 2, 2, 3, 1])
    assert set(result) == {1, 2, 3}
    assert len(result) == 3


def test_remove_duplicates_no_duplicates():
    """A list with no duplicates returns the same unique values."""
    result = remove_duplicates([1, 2, 3, 4])
    assert set(result) == {1, 2, 3, 4}
    assert len(result) == 4


def test_remove_duplicates_empty_list():
    """An empty list returns an empty list."""
    result = remove_duplicates([])
    assert result == []


def test_remove_duplicates_single_element():
    """A single-element list returns a list with that element."""
    result = remove_duplicates([42])
    assert result == [42]


def test_remove_duplicates_negative_numbers():
    """Negative numbers are handled correctly."""
    result = remove_duplicates([-1, -2, -1, -3])
    assert set(result) == {-1, -2, -3}


def test_remove_duplicates_all_same():
    """A list where all values are the same returns one element."""
    result = remove_duplicates([5, 5, 5, 5])
    assert set(result) == {5}
    assert len(result) == 1


def test_remove_duplicates_original_not_modified():
    """The original input list is NOT modified."""
    original = [1, 2, 2, 3, 1]
    original_copy = list(original)
    remove_duplicates(original)
    assert original == original_copy


if __name__ == "__main__":
    test_tuple_information_normal_tuple()
    test_tuple_information_single_element()
    test_tuple_information_empty_tuple()
    test_tuple_information_strings()
    test_tuple_information_mixed_types()
    test_tuple_information_two_elements()

    test_remove_duplicates_normal_input()
    test_remove_duplicates_no_duplicates()
    test_remove_duplicates_empty_list()
    test_remove_duplicates_single_element()
    test_remove_duplicates_negative_numbers()
    test_remove_duplicates_all_same()
    test_remove_duplicates_original_not_modified()

    print("All day10-tuples-and-sets tests passed!")