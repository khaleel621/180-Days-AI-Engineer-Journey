"""
Day 16 - Data Structures & Algorithms: Daily Temperatures (Monotonic Stack).

Topic: Stacks — Monotonic Stack

Problem:
Given a list of daily temperatures, return a list where result[i] is the
number of days you have to wait after day i until a warmer temperature.
If there is no future day with a warmer temperature, result[i] is 0.

Examples:
  [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
  [30, 40, 50, 60]                 -> [1, 1, 1, 0]
  [60, 50, 40, 30]                 -> [0, 0, 0, 0]
  [30, 30, 30]                     -> [0, 0, 0]
  [30, 35, 30, 40]                 -> [1, 2, 1, 0]
  []                               -> []

Approach - monotonic stack, traversing from left to right:

  1. Create a result list filled with 0 and an empty stack.
  2. Traverse the input from left to right, keeping the current index.
  3. The stack stores indices of days whose warmer day has not been found yet.
     It is kept in decreasing order of temperature (bottom to top).
  4. For the current day, while the stack is not empty and the current
     temperature is strictly greater than the temperature at the stack's top
     index, the current day is the warmer day for that stacked day:
       - Pop the index from the stack.
       - result[popped_index] = current_index - popped_index.
  5. Push the current index onto the stack (its warmer day is still unknown).
  6. Return the result list.

Each index is pushed once and popped at most once, so there are no nested
loops as the main solution — the inner while loop is amortized O(1).

The original input list is never modified: only a new result list is created.

Time complexity:  O(n) - each index is pushed once and popped at most once.
Space complexity: O(n) - the stack and result list hold up to n entries.
"""

# ============================================================================
# Daily Temperatures
# ============================================================================


def daily_temperatures(temperatures):
    """Return the number of days until a warmer temperature for each day.

    Args:
        temperatures: A list of daily temperatures.

    Returns:
        A list where result[i] is the number of days to wait after day i
        until a warmer temperature, or 0 if no such day exists. Returns an
        empty list for empty input. The original input list is not modified.

    Example:
        daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        -> [1, 1, 4, 2, 1, 1, 0, 0]
        daily_temperatures([30, 30, 30]) -> [0, 0, 0]
        daily_temperatures([]) -> []
    """
    length = len(temperatures)
    result = [0] * length  # default: no warmer day found (0)
    stack = []  # monotonic stack of indices waiting for a warmer day

    # Traverse from left to right. The stack stores indices of days whose
    # warmer day has not been found yet, in decreasing temperature order.
    for current_index in range(length):
        current_temperature = temperatures[current_index]

        # While the current temperature is warmer than the temperature at the
        # index on top of the stack, today is the warmer day for that day.
        while stack and temperatures[stack[-1]] < current_temperature:
            previous_index = stack.pop()
            result[previous_index] = current_index - previous_index

        # Push the current index: its warmer day is still unknown.
        stack.append(current_index)

    return result


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 16 - DSA: Daily Temperatures (Monotonic Stack)")
    print("=" * 60)
    print()

    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([60, 50, 40, 30], [0, 0, 0, 0]),
        ([30, 30, 30], [0, 0, 0]),
        ([30, 35, 30, 40], [1, 2, 1, 0]),
        ([], []),
    ]

    for temperatures, expected in test_cases:
        original = list(temperatures)  # remember the input to check immutability
        result = daily_temperatures(temperatures)
        status = "OK" if result == expected else "FAIL"
        modified = " (input modified!)" if temperatures != original else ""
        print(
            f"daily_temperatures({temperatures}) = {result}  "
            f"(expected {expected})  [{status}]{modified}"
        )
        assert result == expected, f"Expected {expected}, got {result}"
        assert temperatures == original, f"Input was modified: {temperatures}"

    print()
    print("Time complexity:  O(n)")
    print("Space complexity: O(n)")
    print()
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()