"""
Tests for Day 20 - Minimum Window Substring in
02-data-structures-algorithms/strings/day20-minimum-window-substring.py.

Covers:
  1. Normal example: s="ADOBECODEBANC", t="ABC" -> "BANC".
  2. No valid substring: s="ABCDEF", t="G" -> "".
  3. Exact matching substring: s="ABC", t="ABC" -> "ABC".
  4. Duplicate characters in t: s="aabbcc", t="aabc" -> "aabbc".
  5. Empty input: s="" or t="" -> "".
  6. Single-character input: s="a", t="a" -> "a".
  7. t longer than s -> "".

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day20-minimum-window-substring.py by file path.
_module_path = os.path.join(
    os.path.dirname(__file__), "day20-minimum-window-substring.py"
)
_spec = importlib.util.spec_from_file_location(
    "day20_minimum_window_substring", _module_path
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

min_window = _module.min_window


# -----------------------------------------------------------
# Required test cases from the task
# -----------------------------------------------------------

def test_normal_example():
    """s='ADOBECODEBANC', t='ABC' -> 'BANC'."""
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"


def test_no_valid_substring():
    """When t's characters are not in s, return ''."""
    assert min_window("ABCDEF", "G") == ""


def test_exact_matching_substring():
    """When s equals t, return s itself."""
    assert min_window("ABC", "ABC") == "ABC"


def test_duplicate_characters_in_t():
    """t='aabc' needs two a's, one b, one c -> 'aabbc'."""
    assert min_window("aabbcc", "aabc") == "aabbc"


def test_empty_input():
    """Empty s or empty t returns ''. """
    assert min_window("", "A") == ""
    assert min_window("A", "") == ""


def test_single_character_input():
    """Single-character match returns that character."""
    assert min_window("a", "a") == "a"


# -----------------------------------------------------------
# Additional edge cases
# -----------------------------------------------------------

def test_t_longer_than_s():
    """If t is longer than s, no window can exist."""
    assert min_window("a", "aa") == ""


def test_multiple_valid_windows_returns_smallest():
    """Return the smallest among several valid windows."""
    assert min_window("abcaabca", "abc") == "abc"


def test_all_characters_same():
    """s and t made of the same repeated character."""
    assert min_window("aaaa", "aa") == "aa"


if __name__ == "__main__":
    test_normal_example()
    test_no_valid_substring()
    test_exact_matching_substring()
    test_duplicate_characters_in_t()
    test_empty_input()
    test_single_character_input()
    test_t_longer_than_s()
    test_multiple_valid_windows_returns_smallest()
    test_all_characters_same()
    print("All test_day20_minimum_window_substring tests passed!")