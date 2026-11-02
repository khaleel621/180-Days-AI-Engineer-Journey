"""
Day 2 — DSA: Count Even Numbers

Count how many even numbers appear in a list using a single loop.
A number is even if number % 2 == 0.

This is a beginner-friendly DSA exercise that practices:
- Looping through a list with a for loop
- Using the modulus operator (%) to check even/odd
- Maintaining a counter variable
- Returning the final count
"""


def count_even_numbers(numbers):
    """
    Count how many even numbers are in the list.

    Args:
        numbers: List of integers.

    Returns:
        The count of even numbers (0 for an empty list).
    """
    count = 0  # start with zero even numbers found

    # Look at each number in the list one by one.
    for number in numbers:
        # A number is even if the remainder when divided by 2 is zero.
        if number % 2 == 0:
            # Increment the counter when we find an even number.
            count += 1

    # Return the total count of even numbers found.
    return count


def main():
    numbers = [12, 7, 4, 9, 6, 3, 8]
    result = count_even_numbers(numbers)
    print(f"Even numbers count: {result}")


if __name__ == "__main__":
    main()