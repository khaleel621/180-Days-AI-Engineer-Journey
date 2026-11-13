"""
Day 15 - Data Structures & Algorithms: Next Greater Element (Stack).

Topic: Stacks

Problem:
Given a list of numbers, find the next greater element to the right for every
element. The next greater element of numbers[i] is the first element to its
right that is strictly greater than numbers[i]. If no such element exists, the
result is -1.

Examples:
  [4, 5, 2, 10, 8] -> [5, 10, 10, -1, -1]
  [1, 2, 3, 4]     -> [2, 3, 4, -1]
  [4, 3, 2, 1]     -> [-1, -1, -1, -1]
  [5, 5, 5]        -> [-1, -1, -1]
  [2, 1, 3]        -> [3, 3, -1]
  []               -> []

Approach - use a stack, traversing from right to left:

  1. Create a result list filled with -1 and an empty stack.
  2. Traverse the input from right to left.
  3. For the current element, pop every stack value that is not greater than
     it (<= current). Those values can never be the next greater element for
     this element or for any element further to the left.
  4. If the stack is not empty, its top is the next greater element.
  5. Push the current element onto the stack (it may be the answer for an
     element to the left).
  6. Return the result list.

The stack stays sorted in decreasing order from bottom to top, so each element
is pushed once and popped at most once.

Duplicate values: equal values are popped (<= current), so the result is the
first STRICTLY greater element. For [5, 5, 5] every element gets -1.

The original input list is never modified: only a new result list is created.
No nested loops are used as the main solution (the inner while loop is
amortized O(1) per element because each element is popped at most once).

Time complexity:  O(n) - each element is pushed once and popped at most once.
Space complexity: O(n) - the stack and result list hold up to n elements.
"""

# ============================================================================
# Next Greater Element
# ============================================================================


def next_greater_element(numbers):
    """Return the next greater element to the right for every element.

    Args:
        numbers: A list of numbers.

    Returns:
        A list where result[i] is the first element to the right of
        numbers[i] that is strictly greater than numbers[i], or -1 if no such
        element exists. Returns an empty list for empty input. The original
        input list is not modified.

    Example:
        next_greater_element([4, 5, 2, 10, 8]) -> [5, 10, 10, -1, -1]
        next_greater_element([5, 5, 5])        -> [-1, -1, -1]
        next_greater_element([])               -> []
    """
    length = len(numbers)
    result = [-1] * length  # default: no greater element found (-1)
    stack = []  # monotonic decreasing stack of candidates to the right

    # Traverse from right to left so the stack always holds elements that are
    # to the right of the current index.
    for index in range(length - 1, -1, -1):
        current = numbers[index]

        # Remove candidates that are not greater than the current element.
        # They are useless for the current element and for every element
        # further to the left, because current is closer and at least as large.
        while stack and stack[-1] <= current:
            stack.pop()

        # The stack top (if any) is the nearest greater element to the right.
        if stack:
            result[index] = stack[-1]

        # Push the current element: it may be the next greater element for an
        # element to the left.
        stack.append(current)

    return result


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 15 - DSA: Next Greater Element (Stack)")
    print("=" * 60)
    print()

    test_cases = [
        ([4, 5, 2, 10, 8], [5, 10, 10, -1, -1]),
        ([1, 2, 3, 4], [2, 3, 4, -1]),
        ([4, 3, 2, 1], [-1, -1, -1, -1]),
        ([5, 5, 5], [-1, -1, -1]),
        ([2, 1, 3], [3, 3, -1]),
        ([], []),
        ([7], [-1]),
    ]

    for numbers, expected in test_cases:
        original = list(numbers)  # remember the input to check it is not modified
        result = next_greater_element(numbers)
        status = "OK" if result == expected else "FAIL"
        modified = " (input modified!)" if numbers != original else ""
        print(f"next_greater_element({numbers}) = {result}  (expected {expected})  [{status}]{modified}")
        assert result == expected, f"Expected {expected}, got {result}"
        assert numbers == original, f"Input was modified: {numbers}"

    print()
    print("Time complexity:  O(n)")
    print("Space complexity: O(n)")
    print()
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()