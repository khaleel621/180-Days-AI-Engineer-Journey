"""
Day 7 — Data Structures & Algorithms: Searching Algorithms

Topic: Binary Search

Binary search finds a target in a SORTED list by repeatedly dividing the
search range in half.

IMPORTANT: Binary search only works on a sorted list. If the list is not
sorted, the result may be wrong even if the target exists in the list.

Algorithm:
- Start with low = 0 and high = last index of the list.
- While low is less than or equal to high:
    - Compute mid = (low + high) // 2 (the middle index).
    - If numbers[mid] == target, return mid.
    - If numbers[mid] < target, the target can only be on the right side,
      so move low to mid + 1.
    - If numbers[mid] > target, the target can only be on the left side,
      so move high to mid - 1.
- If the loop ends, the target is not in the list; return -1.
"""


def binary_search(numbers, target):
    """
    Search for target in a sorted list of numbers using binary search.

    Args:
        numbers: A sorted list of numbers (ascending order).
        target: The number to find.

    Returns:
        The index of target if found, otherwise -1.
    """
    low = 0  # start of the search range
    high = len(numbers) - 1  # end of the search range

    # Keep searching while the range is valid.
    while low <= high:
        mid = (low + high) // 2  # middle index of the current range

        if numbers[mid] == target:
            return mid  # target found at the middle

        if numbers[mid] < target:
            # Target is greater than the middle element.
            # Discard the left half including mid.
            low = mid + 1
        else:
            # Target is smaller than the middle element.
            # Discard the right half including mid.
            high = mid - 1

    # The range is empty and the target was never found.
    return -1


def main():
    numbers = [10, 20, 30, 40, 50, 60, 70]
    target = 50

    result = binary_search(numbers, target)

    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not found in the list")


if __name__ == "__main__":
    main()