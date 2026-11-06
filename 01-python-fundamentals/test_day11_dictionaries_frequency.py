"""
Tests for Day 11 — Dictionary Methods and Frequency Counting in
day11-dictionaries-frequency.py.

Covers: dictionary creation, access, add/update, remove, keys/values/items,
get, update, pop, iteration, calculate_total_marks, character_frequency.
"""

import importlib.util
import os

# Load day11-dictionaries-frequency.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day11-dictionaries-frequency.py")
_spec = importlib.util.spec_from_file_location("day11_dictionaries_frequency", _module_path)
_day11_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day11_module)

calculate_total_marks = _day11_module.calculate_total_marks
character_frequency = _day11_module.character_frequency


# ------------------------------------------------------------
# calculate_total_marks tests
# ------------------------------------------------------------

def test_calculate_total_marks_example():
    """The given example should return 250."""
    marks = {
        "Maths": 85,
        "Python": 90,
        "English": 75
    }
    assert calculate_total_marks(marks) == 250


def test_calculate_total_marks_empty_dict():
    """An empty dictionary should return 0."""
    assert calculate_total_marks({}) == 0


def test_calculate_total_marks_single_subject():
    """A single subject returns its mark."""
    assert calculate_total_marks({"Maths": 100}) == 100


def test_calculate_total_marks_zero_marks():
    """Marks of zero should sum to zero."""
    assert calculate_total_marks({"Maths": 0, "Python": 0}) == 0


def test_calculate_total_marks_negative_marks():
    """Negative marks are summed mathematically."""
    assert calculate_total_marks({"Maths": -10, "Python": 20}) == 10


# ------------------------------------------------------------
# character_frequency tests
# ------------------------------------------------------------

def test_character_frequency_example():
    """The given example should return {'b': 1, 'a': 3, 'n': 2}."""
    assert character_frequency("banana") == {"b": 1, "a": 3, "n": 2}


def test_character_frequency_empty_string():
    """An empty string should return an empty dictionary."""
    assert character_frequency("") == {}


def test_character_frequency_single_char():
    """A single character should return a count of 1."""
    assert character_frequency("a") == {"a": 1}


def test_character_frequency_all_same():
    """All same characters should return one key with that count."""
    assert character_frequency("aaa") == {"a": 3}


def test_character_frequency_no_repeats():
    """A string with all unique characters returns count 1 for each."""
    assert character_frequency("abc") == {"a": 1, "b": 1, "c": 1}


def test_character_frequency_spaces():
    """Spaces are counted as characters too."""
    assert character_frequency("a b") == {"a": 1, " ": 1, "b": 1}


def test_character_frequency_case_sensitive():
    """Uppercase and lowercase are treated as different characters."""
    result = character_frequency("Aa")
    assert result == {"A": 1, "a": 1}


if __name__ == "__main__":
    test_calculate_total_marks_example()
    test_calculate_total_marks_empty_dict()
    test_calculate_total_marks_single_subject()
    test_calculate_total_marks_zero_marks()
    test_calculate_total_marks_negative_marks()

    test_character_frequency_example()
    test_character_frequency_empty_string()
    test_character_frequency_single_char()
    test_character_frequency_all_same()
    test_character_frequency_no_repeats()
    test_character_frequency_spaces()
    test_character_frequency_case_sensitive()

    print("All day11-dictionaries-frequency tests passed!")