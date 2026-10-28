"""
Day 5 — DSA: Counting Occurrences (Arrays)

Topic: Count how many times a target value appears in a list.

Algorithm: linear scan with a counter.
- Start a counter at zero.
- Look at every element once with a for loop.
- Increment the counter whenever an element equals the target.
- Return the counter after the loop finishes.

Shortcuts such as list.count() or collections.Counter are intentionally
not used, so the exercise demonstrates the counting pattern explicitly.
"""


def count_occurrences(numbers, target):
    """
    Count how many times target appears in numbers.

    Args:
        numbers: List of numbers.
        target: Value to count.

    Returns:
        The number of times target appears in numbers (0 if it never
        appears, including for an empty list).
    """
    count = 0  # initialize the counter to zero

    for number in numbers:  # examine each element once
        if number == target:
            count += 1  # increase the counter on a match

    return count  # final count after the whole list is checked


def main():
    numbers = [2, 5, 2, 8, 2, 10, 5]
    target = 2

    result = count_occurrences(numbers, target)
    print(f"{target} appears {result} times")


if __name__ == "__main__":
    main()
