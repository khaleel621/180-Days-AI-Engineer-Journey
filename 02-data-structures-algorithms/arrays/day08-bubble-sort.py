"""
Day 8 — Data Structures & Algorithms: Sorting Algorithms

Topic: Bubble Sort

Bubble sort repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order. This process is repeated
until the list is sorted. The largest elements "bubble up" to their
correct positions at the end of the list.

This implementation is optimized: it uses a swap flag to detect when no
swaps occurred in a full pass, meaning the list is already sorted and
the algorithm can stop early.

Exercise: Sort a list of numbers in ascending order using bubble sort.
- Use nested loops.
- Compare adjacent elements.
- Swap elements when they are in the wrong order.
- Stop early if a full pass makes no swaps (optimization).
- Return a new sorted list; the original list is NOT modified.
"""


def bubble_sort(numbers):
    """
    Sort a list of numbers in ascending order using bubble sort.

    Args:
        numbers: List of numbers to sort.

    Returns:
        A new list containing the same numbers in ascending order.
        The original list is not modified.
    """
    # Make a copy so the original list is not changed.
    sorted_nums = list(numbers)
    n = len(sorted_nums)

    # Outer loop: repeat for each element.
    # After each full pass, the largest unsorted element is in place.
    for i in range(n):
        # Track whether any swap happened in this pass.
        # If no swaps occur, the list is already sorted and we can stop.
        swapped = False

        # Inner loop: compare adjacent elements up to the last unsorted index.
        # The last i elements are already in their final positions,
        # so we only need to check up to n - i - 1.
        for j in range(0, n - i - 1):
            # If the left element is greater than the right element,
            # they are in the wrong order — swap them.
            if sorted_nums[j] > sorted_nums[j + 1]:
                sorted_nums[j], sorted_nums[j + 1] = sorted_nums[j + 1], sorted_nums[j]
                swapped = True  # remember that we made a change

        # If no elements were swapped in the inner loop,
        # the list is already sorted — exit early.
        if not swapped:
            break

    return sorted_nums


def main():
    numbers = [5, 3, 8, 1, 2]

    print("Original list:", numbers)

    sorted_numbers = bubble_sort(numbers)

    print("Sorted list:  ", sorted_numbers)

    # Show that the original list was not modified.
    print("Original after sort:", numbers)


if __name__ == "__main__":
    main()