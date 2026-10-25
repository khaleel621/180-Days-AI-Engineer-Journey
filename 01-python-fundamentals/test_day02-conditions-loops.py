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


_even_odd = _load("even_odd", "02-even-odd.py")
_table = _load("multiplication_table", "03-multiplication-table.py")
_count = _load("count_even_numbers", "04-count-even-numbers.py")


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


def test_even_number_count_for_given_list():
    assert _count.count_even_numbers([12, 7, 4, 9, 6, 3, 8]) == 4


def test_even_number_count_edge_cases():
    assert _count.count_even_numbers([]) == 0
    assert _count.count_even_numbers([2, 4, 6]) == 3
    assert _count.count_even_numbers([1, 3, 5]) == 0


def test_even_number_count_with_zero_and_negative_numbers():
    assert _count.count_even_numbers([0, -2, -3, -4, 5]) == 3
    assert _count.count_even_numbers([-12, -7, 0, 4]) == 3


if __name__ == "__main__":
    test_even_and_odd_integers()
    test_zero_and_negative_integers()
    test_multiplication_tables_for_different_inputs()
    test_multiplication_table_for_zero()
    test_even_number_count_for_given_list()
    test_even_number_count_edge_cases()
    test_even_number_count_with_zero_and_negative_numbers()
    print("All Day 2 conditions and loops tests passed!")