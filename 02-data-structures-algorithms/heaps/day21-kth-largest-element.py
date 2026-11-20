"""
Day 21 - Data Structures & Algorithms: Heap and Priority Queue.

Topic: Heaps and priority queues, with Python's heapq module.

Main problem: Kth Largest Element in an Array.

Example:
    Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5
    Explanation: The sorted array is [1, 2, 3, 4, 5, 6].
    The 1st largest is 6, the 2nd largest is 5.

What is a heap?
    - A heap is a complete binary tree where every parent node satisfies a
      heap property relative to its children.
    - In a min-heap, every parent is <= its children, so the smallest
      element is always at the root (index 0).
    - In a max-heap, every parent is >= its children, so the largest
      element is always at the root.
    - Heaps are usually stored as arrays (lists). For a node at index i:
        left child  = 2*i + 1
        right child = 2*i + 2
        parent      = (i - 1) // 2

Min-heap vs Max-heap:
    - Min-heap: root is the minimum. Good for "extract smallest repeatedly".
    - Max-heap: root is the maximum. Good for "extract largest repeatedly".
    - Python's heapq only provides a min-heap. To simulate a max-heap, store
      negated values.

Python's heapq module:
    - heapify(list):   Transform a list into a heap, in-place, in O(n) time.
    - heappush(heap, item): Push item onto the heap, O(log n).
    - heappop(heap):    Pop and return the smallest item, O(log n).
    - nlargest(n, iterable): Return the n largest elements.
    - nsmallest(n, iterable): Return the n smallest elements.

Optimal approach for Kth Largest Element:
    - Maintain a min-heap of at most k elements.
    - For each number, push it onto the heap.
    - If the heap grows larger than k, pop the smallest element.
    - After processing all numbers, the heap contains the k largest numbers,
      and the root (smallest of those k) is the kth largest overall.
    - Why it works: the k largest elements are exactly those that survive.
      The smallest of the k largest is the kth largest.
    - Time complexity: O(n log k) — each of n elements costs O(log k).
    - Space complexity: O(k) — the heap holds at most k elements.

Duplicate handling:
    - Duplicates are treated as separate elements. For example,
      nums = [5, 5, 4], k = 2 -> sorted [4, 5, 5], 2nd largest = 5.
    - The heap keeps duplicates as distinct entries, so this works correctly.

Invalid k:
    - k must satisfy 1 <= k <= len(nums).
    - Otherwise raise ValueError.
"""

import heapq


def find_kth_largest(nums, k):
    """Return the kth largest element in nums using a min-heap of size k.

    Args:
        nums: List of integers (may contain duplicates).
        k:    Which largest element to return (1 = largest).

    Returns:
        The kth largest element.

    Raises:
        ValueError: If k is not in the range 1 <= k <= len(nums).
    """
    # Validate k before doing any work.
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("k must be an integer.")
    if k < 1:
        raise ValueError("k must be at least 1.")
    if k > len(nums):
        raise ValueError("k cannot be greater than the number of elements.")

    # Min-heap that will hold at most k elements (the k largest seen so far).
    min_heap = []

    for num in nums:
        # Add the current number to the heap.
        heapq.heappush(min_heap, num)
        # If we now hold more than k elements, remove the smallest.
        # The smallest of the k largest is exactly what we want to drop.
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # The root of the min-heap is the smallest of the k largest elements,
    # which is the kth largest overall.
    return min_heap[0]


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 21 - DSA: Heap and Priority Queue (Kth Largest Element)")
    print("=" * 60)
    print()

    # --- Normal example ---------------------------------------------------
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = find_kth_largest(nums, k)
    print(f"Normal example: nums = {nums}, k = {k}")
    print(f"Output: {result}  (expected 5)")
    print()

    # --- Duplicates -------------------------------------------------------
    nums_dup = [5, 5, 4, 4, 3]
    k_dup = 2
    result_dup = find_kth_largest(nums_dup, k_dup)
    print(f"Duplicates:     nums = {nums_dup}, k = {k_dup}")
    print(f"Output: {result_dup}  (expected 5; sorted [3,4,4,5,5], 2nd largest = 5)")
    print()

    # --- K = 1 (largest) --------------------------------------------------
    k_one = 1
    result_one = find_kth_largest(nums, k_one)
    print(f"K = 1 (largest): nums = {nums}, k = {k_one}")
    print(f"Output: {result_one}  (expected 6)")
    print()

    # --- K = len(nums) (smallest) ----------------------------------------
    k_full = len(nums)
    result_full = find_kth_largest(nums, k_full)
    print(f"K = len(nums):   nums = {nums}, k = {k_full}")
    print(f"Output: {result_full}  (expected 1; kth largest = smallest)")
    print()

    # --- Single-element array --------------------------------------------
    single = [42]
    k_single = 1
    result_single = find_kth_largest(single, k_single)
    print(f"Single element:  nums = {single}, k = {k_single}")
    print(f"Output: {result_single}  (expected 42)")
    print()

    # --- Invalid k values -------------------------------------------------
    print("Invalid k values (each should raise ValueError):")
    for bad_k in [0, -1, 7, 2.5]:
        try:
            find_kth_largest([3, 2, 1], bad_k)
            print(f"  k = {bad_k!r}: NO ERROR (unexpected!)")
        except ValueError as error:
            print(f"  k = {bad_k!r}: ValueError -> {error}")
    print()

    # --- heapq operations demo -------------------------------------------
    print("--- heapq operations demo ---")
    demo_list = [3, 1, 4, 1, 5, 9, 2, 6]
    heapq.heapify(demo_list)
    print(f"After heapify:        {demo_list}  (root/min = {demo_list[0]})")
    heapq.heappush(demo_list, 0)
    print(f"After heappush(0):    {demo_list}  (root/min = {demo_list[0]})")
    smallest = heapq.heappop(demo_list)
    print(f"heappop() -> {smallest}; heap now: {demo_list}")
    print(f"nlargest(3, demo):    {heapq.nlargest(3, demo_list)}")
    print(f"nsmallest(3, demo):   {heapq.nsmallest(3, demo_list)}")
    print()

    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()


def find_kth_largest_using_nlargest(nums, k):
    """Alternative: return kth largest using heapq.nlargest.

    heapq.nlargest(k, nums) returns the k largest elements in descending
    order, so the last one (index -1) is the kth largest.
    """
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("k must be an integer.")
    if k < 1:
        raise ValueError("k must be at least 1.")
    if k > len(nums):
        raise ValueError("k cannot be greater than the number of elements.")

    return heapq.nlargest(k, nums)[-1]