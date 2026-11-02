"""
Day 8 — Data Structures & Algorithms: Sorting Algorithms

Topic: Selection Sort

Selection sort divides the list into a sorted part (on the left) and an
unsorted part (on the right). It repeatedly finds the smallest element in
the unsorted part and swaps it into the correct position at the boundary
between the sorted and unsorted parts.

Exercise: Sort a list of numbers in ascending order using selection sort.
- Find the smallest element in the unsorted section.
- Swap it into the correct position.
- Use loops and comparisons.
- Return a new sorted list; the original list is NOT modified.
"""


def selection_sort(numbers):
    """
    Sort a list of numbers in ascending order using selection sort.

    Args:
        numbers: List of numbers to sort.

    Returns:
        A new list containing the same numbers in ascending order.
        The original list is not modified.
    """
    # Make a copy so the original list is not changed.
    sorted_nums = list(numbers)
    n = len(sorted_nums)

    # Outer loop: move the boundary between sorted and unsorted parts
    # one step to the right each time.
    for i in range(n):
        # Assume the current position holds the smallest value.
        min_index = i

        # Inner loop: scan the unsorted part (from i+1 to the end)
        # to find the actual smallest element.
        for j in range(i + 1, n):
            if sorted_nums[j] < sorted_nums[min_index]:
                # Found a new smallest element — remember its index.
                min_index = j

        # Swap the smallest found element into its correct position
        # at index i (the boundary between sorted and unsorted parts).
        # Only swap if the smallest element is not already at i.
        if min_index != i:
            sorted_nums[i], sorted_nums[min_index] = sorted_nums[min_index], sorted_nums[i]

    return sorted_nums


def main():
    numbers = [64, 25, 12, 22, 11]

    print("Original list:", numbers)

    sorted_numbers = selection_sort(numbers)

    print("Sorted list:  ", sorted_numbers)

    # Show that the original list was not modified.
    print("Original after sort:", numbers)


if __name__ == "__main__":
    main()