"""
Day 18 - Data Structures & Algorithms: Trapping Rain Water (Two Pointers).

Topic: Two Pointers

Problem:
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water can be trapped after raining.

Example:
  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  Visual:
        █
      █ █ █
    █ █ █ █ █ █
    █ █ █ █ █ █ █ █
    ┌─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┐
    Water trapped: 6 units

Approach - Two Pointers:

  1. Start with two pointers: left at index 0, right at the last index.
  2. Track the highest bar seen so far from the left (left_max) and from the
     right (right_max). Both start at 0.
  3. While left < right:
     a. If height[left] < height[right]:
        - The left side is the limiting side. The water above height[left]
          depends only on left_max (the highest bar to its left).
        - If height[left] >= left_max, update left_max = height[left]
          (no water can sit on this bar).
        - Otherwise, water += left_max - height[left] (water sits above this
          bar, bounded by left_max on the left and some taller bar on the
          right).
        - Move left one step to the right.
     b. Else (height[left] >= height[right]):
        - Symmetric: the right side is the limiting side.
        - If height[right] >= right_max, update right_max = height[right].
        - Otherwise, water += right_max - height[right].
        - Move right one step to the left.
  4. Return the total water.

Why this works:
At each step we process the side with the smaller bar. The water level at
that bar is limited by the lower of the two maximums (left_max or right_max).
Since we always move the pointer at the smaller bar, we know the other side
has a bar at least as tall, so the water level is correctly bounded.

Time complexity:  O(n) — each index is visited at most once.
Space complexity: O(1) — only a few integer variables are used.

Simple English explanation:
  Imagine standing on the leftmost bar with a friend on the rightmost bar.
  Whoever is standing on the shorter bar looks inward: "How much water can
  sit above me?" The answer depends on the tallest bar between you and the
  edge on your side (your max) and the fact that the other side has a bar
  at least as tall as yours. So you can safely calculate your trapped water
  using only your side's max. Then you move one step inward and repeat.
  When you meet in the middle, every bar has been checked exactly once.
"""


def trap(height):
    """Calculate how much water can be trapped after raining.

    Args:
        height: A list of non-negative integers representing bar heights.

    Returns:
        The total units of water trapped. Returns 0 for empty input or
        when no water can be trapped.

    Example:
        trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) -> 6
        trap([3, 0, 2, 0, 4]) -> 11
        trap([]) -> 0
        trap([5]) -> 0
    """
    n = len(height)
    if n < 3:
        # Need at least 3 bars to trap any water.
        return 0

    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            # Left side is limiting.
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            # Right side is limiting (or equal).
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 18 - DSA: Trapping Rain Water (Two Pointers)")
    print("=" * 60)
    print()

    test_cases = [
        ([], 0),
        ([5], 0),
        ([1, 2, 3, 4], 0),
        ([4, 3, 2, 1], 0),
        ([3, 0, 2, 0, 4], 7),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ]

    for heights, expected in test_cases:
        original = list(heights)
        result = trap(heights)
        status = "OK" if result == expected else "FAIL"
        modified = " (input modified!)" if heights != original else ""
        print(
            f"trap({heights}) = {result}  (expected {expected})  [{status}]{modified}"
        )
        assert result == expected, f"Expected {expected}, got {result}"
        assert heights == original, f"Input was modified: {heights}"

    print()
    print("Time complexity:  O(n)")
    print("Space complexity: O(1)")
    print()
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()