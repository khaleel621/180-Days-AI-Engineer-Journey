"""
Day 10 — Data Structures & Algorithms: Contains Duplicate

Topic: Arrays — Duplicate Detection with Sets

Problem:
    Given a list of integers, determine whether any value appears at least twice.

Approach — Set-based:
    A set stores only unique values. As we iterate through the list,
    we add each number to a set. If a number is already in the set,
    we have found a duplicate and return True immediately. If we finish
    the loop without finding any duplicates, return False.

Time complexity: O(n) — one pass through the list.
Extra space complexity: O(n) — the set may store up to n elements.

Examples:
    contains_duplicate([1, 2, 3, 1]) -> True
    contains_duplicate([1, 2, 3, 4]) -> False
    contains_duplicate([])           -> False
    contains_duplicate([5, 5])       -> True
"""


def contains_duplicate(numbers):
    """
    Determine whether any value appears at least twice in the list.

    Uses a set to track seen values. A set stores only unique values,
    so checking membership and adding are both O(1) on average.
    When we encounter a number already in the set, a duplicate exists.

    Args:
        numbers: A list of integers.

    Returns:
        True if any value appears at least twice, False otherwise.

    Example:
        contains_duplicate([1, 2, 3, 1]) -> True
        contains_duplicate([1, 2, 3, 4]) -> False
    """
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False


def main():
    print("=" * 60)
    print("Day 10 — DSA: Contains Duplicate")
    print("=" * 60)
    print()

    examples = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([], False),
        ([5, 5], True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),
        ([-1, -2, -3, -1], True),
        ([42], False),
    ]

    print("Examples:")
    print("-" * 60)
    for numbers, expected in examples:
        result = contains_duplicate(numbers)
        status = "OK" if result == expected else "FAIL"
        print(f"  contains_duplicate({numbers}) -> {result}  (expected: {expected})  [{status}]")

    print()
    print("How it works:")
    print("  - A set stores only unique values.")
    print("  - For each number, check if it's already in the set.")
    print("  - If yes: duplicate found -> return True.")
    print("  - If no: add it to the set and continue.")
    print("  - If loop finishes: no duplicates -> return False.")
    print()
    print("Time complexity:  O(n)  — one pass through the list.")
    print("Extra space:      O(n)  — the set may hold up to n elements.")
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()