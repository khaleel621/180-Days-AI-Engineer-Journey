"""Beginner-friendly tests for the Day 2 conditions and loops exercises."""

import importlib.util
import os

_folder = os.path.dirname(__file__)


def _load(name, filename):
    path = os.path.join(_folder, filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# The even/odd exercise was moved to the DSA folder during reorganization.
_even_odd_path = os.path.normpath(
    os.path.join(_folder, "..", "02-data-structures-algorithms", "arrays", "day_02-even-odd.py")
)
_even_odd = _load("even_odd", _even_odd_path)
_table = _load("multiplication_table", "03-multiplication-table.py")


def test_even_and_odd_integers():
    assert _even_odd.even_or_odd(8) == "8 is even."
    assert _even_odd.even_or_odd(7) == "7 is odd."


def test_zero_and_negative_integers():
    assert _even_odd.even_or_odd(0) == "0 is even."
    assert _even_odd.even_or_odd(-4) == "-4 is even."
    assert _even_odd.even_or_odd(-3) == "-3 is odd."


def test_multiplication_tables_for_different_inputs():
    assert _table.multiplication_table(3) == [
        f"3 x {multiplier} = {3 * multiplier}" for multiplier in range(1, 11)
    ]
    table_for_negative = _table.multiplication_table(-2)
    assert len(table_for_negative) == 10
    assert table_for_negative[0] == "-2 x 1 = -2"
    assert table_for_negative[-1] == "-2 x 10 = -20"


def test_multiplication_table_for_zero():
    table_for_zero = _table.multiplication_table(0)
    assert len(table_for_zero) == 10
    assert table_for_zero == [
        f"0 x {multiplier} = {0 * multiplier}" for multiplier in range(1, 11)
    ]


if __name__ == "__main__":
    test_even_and_odd_integers()
    test_zero_and_negative_integers()
    test_multiplication_tables_for_different_inputs()
    test_multiplication_table_for_zero()
    print("All Day 2 conditions and loops tests passed!")
