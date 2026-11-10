"""
Day 13 - Data Structures & Algorithms: Min Stack

Topic: Stacks

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:
- push(value)  - Push an element onto the stack.
- pop()        - Remove the element on top of the stack.
- top()        - Get the top element.
- get_min()    - Retrieve the minimum element in the stack.

Approach - two stacks:
This solution uses two stacks:

  1. `stack`      - stores all values pushed onto the stack.
  2. `min_stack`  - tracks the minimum values.

How min_stack works:
- On `push(value)`, the value is always pushed onto `stack`. It is also
  pushed onto `min_stack` when `min_stack` is empty or when `value` is
  less than or equal to the current minimum (`min_stack[-1]`). Using `<=`
  (not just `<`) correctly handles repeated minimum values.
- On `pop()`, the top value is removed from `stack`. If that value equals
  the current minimum (top of `min_stack`), it is also removed from
  `min_stack`, revealing the previous minimum.
- `top()` returns the top of `stack` without removing it.
- `get_min()` returns the top of `min_stack` without removing it.

All four operations run in O(1) time. get_min() does NOT use Python's
built-in min(); it simply reads the top of min_stack.

Empty-stack behaviour:
- pop(), top(), and get_min() return None when called on an empty stack.
  This keeps behaviour consistent and avoids raising an exception for
  everyday beginner use.

Time complexity:  O(1) for push, pop, top, and get_min.
Space complexity: O(n) - in the worst case min_stack holds up to n values
                    (for example, when values are pushed in decreasing order).
"""

# ============================================================================
# MinStack class
# ============================================================================


class MinStack:
    """A stack that supports retrieving the minimum element in O(1) time.

    Uses two stacks:
      - self.stack:      stores all values.
      - self.min_stack:  tracks minimum values (top is the current minimum).
    """

    def __init__(self):
        """Initialize an empty MinStack with two internal stacks."""
        self.stack = []      # stores all values
        self.min_stack = []  # tracks minimum values

    def push(self, value):
        """Push a value onto the stack.

        The value is always added to self.stack. It is also added to
        self.min_stack when min_stack is empty or when value is less than
        or equal to the current minimum, so min_stack[-1] is always the
        minimum of all values currently in the stack.

        Runs in O(1) time.
        """
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        """Remove and return the top value of the stack.

        If the removed value equals the current minimum, it is also removed
        from self.min_stack so the next minimum becomes visible.

        Returns:
            The popped value, or None if the stack is empty.

        Runs in O(1) time.
        """
        if not self.stack:
            # Empty stack: nothing to pop. Return None consistently.
            return None

        value = self.stack.pop()

        if self.min_stack and value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        """Return the top value of the stack without removing it.

        Returns:
            The top value, or None if the stack is empty.

        Runs in O(1) time.
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def get_min(self):
        """Return the minimum value in the stack without removing it.

        The minimum is read from the top of self.min_stack. Python's
        built-in min() is NOT used.

        Returns:
            The minimum value, or None if the stack is empty.

        Runs in O(1) time.
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]


# ============================================================================
# DEMO
# ============================================================================


def _print(label, value):
    print(f"{label:<12} -> {value!r}")


def main():
    print("=" * 60)
    print("Day 13 - DSA: Min Stack (two-stack approach)")
    print("=" * 60)
    print()

    min_stack = MinStack()

    print("--- push positive numbers ---")
    for value in [5, 3, 8, 2, 7]:
        min_stack.push(value)
        _print(f"push({value})", None)
        _print("top()", min_stack.top())
        _print("get_min()", min_stack.get_min())
        print()

    print("--- pop the current minimum (2) ---")
    _print("pop()", min_stack.pop())
    _print("top()", min_stack.top())
    _print("get_min() after popping 2", min_stack.get_min())
    print()

    print("--- push negative numbers ---")
    for value in [-4, -10, -1]:
        min_stack.push(value)
        _print(f"push({value})", None)
        _print("top()", min_stack.top())
        _print("get_min()", min_stack.get_min())
        print()

    print("--- repeated minimum values ---")
    repeated = MinStack()
    for value in [4, 4, 4]:
        repeated.push(value)
    _print("after pushing 4, 4, 4 - get_min()", repeated.get_min())
    _print("pop()", repeated.pop())
    _print("get_min() after one pop (still 4)", repeated.get_min())
    _print("pop()", repeated.pop())
    _print("get_min() after second pop (still 4)", repeated.get_min())
    print()

    print("--- empty-stack behaviour ---")
    empty = MinStack()
    _print("pop() on empty", empty.pop())
    _print("top() on empty", empty.top())
    _print("get_min() on empty", empty.get_min())
    print()

    print("=" * 60)
    print("All Min Stack demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()
