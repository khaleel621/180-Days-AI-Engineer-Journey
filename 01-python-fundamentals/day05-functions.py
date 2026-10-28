"""
Day 5 — Python Functions

Topic: Defining and calling functions, parameters, return values,
       and the difference between print() and return.

Exercise A: Add Two Numbers
"""


def add_numbers(a, b):
    """
    Add two numbers and return their sum.

    Args:
        a: First number (int or float).
        b: Second number (int or float).

    Returns:
        The sum of a and b.
    """
    # Basic input validation: only numeric values are accepted.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float).")

    # return sends the result back to the caller; it does not print anything.
    return a + b


def main():
    # Demonstration: 10 + 20 should produce 30.
    result = add_numbers(10, 20)
    print(f"Sum: {result}")


# print() vs return:
# - print() only shows text on the screen; the function still returns None.
# - return sends a value back to the caller, so the result can be stored,
#   printed, or used in another calculation.

if __name__ == "__main__":
    main()
