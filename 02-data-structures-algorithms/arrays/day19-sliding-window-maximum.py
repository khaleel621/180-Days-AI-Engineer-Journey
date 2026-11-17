"""
Day 19 - Data Structures & Algorithms: Sliding Window Maximum.

Topic: Sliding Window — using a deque to find the maximum in every window.

Problem:
Given a list of numbers and a window size k, return a list containing the
maximum value of each contiguous subarray (window) of size k.

Examples:
  max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) -> [3, 3, 5, 5, 6, 7]
  max_sliding_window([1, 2, 3, 4, 5], 2)              -> [2, 3, 4, 5]
  max_sliding_window([5, 5, 5, 5], 2)                 -> [5, 5, 5]
  max_sliding_window([7], 1)                          -> [7]
  max_sliding_window([9, -1, 4], 2)                   -> [9, 4]

Approach — monotonic deque of indices:

  1. Validate input:
     - If k is not a positive integer, raise ValueError.
     - If k is larger than the list length, raise ValueError.
     - If the input list is empty, return an empty list.

  2. Use collections.deque to store indices (not values).
     The deque maintains indices of elements in decreasing order of their
     values, so the front always holds the index of the current window's
     maximum.

  3. For each index i in the list:
     - Remove indices from the front that are outside the current window
       (index <= i - k).
     - Remove indices from the back while their values are less than the
       current value (they can never be the maximum while the current
       element is in the window).
     - Append the current index i to the deque.
     - Once the first full window is formed (i >= k - 1), the value at the
       front of the deque is the maximum for that window.

  4. Return the list of maximums.

Time complexity:  O(n) — each index is added and removed at most once.
Space complexity: O(k) — the deque holds at most k indices.
"""

# ============================================================================
# Imports
# ============================================================================

from collections import deque

# ============================================================================
# Solution
# ============================================================================


def max_sliding_window(numbers, k):
    """Return the maximum of each sliding window of size k over numbers.

    Args:
        numbers: A list of numbers.
        k: The window size (must be a positive integer <= len(numbers)).

    Returns:
        A list of maximums, one for each window.

    Raises:
        ValueError: If k is not a positive integer, or if k is larger than
            the length of numbers.
    """
    # --- Handle empty input -------------------------------------------------
    if not numbers:
        return []

    # --- Validate window size ----------------------------------------------
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("k must be an integer")
    if k <= 0:
        raise ValueError("k must be a positive integer")
    if k > len(numbers):
        raise ValueError("k cannot be larger than the length of numbers")

    # --- Monotonic deque of indices ----------------------------------------
    # The deque stores indices of elements in decreasing order of value.
    # The front (leftmost) index always corresponds to the current window's
    # maximum element.
    window = deque()
    result = []

    for i in range(len(numbers)):
        # Remove indices that are outside the current window.
        # The current window covers indices [i - k + 1, i].
        # Any index <= i - k is outside and must be removed from the front.
        while window and window[0] <= i - k:
            window.popleft()

        # Remove indices from the back whose values are less than the
        # current value. They cannot be the maximum while the current
        # element is in the window (and the current element will stay in
        # the window longer than they will).
        while window and numbers[window[-1]] < numbers[i]:
            window.pop()

        # Add the current index to the deque.
        window.append(i)

        # Once we have processed at least k elements, the front of the
        # deque holds the index of the maximum for the current window.
        if i >= k - 1:
            result.append(numbers[window[0]])

    return result


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 19 - DSA: Sliding Window Maximum (Monotonic Deque)")
    print("=" * 60)
    print()

    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1, 2, 3, 4, 5], 2, [2, 3, 4, 5]),
        ([5, 5, 5, 5], 2, [5, 5, 5]),
        ([7], 1, [7]),
        ([9, -1, 4], 2, [9, 4]),
    ]

    for numbers, k, expected in test_cases:
        result = max_sliding_window(numbers, k)
        status = "OK" if result == expected else "FAIL"
        print(
            f"max_sliding_window({numbers}, k={k}) = {result}  "
            f"(expected {expected})  [{status}]"
        )
        assert result == expected, f"Expected {expected}, got {result}"

    print()

    # --- Invalid window sizes ---
    print("--- Invalid window sizes (ValueError) ---")
    for bad_k in [0, -1, 10]:
        try:
            max_sliding_window([1, 2, 3], bad_k)
        except ValueError as error:
            print(f"k={bad_k}: ValueError - {error}")

    # --- Empty input ---
    print()
    print("--- Empty input ---")
    print(f"max_sliding_window([], 3) = {max_sliding_window([], 3)}")

    print()
    print("Time complexity:  O(n)")
    print("Space complexity: O(k)")
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()