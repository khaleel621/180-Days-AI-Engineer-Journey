"""
Tests for Day 13 - Min Stack in
02-data-structures-algorithms/stacks/day13-min-stack.py.

Covers: push positive numbers, push negative numbers, repeated minimum
values, pop the current minimum, minimum after popping, top(), empty-stack
behaviour, and a sequence of multiple operations.

All operations are expected to run in O(1) time; get_min() must NOT use
Python's built-in min().
"""

import importlib.util
import os

# Load day13-min-stack.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day13-min-stack.py")
_spec = importlib.util.spec_from_file_location("day13_min_stack", _module_path)
_min_stack_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_min_stack_module)

MinStack = _min_stack_module.MinStack


# ------------------------------------------------------------
# Push positive numbers
# ------------------------------------------------------------


def test_push_positive_numbers():
    """After pushing positive numbers, get_min() returns the smallest one."""
    stack = MinStack()
    stack.push(5)
    stack.push(3)
    stack.push(8)
    stack.push(2)
    stack.push(7)
    assert stack.get_min() == 2
    assert stack.top() == 7


def test_push_negative_numbers():
    """After pushing negative numbers, get_min() returns the most negative."""
    stack = MinStack()
    stack.push(-4)
    stack.push(-10)
    stack.push(-1)
    assert stack.get_min() == -10
    assert stack.top() == -1


def test_mixed_positive_and_negative():
    """A mix of positive and negative numbers tracks the true minimum."""
    stack = MinStack()
    stack.push(10)
    stack.push(-3)
    stack.push(5)
    assert stack.get_min() == -3


# ------------------------------------------------------------
# Repeated minimum values
# ------------------------------------------------------------


def test_repeated_minimum_values():
    """Pushing the same minimum several times keeps get_min() correct after
    each pop (uses <= so duplicates are tracked)."""
    stack = MinStack()
    stack.push(4)
    stack.push(4)
    stack.push(4)
    assert stack.get_min() == 4
    stack.pop()
    assert stack.get_min() == 4
    stack.pop()
    assert stack.get_min() == 4
    stack.pop()
    assert stack.get_min() is None


# ------------------------------------------------------------
# Pop the current minimum
# ------------------------------------------------------------


def test_pop_current_minimum_updates_min():
    """Popping the current minimum reveals the next smallest value."""
    stack = MinStack()
    stack.push(5)
    stack.push(3)
    stack.push(8)
    stack.push(2)
    stack.push(7)
    assert stack.get_min() == 2

    popped = stack.pop()  # removes 7, min stays 2
    assert popped == 7
    assert stack.get_min() == 2

    popped = stack.pop()  # removes 2 (current minimum)
    assert popped == 2
    assert stack.get_min() == 3


# ------------------------------------------------------------
# top()
# ------------------------------------------------------------


def test_top_returns_last_pushed_without_removing():
    """top() returns the most recently pushed value and leaves the stack
    unchanged."""
    stack = MinStack()
    stack.push(100)
    stack.push(200)
    assert stack.top() == 200
    assert stack.top() == 200  # top does not remove
    assert stack.get_min() == 100


# ------------------------------------------------------------
# Empty-stack behaviour
# ------------------------------------------------------------


def test_empty_stack_operations_return_none():
    """pop(), top(), and get_min() on an empty stack return None consistently
    instead of raising an exception."""
    stack = MinStack()
    assert stack.pop() is None
    assert stack.top() is None
    assert stack.get_min() is None


def test_get_min_after_popping_all_elements():
    """After popping every element, get_min() returns None."""
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.top() is None
    assert stack.get_min() is None


# ------------------------------------------------------------
# Sequence of multiple operations
# ------------------------------------------------------------


def test_sequence_of_multiple_operations():
    """A realistic sequence of pushes, pops, tops, and get_min calls."""
    stack = MinStack()

    stack.push(10)
    assert stack.get_min() == 10
    assert stack.top() == 10

    stack.push(5)
    assert stack.get_min() == 5
    assert stack.top() == 5

    stack.push(20)
    assert stack.get_min() == 5
    assert stack.top() == 20

    stack.push(5)  # repeated minimum
    assert stack.get_min() == 5

    assert stack.pop() == 5
    assert stack.get_min() == 5  # still 5 because of the duplicate

    assert stack.pop() == 20
    assert stack.get_min() == 5

    assert stack.pop() == 5
    assert stack.get_min() == 10

    assert stack.pop() == 10
    assert stack.get_min() is None
    assert stack.top() is None


if __name__ == "__main__":
    test_push_positive_numbers()
    test_push_negative_numbers()
    test_mixed_positive_and_negative()
    test_repeated_minimum_values()
    test_pop_current_minimum_updates_min()
    test_top_returns_last_pushed_without_removing()
    test_empty_stack_operations_return_none()
    test_get_min_after_popping_all_elements()
    test_sequence_of_multiple_operations()

    print("All day13-min-stack tests passed!")
