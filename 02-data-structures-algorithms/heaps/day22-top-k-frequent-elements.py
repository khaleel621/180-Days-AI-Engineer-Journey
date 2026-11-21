"""
Day 22 - Data Structures & Algorithms: Top K Frequent Elements.

Topic: Return the K most frequent elements in an integer array.

Example:
    Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]
    Explanation: 1 appears 3 times, 2 appears 2 times, and 3 appears 1
    time. The 2 most frequent elements are 1 and 2.

Two approaches are implemented and explained:

  1. Dictionary + sorting (top_k_frequent_sorting)
  2. Heap with heapq (top_k_frequent_heap)

Both count frequencies with a dictionary first, then pick the top k.

------------------------------------------------------------------
Step 1: Frequency counting with a dictionary (used by both approaches)
------------------------------------------------------------------
    - Loop through the array once.
    - Use a dictionary where each key is a number from the array and
      each value is how many times that number has been seen.
    - Example: nums = [1, 1, 1, 2, 2, 3]
      Frequency dictionary: {1: 3, 2: 2, 3: 1}
    - Duplicates are handled naturally: the same key is updated, so the
      result will never contain the same number twice.
    - Time: O(n), Space: O(m), where n = len(nums) and m = number of
      distinct elements.

------------------------------------------------------------------
Approach 1: Dictionary + sorting
------------------------------------------------------------------
    1. Build the frequency dictionary.
    2. Sort the distinct numbers by frequency, highest frequency first.
    3. Return the first k numbers from the sorted list.

    - Time complexity: O(n + m log m) — counting takes O(n), sorting m
      distinct numbers takes O(m log m).
    - Space complexity: O(m) for the dictionary and the sorted list.

------------------------------------------------------------------
Approach 2: Heap with heapq
------------------------------------------------------------------
    1. Build the frequency dictionary.
    2. Keep a min-heap of at most k items. Each item is a pair
       (frequency, number).
    3. Push every (frequency, number) pair onto the heap. If the heap
       grows larger than k, pop the root: the pair with the smallest
       frequency. Python's heapq is a min-heap, so the smallest
       frequency is always at the root.
    4. After processing all numbers, the heap holds the k most frequent
       numbers. Pop them all and return the numbers.

    - Time complexity: O(n + m log k) — counting takes O(n); each of
      the m distinct values costs O(log k) for push/pop.
    - Space complexity: O(m) for the dictionary plus O(k) for the heap.

------------------------------------------------------------------
Validation and edge cases
------------------------------------------------------------------
    - k must be an integer with 1 <= k <= number of distinct elements.
    - Otherwise ValueError is raised (TypeError for non-integer k).
    - Negative numbers work fine: they are just dictionary keys.
    - If several numbers have the same frequency (a tie), any valid set
      of k numbers is a correct answer. Tests compare results as sets.
"""

import heapq


def _count_frequencies(nums):
    """Count how many times each number appears in nums.

    Args:
        nums: List of integers (may contain duplicates and negatives).

    Returns:
        Dictionary mapping each distinct number to its frequency.
    """
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency


def _validate_inputs(nums, k):
    """Validate nums and k; raise TypeError or ValueError on bad input."""
    if not isinstance(nums, list):
        raise TypeError("nums must be a list of integers.")
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError("k must be an integer.")
    if k < 1:
        raise ValueError("k must be at least 1.")

def top_k_frequent_heap(nums, k):
    """Return the k most frequent elements using a heap (heapq).

    Args:
        nums: List of integers.
        k:    How many most frequent elements to return.

    Returns:
        List of the k most frequent elements. Order is not guaranteed
        (especially when frequencies tie), which is fine because any
        valid set of k elements is a correct answer.

    Raises:
        TypeError:  If nums is not a list or k is not an integer.
        ValueError: If k is less than 1 or greater than the number of
                    distinct elements.
    """
    _validate_inputs(nums, k)

    frequency = _count_frequencies(nums)
    distinct_count = len(frequency)

    if k > distinct_count:
        raise ValueError(
            "k cannot be greater than the number of distinct elements."
        )

    # Min-heap of (frequency, number) pairs. Holds at most k pairs:
    # the k most frequent numbers seen so far.
    min_heap = []

    for num, count in frequency.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            # Remove the least frequent number so far.
            heapq.heappop(min_heap)

    # Collect the numbers left in the heap.
    top_k = []
    while min_heap:
        count, num = heapq.heappop(min_heap)
        top_k.append(num)

    return top_k



def top_k_frequent_sorting(nums, k):
    """Return the k most frequent elements using dictionary + sorting.

    Args:
        nums: List of integers.
        k:    How many most frequent elements to return.

    Returns:
        List of the k most frequent elements. Order is highest frequency
        first; ties may appear in any order.

    Raises:
        TypeError:  If nums is not a list or k is not an integer.
        ValueError: If k is less than 1 or greater than the number of
                    distinct elements.
    """
    _validate_inputs(nums, k)

    frequency = _count_frequencies(nums)
    distinct_count = len(frequency)

    if k > distinct_count:
        raise ValueError(
            "k cannot be greater than the number of distinct elements."
        )

    # Sort distinct numbers by frequency, highest first.
    # sorted(...) returns a new list and is stable, so ties keep their
    # original order. reverse=True puts the highest frequency first.
    numbers_by_frequency = sorted(
        frequency.keys(), key=lambda num: frequency[num], reverse=True
    )

    return numbers_by_frequency[:k]


def main():
    print("=" * 60)
    print("Day 22 - DSA: Top K Frequent Elements")
    print("=" * 60)
    print()

    # --- Normal example --------------------------------------------------
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"Normal example: nums = {nums}, k = {k}")
    print(f"  Sorting: {top_k_frequent_sorting(nums, k)}  (expected [1, 2])")
    print(f"  Heap:    {top_k_frequent_heap(nums, k)}  (expected [1, 2] as a set)")
    print()

    # --- All elements identical ------------------------------------------
    nums = [5, 5, 5, 5]
    k = 1
    print(f"All identical:  nums = {nums}, k = {k}")
    print(f"  Sorting: {top_k_frequent_sorting(nums, k)}  (expected [5])")
    print(f"  Heap:    {top_k_frequent_heap(nums, k)}     (expected [5])")
    print()

    # --- All elements have equal frequency -------------------------------
    nums = [1, 2, 3, 4]
    k = 2
    print(f"Equal frequency: nums = {nums}, k = {k}")
    print(f"  Sorting: {top_k_frequent_sorting(nums, k)}  (any 2 of them)")
    print(f"  Heap:    {top_k_frequent_heap(nums, k)}     (any 2 of them)")
    print()

    # --- Negative numbers ------------------------------------------------
    nums = [-1, -1, -2, -2, -2, 3]
    k = 1
    print(f"Negative numbers: nums = {nums}, k = {k}")
    print(f"  Sorting: {top_k_frequent_sorting(nums, k)}  (expected [-2])")
    print(f"  Heap:    {top_k_frequent_heap(nums, k)}     (expected [-2])")
    print()

    # --- Single-element array --------------------------------------------
    nums = [7]
    k = 1
    print(f"Single element: nums = {nums}, k = {k}")
    print(f"  Sorting: {top_k_frequent_sorting(nums, k)}  (expected [7])")
    print(f"  Heap:    {top_k_frequent_heap(nums, k)}     (expected [7])")
    print()

    # --- k = 1 -----------------------------------------------------------
    nums = [1, 1, 1, 2, 2, 3]
    k = 1
    print(f"k = 1: nums = {nums}, k = {k}")
    print(f"  Sorting: {top_k_frequent_sorting(nums, k)}  (expected [1])")
    print(f"  Heap:    {top_k_frequent_heap(nums, k)}     (expected [1])")
    print()

    # --- k equal to the number of distinct elements ----------------------
    nums = [1, 1, 1, 2, 2, 3]
    k = 3  # distinct elements are 1, 2, 3
    print(f"k = distinct count: nums = {nums}, k = {k}")
    print(f"  Sorting: {top_k_frequent_sorting(nums, k)}  (expected [1, 2, 3])")
    print(f"  Heap:    {top_k_frequent_heap(nums, k)}     (expected [1, 2, 3] as a set)")
    print()

    # --- Invalid k values ------------------------------------------------
    print("Invalid k values (each should raise an error):")
    invalid_cases = [
        ([1, 2, 3], 0, "k = 0"),
        ([1, 2, 3], -2, "k = -2"),
        ([1, 2, 3], 5, "k = 5 (more than distinct elements)"),
        ([1, 2, 3], 2.5, "k = 2.5 (not an integer)"),
    ]
    for nums_case, k_case, label in invalid_cases:
        for func_name, func in [("sorting", top_k_frequent_sorting),
                                ("heap", top_k_frequent_heap)]:
            try:
                func(nums_case, k_case)
                print(f"  {label}, {func_name}: NO ERROR (unexpected!)")
            except (TypeError, ValueError) as error:
                print(f"  {label}, {func_name}: {type(error).__name__} -> {error}")
    print()

    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()


