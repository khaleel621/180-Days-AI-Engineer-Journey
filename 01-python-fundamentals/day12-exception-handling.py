"""
Day 12 - Python Fundamentals: Exception Handling (try, except, else, finally)

Topic: Exception Handling

This file teaches beginner-friendly exception handling concepts with examples,
plus two practice exercises:

  1. safe_divide(a, b)
  2. convert_to_integer(value)

Learner practice is pending - completing the exercises yourself is required
to mark this day complete.
"""

# ============================================================================
# 1. WHAT IS EXCEPTION HANDLING?
# ============================================================================
# An exception is an error that happens while a program is running.
# For example, dividing by zero or converting "abc" to an integer crashes
# the program with an error message.
#
# Exception handling lets us "catch" those errors and decide what to do
# instead of letting the program crash. Python provides four blocks for this:
#
#   try:    Code that might raise an error goes here.
#   except: Code that runs only if a specific error happens in try.
#   else:   Code that runs only if NO error happened in try.
#   finally:Code that ALWAYS runs, whether or not an error happened.
#           Often used for cleanup, such as closing files.

# ============================================================================
# 2. EXERCISE 1: safe_divide(a, b)
# ============================================================================
# Divide a by b. Handle division by zero so the program does not crash.


def safe_divide(a, b):
    """
    Divide a by b and handle division by zero gracefully.

    Args:
        a: The numerator (dividend).
        b: The denominator (divisor).

    Returns:
        The division result as a float if b is not zero.
        If b is zero, returns a clear error message string instead of crashing.

    Example:
        safe_divide(10, 2)  -> 5.0
        safe_divide(10, 0)  -> "Error: division by zero is not allowed."
    """
    try:
        # This line raises ZeroDivisionError when b is 0.
        result = a / b
    except ZeroDivisionError:
        # Runs only when b is 0. Return a clear message instead of crashing.
        return "Error: division by zero is not allowed."
    else:
        # Runs only when no exception occurred: division succeeded.
        return result
    finally:
        # ALWAYS runs, whether division succeeded or failed.
        # Good place for cleanup work such as closing files.
        print(f"safe_divide({a}, {b}) finished.")


# ============================================================================
# 3. EXERCISE 2: convert_to_integer(value)
# ============================================================================
# Convert a value (for example a string like "42") into an integer.
# Handle ValueError so invalid input does not crash the program.


def convert_to_integer(value):
    """
    Convert a value into an integer and handle invalid input gracefully.

    Args:
        value: The value to convert, for example a numeric string like "42".

    Returns:
        The integer value if conversion succeeds.
        If the input cannot be converted (for example "abc"), returns a clear
        error message string instead of crashing.

    Example:
        convert_to_integer("42")  -> 42
        convert_to_integer("-7")  -> -7
        convert_to_integer("0")   -> 0
        convert_to_integer("abc") -> "Error: 'abc' is not a valid integer."
    """
    try:
        # int() raises ValueError when value is not a valid integer string.
        number = int(value)
    except ValueError:
        # Runs only when int(value) fails. Return a clear message.
        return f"Error: '{value}' is not a valid integer."
    else:
        # Runs only when conversion succeeded.
        return number
    finally:
        # ALWAYS runs, whether conversion succeeded or failed.
        print(f"convert_to_integer({value!r}) finished.")


# ============================================================================
# 4. DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 12 - Python Fundamentals: Exception Handling")
    print("=" * 60)
    print()

    # --- safe_divide: normal case ---
    print("--- safe_divide: normal division ---")
    print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")   # 5.0
    print()

    # --- safe_divide: division by zero ---
    print("--- safe_divide: division by zero ---")
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")   # error message
    print()

    # --- convert_to_integer: valid inputs ---
    print("--- convert_to_integer: valid inputs ---")
    print(f'convert_to_integer("42") = {convert_to_integer("42")}')   # 42
    print(f'convert_to_integer("-7") = {convert_to_integer("-7")}')   # -7
    print(f'convert_to_integer("0")  = {convert_to_integer("0")}')    # 0
    print()

    # --- convert_to_integer: invalid input ---
    print("--- convert_to_integer: invalid input ---")
    print(f'convert_to_integer("abc") = {convert_to_integer("abc")}')  # error message
    print()

    print("=" * 60)
    print("Learner practice: complete the exercises yourself to mark Day 12 complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()