"""
Tests for Day 9 — max_profit() in
day09-best-time-to-buy-and-sell-stock.py.

Covers all examples from the problem statement plus additional edge cases:
single price, empty list, flat prices, and prices that only decrease.
"""

import importlib.util
import os

# Load day09-best-time-to-buy-and-sell-stock.py by file path so the test works
# regardless of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day09-best-time-to-buy-and-sell-stock.py")
_spec = importlib.util.spec_from_file_location("day09_best_time_to_buy_and_sell_stock", _module_path)
_day09_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day09_module)

max_profit = _day09_module.max_profit


def test_max_profit_example_1():
    """Buy at 1, sell at 6 -> profit 5."""
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_max_profit_example_2():
    """Prices only decrease -> no profit possible -> 0."""
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_max_profit_example_3():
    """Buy at 2, sell at 4 -> profit 2 (price 1 later cannot be sold at profit)."""
    assert max_profit([2, 4, 1]) == 2


def test_max_profit_single_price():
    """Only one day — cannot buy and sell on different days -> 0."""
    assert max_profit([3]) == 0


def test_max_profit_empty_list():
    """No prices — no profit possible -> 0."""
    assert max_profit([]) == 0


def test_max_profit_flat_prices():
    """Same price every day — no profit possible -> 0."""
    assert max_profit([1, 1]) == 0


def test_max_profit_two_prices_profit():
    """Buy low, sell high on the next day."""
    assert max_profit([1, 5]) == 4


def test_max_profit_two_prices_no_profit():
    """Buy high, sell low — no profit possible."""
    assert max_profit([5, 1]) == 0


def test_max_profit_negative_prices_not_applicable():
    """Stock prices are non-negative; this test documents that negative
    prices are not a valid scenario for this problem."""
    # Prices are assumed non-negative; if negatives appear, the algorithm
    # still computes a mathematical result but it is not meaningful.
    assert max_profit([0, 0]) == 0


def test_max_profit_large_gap():
    """A large price difference should be captured."""
    assert max_profit([3, 100]) == 97


def test_max_profit_profit_after_dip():
    """Buy at the lowest dip, sell at the peak after it."""
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4


if __name__ == "__main__":
    test_max_profit_example_1()
    test_max_profit_example_2()
    test_max_profit_example_3()
    test_max_profit_single_price()
    test_max_profit_empty_list()
    test_max_profit_flat_prices()
    test_max_profit_two_prices_profit()
    test_max_profit_two_prices_no_profit()
    test_max_profit_negative_prices_not_applicable()
    test_max_profit_large_gap()
    test_max_profit_profit_after_dip()

    print("All day09-best-time-to-buy-and-sell-stock tests passed!")