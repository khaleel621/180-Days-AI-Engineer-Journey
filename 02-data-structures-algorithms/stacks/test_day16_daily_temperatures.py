"""
Tests for Day 16 - Daily Temperatures in
02-data-structures-algorithms/stacks/day16-daily-temperatures.py.

Covers all required examples, equal temperatures, decreasing input, empty
input, single element, and verifies the original input list is not modified.

The implementation is loaded by file path so the tests work regardless of the
current working directory. A monotonic stack is used (no nested-loop main
solution).
"""

import importlib.util
import os

# Load day16-daily-temperatures.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day16-daily-temperatures.py")
_spec = importlib.util.spec_from_file_location("day16_daily_temperatures", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

daily_temperatures = _module.daily_temperatures


def _check(temperatures, expected):
    """Run daily_temperatures and assert result and input immutability."""
    original = list(temperatures)
    result = daily_temperatures(temperatures)
    assert result == expected, (
        f"daily_temperatures({temperatures}) = {result}, expected {expected}"
    )
    assert temperatures == original, f"Input was modified: {temperatures}"


# -----------------------------------------------------------
# Required test cases from the task
# -----------------------------------------------------------

def test_case_73_74_75_71_69_72_76_73():
    """[73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]"""
    _check([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])


def test_case_30_40_50_60():
    """[30, 40, 50, 60] -> [1, 1, 1, 0]"""
    _check([30, 40, 50, 60], [1, 1, 1, 0])


def test_case_60_50_40_30():
    """[60, 50, 40, 30] -> [0, 0, 0, 0]"""
    _check([60, 50, 40, 30], [0, 0, 0, 0])


def test_case_30_30_30():
    """[30, 30, 30] -> [0, 0, 0]"""
    _check([30, 30, 30], [0, 0, 0])


def test_case_30_35_30_40():
    """[30, 35, 30, 40] -> [1, 2, 1, 0]"""
    _check([30, 35, 30, 40], [1, 2, 1, 0])


def test_case_empty_list():
    """[] -> []"""
    _check([], [])


# -----------------------------------------------------------
# Additional checks
# -----------------------------------------------------------

def test_single_element():
    _check([70], [0])


def test_two_elements_warmer_second():
    _check([70, 80], [1, 0])


def test_two_elements_cooler_second():
    _check([80, 70], [0, 0])


def test_input_not_modified():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    original = list(temperatures)
    daily_temperatures(temperatures)
    assert temperatures == original


if __name__ == "__main__":
    test_case_73_74_75_71_69_72_76_73()
    test_case_30_40_50_60()
    test_case_60_50_40_30()
    test_case_30_30_30()
    test_case_30_35_30_40()
    test_case_empty_list()
    test_single_element()
    test_two_elements_warmer_second()
    test_two_elements_cooler_second()
    test_input_not_modified()
    print("All test_day16_daily_temperatures tests passed!")