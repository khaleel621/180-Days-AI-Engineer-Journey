"""
Day 17 - Data Structures & Algorithms: Largest Rectangle in Histogram.

Topic: Stacks — Monotonic Stack

Problem:
Given a list of bar heights (a histogram), find the area of the largest
rectangle that can be formed using consecutive bars. A rectangle spanning
several bars is limited by the shortest bar in that span.

Examples:
  largest_rectangle([2, 1, 5, 6, 2, 3]) -> 10   (bars of height 5 and 6, width 2)
  largest_rectangle([5])                  -> 5
  largest_rectangle([2, 2, 2])            -> 6   (height 2, width 3)
  largest_rectangle([1, 2, 3, 4])         -> 6
  largest_rectangle([4, 3, 2, 1])         -> 6
  largest_rectangle([])                   -> 0

Approach - monotonic increasing stack:

  1. Walk through the bars from left to right, keeping their indices on a stack.
     The stack is "monotonic increasing": the heights of the bars at the stored
     indices increase from bottom to top.

  2. For each bar (and one extra sentinel bar of height 0 at the end):
     - While the stack is not empty and the current bar is lower than the bar
       at the top of the stack, the current bar is the right boundary for the
       stacked bar's tallest rectangle:
         - Pop the index at the top. Its height is the rectangle's height.
         - The left boundary is the index now on top of the stack, plus 1
           (all bars between that index and the popped index are taller).
         - The right boundary is the current index minus 1.
         - width = right boundary - left boundary + 1.
         - area = height * width; keep the maximum area seen so far.
     - Push the current index onto the stack.

  3. Return the maximum area found.

The sentinel bar of height 0 forces every remaining bar to be popped and
measured at the end.

Each index is pushed once and popped at most once, so there are no nested
loops as the main solution — the inner while loop is amortized O(1).

Time complexity:  O(n) - each index is pushed once and popped at most once.
Space complexity: O(n) - the stack holds up to n indices.

Simple English explanation:
  Imagine each bar as a building. For every building, ask: "How wide a block
  of buildings can I cover if my height is limited to this building?" The
  answer stretches left and right until a shorter building blocks the way.

  The monotonic increasing stack remembers buildings whose right boundary is
  still unknown. When a shorter building arrives, it is the right boundary for
  all taller buildings waiting on the stack, so we measure each of them and
  remove them from the stack. The shorter building itself is then pushed and
  waits for its own right boundary.

  Because every building is pushed once and popped at most once, the whole
  scan is O(n) time, and the stack uses O(n) extra space.
"""


def largest_rectangle(heights):
    """Return the area of the largest rectangle in a histogram.

    Args:
        heights: A list of non-negative bar heights.

    Returns:
        The largest rectangle area as a number. Returns 0 for empty input.

    Example:
        largest_rectangle([2, 1, 5, 6, 2, 3]) -> 10
        largest_rectangle([]) -> 0
        largest_rectangle([5]) -> 5
    """
    stack = []  # monotonic increasing stack of bar indices
    max_area = 0

    # One extra iteration with a sentinel height of 0 flushes the stack.
    for current_index in range(len(heights) + 1):
        current_height = (
            heights[current_index] if current_index < len(heights) else 0
        )

        # The current bar is shorter than the bar at the stack top: the stack
        # top's tallest rectangle ends at the bar before the current one.
        while stack and heights[stack[-1]] > current_height:
            top_index = stack.pop()
            height = heights[top_index]

            if stack:
                # There is a shorter bar to the left (the new stack top);
                # the rectangle starts right after it.
                left_index = stack[-1] + 1
            else:
                # No shorter bar to the left: the rectangle starts at 0.
                left_index = 0

            width = current_index - left_index
            area = height * width
            if area > max_area:
                max_area = area

        # Push the current index: its right boundary is still unknown.
        stack.append(current_index)

    return max_area


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 17 - DSA: Largest Rectangle in Histogram (Monotonic Stack)")
    print("=" * 60)
    print()

    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([], 0),
        ([5], 5),
        ([2, 2, 2], 6),
        ([1, 2, 3, 4], 6),
        ([4, 3, 2, 1], 6),
        ([2, 1, 2], 3),
        ([6, 2, 5, 4, 5, 1, 6], 12),
    ]

    for heights, expected in test_cases:
        original = list(heights)  # remember the input to check immutability
        result = largest_rectangle(heights)
        status = "OK" if result == expected else "FAIL"
        modified = " (input modified!)" if heights != original else ""
        print(
            f"largest_rectangle({heights}) = {result}  "
            f"(expected {expected})  [{status}]{modified}"
        )
        assert result == expected, f"Expected {expected}, got {result}"
        assert heights == original, f"Input was modified: {heights}"

    print()
    print("Time complexity:  O(n)")
    print("Space complexity: O(n)")
    print()
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()