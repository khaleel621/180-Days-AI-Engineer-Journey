"""
Tests for Day 14 - Modules and Packages in
01-python-fundamentals/day14-modules-and-packages.py.

Covers:
  - calculate_circle_area(): positive radius, zero radius, negative radius
                             (ValueError), and use of math.pi.
  - generate_random_number(): result is always within 1..100 (the exact value
                              is intentionally never asserted).
  - Importing from the custom module math_operations: import style,
    from ... import style, and as alias style, plus division by zero.

The helper module math_operations.py is loaded by file path so the tests work
regardless of the current working directory.
"""

import importlib.util
import math
import os
import random

# ---------------------------------------------------------------------------
# Load the two modules by file path.
# ---------------------------------------------------------------------------
_module_dir = os.path.dirname(__file__)

_day14_path = os.path.join(_module_dir, "day14-modules-and-packages.py")
_day14_spec = importlib.util.spec_from_file_location("day14_modules_and_packages", _day14_path)
_day14_module = importlib.util.module_from_spec(_day14_spec)
_day14_spec.loader.exec_module(_day14_module)

calculate_circle_area = _day14_module.calculate_circle_area
generate_random_number = _day14_module.generate_random_number
demo_module_imports = _day14_module.demo_module_imports

_helper_path = os.path.join(_module_dir, "math_operations.py")
_helper_spec = importlib.util.spec_from_file_location("math_operations", _helper_path)
_helper_module = importlib.util.module_from_spec(_helper_spec)
_helper_spec.loader.exec_module(_helper_module)

add = _helper_module.add
subtract = _helper_module.subtract
multiply = _helper_module.multiply
divide = _helper_module.divide


# ---------------------------------------------------------------------------
# calculate_circle_area tests
# ---------------------------------------------------------------------------

def test_circle_area_positive_radius():
    """Area for a positive radius equals math.pi * radius * radius."""
    radius = 5
    expected = math.pi * radius * radius
    assert calculate_circle_area(radius) == expected


def test_circle_area_unit_radius():
    """Area for radius 1 equals math.pi."""
    assert calculate_circle_area(1) == math.pi


def test_circle_area_zero_radius():
    """Area for a zero radius is 0.0."""
    assert calculate_circle_area(0) == 0.0


def test_circle_area_negative_radius():
    """A negative radius raises ValueError (input validation)."""
    try:
        calculate_circle_area(-3)
    except ValueError:
        pass
    else:
        raise AssertionError("calculate_circle_area(-3) did not raise ValueError")


# ---------------------------------------------------------------------------
# generate_random_number tests
# ---------------------------------------------------------------------------

def test_random_number_is_in_range():
    """generate_random_number() always returns an integer between 1 and 100."""
    for _ in range(100):
        number = generate_random_number()
        assert isinstance(number, int)
        assert 1 <= number <= 100


def test_random_number_not_fixed():
    """The result should not depend on one particular random number."""
    numbers = {generate_random_number() for _ in range(50)}
    # With 50 draws from 1..100, we expect more than one distinct value
    # (extremely unlikely to fail unless random is broken).
    assert len(numbers) > 1


# ---------------------------------------------------------------------------
# math_operations import-style tests
# ---------------------------------------------------------------------------

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6


def test_divide_normal():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    """Division by zero returns a clear error message instead of crashing."""
    result = divide(10, 0)
    assert isinstance(result, str)
    assert "division by zero" in result.lower()


# ---------------------------------------------------------------------------
# Import style demonstrations (import / from ... import / as)
# ---------------------------------------------------------------------------

def test_demo_module_imports_uses_all_styles():
    """demo_module_imports() returns correct results for every import style."""
    results = demo_module_imports()
    assert results["import_add"] == 15
    assert results["import_subtract"] == 5
    assert results["from_add"] == 15
    assert results["from_subtract"] == 5
    assert results["as_multiply"] == 12
    assert results["divide_normal"] == 5.0
    assert "division by zero" in results["divide_by_zero"].lower()


if __name__ == "__main__":
    test_circle_area_positive_radius()
    test_circle_area_unit_radius()
    test_circle_area_zero_radius()
    test_circle_area_negative_radius()

    test_random_number_is_in_range()
    test_random_number_not_fixed()

    test_add()
    test_subtract()
    test_multiply()
    test_divide_normal()
    test_divide_by_zero()

    test_demo_module_imports_uses_all_styles()

    print("All day14-modules-and-packages tests passed!")
