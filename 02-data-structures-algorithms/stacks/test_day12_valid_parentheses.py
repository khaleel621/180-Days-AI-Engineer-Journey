"""
Tests for Day 12 - is_valid() in
02-data-structures-algorithms/stacks/day12-valid-parentheses.py.

Covers: valid parentheses, multiple bracket types, incorrect nesting,
unmatched brackets, empty string, single brackets.
"""

import importlib.util
import os

# Load day12-valid-parentheses.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day12-valid-parentheses.py")
_spec = importlib.util.spec_from_file_location("day12_valid_parentheses", _module_path)
_parentheses_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_parentheses_module)

is_valid = _parentheses_module.is_valid


# ------------------------------------------------------------
# Valid parentheses tests
# ------------------------------------------------------------


def test_simple_pair():
    """'()' is valid."""
    assert is_valid("()") is True


def test_multiple_bracket_types():
    """'()[]{}' is valid."""
    assert is_valid("()[]{}") is True


def test_nested_valid():
    """'{[]}' is valid: brackets are correctly nested."""
    assert is_valid("{[]}") is True


def test_empty_string():
    """An empty string is valid."""
    assert is_valid("") is True


# ------------------------------------------------------------
# Invalid parentheses tests
# ------------------------------------------------------------


def test_mismatched_types():
    """'(]' is invalid: ) does not match (."""
    assert is_valid("(]") is False


def test_incorrect_nesting():
    """'([)]' is invalid: closing order is wrong."""
    assert is_valid("([)]") is False


def test_unmatched_opening():
    """'(((' is invalid: opening brackets are never closed."""
    assert is_valid("(((") is False


def test_single_opening_bracket():
    """'[' is invalid: one unmatched opening bracket."""
    assert is_valid("[") is False


def test_single_closing_bracket():
    """']' is invalid: a closing bracket with no opening match."""
    assert is_valid("]") is False


if __name__ == "__main__":
    test_simple_pair()
    test_multiple_bracket_types()
    test_nested_valid()
    test_empty_string()
    test_mismatched_types()
    test_incorrect_nesting()
    test_unmatched_opening()
    test_single_opening_bracket()
    test_single_closing_bracket()

    print("All day12-valid-parentheses tests passed!")