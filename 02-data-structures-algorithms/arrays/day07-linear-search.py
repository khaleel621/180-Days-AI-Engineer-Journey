"""
Day 7 — Data Structures & Algorithms: Searching Algorithms

Topic: Linear Search

Linear search checks every element of a list one by one, starting from
the first element, until it finds the target or reaches the end of the list.

Exercise: Search for a target number in a list.
- Use a for loop.
- Check each element one by one.
- Return the index if the target exists.
- Return -1 if the target is not found.
"""


def linear_search(numbers, target):
    """
    Search for target in numbers using linear search.

    Args:
        numbers: List of numbers to search through.
        target: The number to find.

    Returns:
        The index of target if found, otherwise -1.
    """
    # Look at every element one by one, starting from index 0.
    for index in range(len(numbers)):
        # If the current element matches the target, we found it.
        if numbers[index] == target:
            return index  # return the position immediately

    # The loop finished without finding the target.
    return -1


def main():
    numbers = [10, 20, 30, 40, 50]
    target = 30

    result = linear_search(numbers, target)

    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not found in the list")


if __name__ == "__main__":
    main()