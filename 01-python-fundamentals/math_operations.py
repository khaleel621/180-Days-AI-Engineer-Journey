"""
Day 14 helper module: math_operations

Topic: Modules and Packages (import, from ... import, ... as)

This small helper module provides four basic arithmetic operations so that
day14-modules-and-packages.py can demonstrate importing functions from a
custom module in three different ways:

    1. import math_operations                -> math_operations.add(a, b)
    2. from math_operations import add, subtract
    3. from math_operations import multiply as mul   (alias with `as`)

All functions are beginner-friendly and include docstrings.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return a multiplied by b."""
    return a * b


def divide(a, b):
    """
    Return a divided by b.

    Division by zero is handled clearly: instead of crashing, this function
    returns an error message string (the same beginner-friendly style used
    by safe_divide() in Day 12 exception handling).

    Args:
        a: The numerator (dividend).
        b: The denominator (divisor).

    Returns:
        The division result (a / b) if b is not zero.
        If b is zero, returns:
            "Error: division by zero is not allowed."

    Example:
        divide(10, 2)  -> 5.0
        divide(10, 0)  -> "Error: division by zero is not allowed."
    """
    if b == 0:
        # Handle division by zero clearly: return a message instead of crashing.
        return "Error: division by zero is not allowed."
    return a / b


if __name__ == "__main__":
    # Quick manual demo when run directly.
    print("add(2, 3)       =", add(2, 3))
    print("subtract(5, 2)  =", subtract(5, 2))
    print("multiply(4, 3)  =", multiply(4, 3))
    print("divide(10, 2)   =", divide(10, 2))
    print("divide(10, 0)   =", divide(10, 0))
