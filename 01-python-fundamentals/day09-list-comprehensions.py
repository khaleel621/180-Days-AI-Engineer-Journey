"""
Day 9 — Python Fundamentals: List Comprehensions

Topic: List Comprehensions

A list comprehension is a concise way to create a new list by applying an
expression to each item in an existing iterable (for example, a list), with
an optional condition to filter items.

General syntax:
    [expression for item in iterable if condition]

Examples:
    [x * x for x in [1, 2, 3, 4]]          -> [1, 4, 9, 16]
    [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]  -> [2, 4, 6]

Rules for this exercise:
- Use list comprehensions (not map() or filter()).
- Do not modify the original input list.
- Return a new list.
"""


def square_numbers(numbers):
    """
    Return a new list containing the square of every number in the input.

    Uses a list comprehension: [x * x for x in numbers].

    Args:
        numbers: A list of numbers.

    Returns:
        A new list where each element is the square of the corresponding
        element in the input list. The original list is not modified.

    Example:
        square_numbers([1, 2, 3, 4]) -> [1, 4, 9, 16]
    """
    return [x * x for x in numbers]


def filter_even_numbers(numbers):
    """
    Return a new list containing only the even numbers from the input.

    Uses a list comprehension with an if condition:
    [x for x in numbers if x % 2 == 0].

    Args:
        numbers: A list of numbers.

    Returns:
        A new list containing only the even numbers from the input,
        in the same order. The original list is not modified.

    Example:
        filter_even_numbers([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
    """
    return [x for x in numbers if x % 2 == 0]


def main():
    # Demonstration of square_numbers
    nums = [1, 2, 3, 4]
    print("square_numbers example:")
    print(f"  Input:  {nums}")
    print(f"  Output: {square_numbers(nums)}")
    print(f"  Original after call: {nums} (unchanged)")
    print()

    # Demonstration of filter_even_numbers
    nums2 = [1, 2, 3, 4, 5, 6]
    print("filter_even_numbers example:")
    print(f"  Input:  {nums2}")
    print(f"  Output: {filter_even_numbers(nums2)}")
    print(f"  Original after call: {nums2} (unchanged)")


if __name__ == "__main__":
    main()