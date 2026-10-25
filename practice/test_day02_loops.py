"""Beginner-friendly tests for the Day 2 conditions and loops exercises."""

import importlib.util
from pathlib import Path


_module_path = Path(__file__).with_name("day02_loops.py")
_spec = importlib.util.spec_from_file_location("day02_loops", _module_path)
_day02 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day02)


def test_even_and_odd_integers():
    assert _day02.even_or_odd(8) == "8 is even."
    assert _day02.even_or_odd(7) == "7 is odd."


def test_zero_and_negative_integers():
    assert _day02.even_or_odd(0) == "0 is even."
    assert _day02.even_or_odd(-4) == "-4 is even."
    assert _day02.even_or_odd(-3) == "-3 is odd."


def test_multiplication_tables_for_different_inputs():
    assert _day02.multiplication_table(3) == [
        f"3 x {multiplier} = {3 * multiplier}"
        for multiplier in range(1, 11)
    ]
    table_for_negative = _day02.multiplication_table(-2)
    assert len(table_for_negative) == 10
    assert table_for_negative[0] == "-2 x 1 = -2"
    assert table_for_negative[-1] == "-2 x 10 = -20"


def test_even_number_count_for_given_list():
    assert _day02.count_even_numbers([12, 7, 4, 9, 6, 3, 8]) == 4


def test_even_number_count_edge_cases():
    assert _day02.count_even_numbers([]) == 0
    assert _day02.count_even_numbers([2, 4, 6]) == 3
    assert _day02.count_even_numbers([1, 3, 5]) == 0


def test_multiplication_table_for_zero():
    table_for_zero = _day02.multiplication_table(0)
    assert len(table_for_zero) == 10
    assert table_for_zero == [
        f"0 x {multiplier} = {0 * multiplier}" for multiplier in range(1, 11)
    ]


def test_even_number_count_with_zero_and_negative_numbers():
    assert _day02.count_even_numbers([0, -2, -3, -4, 5]) == 3
    assert _day02.count_even_numbers([-12, -7, 0, 4]) == 3


if __name__ == "__main__":
    test_even_and_odd_integers()
    test_zero_and_negative_integers()
    test_multiplication_tables_for_different_inputs()
    test_multiplication_table_for_zero()
    test_even_number_count_for_given_list()
    test_even_number_count_edge_cases()
    test_even_number_count_with_zero_and_negative_numbers()
    print("All Day 2 conditions and loops tests passed!")
