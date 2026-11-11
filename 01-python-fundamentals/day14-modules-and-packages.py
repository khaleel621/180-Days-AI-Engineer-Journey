"""
Day 14 - Python Fundamentals: Modules and Packages (import, from ... import, ... as)

Topic: Modules and Packages

A module is a Python file containing functions, variables, and classes that you
can reuse in other files. A package is a folder of modules. This file teaches
beginner-friendly module concepts with three exercises:

  1. calculate_circle_area(radius)
     - Uses the `math` module and `math.pi`.
     - Returns the circle's area.
     - Raises ValueError for a negative radius.

  2. generate_random_number()
     - Uses the `random` module.
     - Returns a random integer between 1 and 100.

  3. Importing functions from a custom module (`math_operations.py`)
     - `import math_operations`              -> math_operations.add(a, b)
     - `from math_operations import add, subtract`
     - `from math_operations import multiply as mul`   (alias with `as`)

Learner practice is pending - completing the exercises yourself is required
to mark this day complete.
"""

# ============================================================================
# 1. IMPORTING BUILT-IN MODULES
# ============================================================================
# `import math` gives access to mathematical constants and functions such as
# math.pi. `import random` gives access to random-number functions such as
# random.randint(a, b), which returns a random integer N such that a <= N <= b.
import math
import random

# math_operations is a custom module in this same folder
# (01-python-fundamentals/math_operations.py).
import math_operations



# ============================================================================
# EXERCISE 1: calculate_circle_area(radius)
# ============================================================================


def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Uses the math module and math.pi for the value of pi.

    Args:
        radius: The radius of the circle (must be a non-negative number).

    Returns:
        The area of the circle as a float: math.pi * radius * radius.

    Raises:
        ValueError: If the radius is negative.

    Example:
        calculate_circle_area(1)  -> 3.141592653589793
        calculate_circle_area(0)  -> 0.0
    """
    if radius < 0:
        # A circle cannot have a negative radius. Raise a clear error instead
        # of silently returning a wrong result.
        raise ValueError("Radius cannot be negative.")
    # math.pi is the mathematical constant pi (approximately 3.14159).
    return math.pi * radius * radius


# ============================================================================
# EXERCISE 2: generate_random_number()
# ============================================================================


def generate_random_number():
    """
    Generate a random integer between 1 and 100 (inclusive).

    Uses the random module's randint(a, b) function.

    Returns:
        A random integer N such that 1 <= N <= 100.

    Example:
        generate_random_number()  -> 42   (the actual value varies each run)
    """
    # random.randint(1, 100) includes both endpoints: 1 and 100 are possible.
    return random.randint(1, 100)


# ============================================================================
# EXERCISE 3: Importing functions from a custom module
# ============================================================================
# Three ways to import are demonstrated below:
#
#   1. import        -> import the whole module, then call with the module name.
#   2. from ... import -> import specific functions directly.
#   3. ... as        -> give an imported function an alias (a shorter/different name).


def demo_module_imports():
    """
    Demonstrate the three import styles using math_operations.

    Returns:
        A dictionary with the results of each demonstration so they can be
        checked programmatically as well as printed.
    """
    results = {}

    # --- Style 1: import ----------------------------------------------------
    # `import math_operations` loads the whole module. Its functions are
    # accessed with the module name as a prefix: math_operations.add(...)
    results["import_add"] = math_operations.add(10, 5)       # 15
    results["import_subtract"] = math_operations.subtract(10, 5)  # 5

    # --- Style 2: from ... import ------------------------------------------
    # `from math_operations import add, subtract` brings the named functions
    # into the current namespace so they can be called directly.
    from math_operations import add, subtract  # noqa: E402 (import inside function for demo)
    results["from_add"] = add(10, 5)       # 15
    results["from_subtract"] = subtract(10, 5)  # 5

    # --- Style 3: ... as (alias) -------------------------------------------
    # `from math_operations import multiply as mul` imports multiply but
    # gives it the alias `mul` so it can be called with a shorter name.
    from math_operations import multiply as mul  # noqa: E402
    results["as_multiply"] = mul(4, 3)     # 12

    # Divide, including the division-by-zero case handled by math_operations.
    results["divide_normal"] = math_operations.divide(10, 2)       # 5.0
    results["divide_by_zero"] = math_operations.divide(10, 0)      # error message

    return results



# ============================================================================
# 4. DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 14 - Python Fundamentals: Modules and Packages")
    print("=" * 60)
    print()

    # --- Exercise 1: circle area ---
    print("--- calculate_circle_area(radius) ---")
    for radius in [1, 5, 0]:
        try:
            area = calculate_circle_area(radius)
            print(f"calculate_circle_area({radius}) = {area}")
        except ValueError as error:
            print(f"calculate_circle_area({radius}) raised ValueError: {error}")
    # Negative radius: validation in action.
    try:
        calculate_circle_area(-3)
    except ValueError as error:
        print(f"calculate_circle_area(-3) raised ValueError: {error}")
    print()

    # --- Exercise 2: random number ---
    print("--- generate_random_number() ---")
    for _ in range(5):
        number = generate_random_number()
        # Confirm the number is within the required range (never a fixed value).
        assert 1 <= number <= 100, f"Number {number} is outside 1..100"
        print(f"generate_random_number() = {number}")
    print()

    # --- Exercise 3: importing from a custom module ---
    print("--- Importing from math_operations (import / from ... import / as) ---")
    results = demo_module_imports()
    print(f"import style:            math_operations.add(10, 5)       = {results['import_add']}")
    print(f"import style:            math_operations.subtract(10, 5)  = {results['import_subtract']}")
    print(f"from ... import style:   add(10, 5)                       = {results['from_add']}")
    print(f"from ... import style:   subtract(10, 5)                  = {results['from_subtract']}")
    print(f"as alias style:          mul(4, 3)                        = {results['as_multiply']}")
    print(f"divide(10, 2)            = {results['divide_normal']}")
    print(f"divide(10, 0)            = {results['divide_by_zero']}")
    print()

    print("=" * 60)
    print("Learner practice: complete the exercises yourself to mark Day 14 complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
