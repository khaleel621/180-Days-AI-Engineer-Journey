"""
Day 12 - Data Structures & Algorithms: Valid Parentheses using a Stack

Topic: Stacks

Problem:
Given a string s containing only the characters '(', ')', '{', '}', '[',
and ']', decide whether the string is valid.

A string is valid when all of these rules hold:
  1. Every opening bracket is closed by the same type of bracket.
  2. Opening brackets are closed in the correct order.
  3. Every closing bracket has a matching opening bracket before it.

An empty string is considered valid.

This solution uses a stack. In Python, a stack is easy to build with a list:
- append(value) pushes a value onto the top of the stack.
- pop() removes and returns the top item (Last-In, First-Out).

Only append() and pop() are used to manage the stack. No sorted(), no
regular expressions, and no simple counting replaces the stack logic.
"""

# Mapping from each closing bracket to its matching opening bracket.
MATCHING = {
    ")": "(",
    "}": "{",
    "]": "[",
}

OPENING = "({["
CLOSING = ")}]"


def is_valid(s):
    """
    Check whether brackets in s are correctly matched using a stack.

    Args:
        s: A string containing only bracket characters ((), {}, []).

    Returns:
        True if all brackets are correctly matched and nested.
        False for incorrect, unmatched, or unbalanced brackets.
        An empty string returns True.

    Example:
        is_valid("()")       -> True
        is_valid("()[]{}")   -> True
        is_valid("(]")       -> False
        is_valid("([)]")     -> False
        is_valid("{[]}")     -> True
        is_valid("(((")      -> False
        is_valid("")         -> True
        is_valid("[")        -> False
        is_valid("]")        -> False

    Time complexity:  O(n) - every character is visited exactly once.
    Space complexity: O(n) - in the worst case the stack holds all
                            opening brackets (for example "(((((").
    """
    stack = []

    for char in s:
        if char in OPENING:
            # Push opening brackets onto the stack.
            stack.append(char)
        elif char in CLOSING:
            # A closing bracket with nothing on the stack is unmatched.
            if not stack:
                return False
            # Pop the most recent opening bracket and check it matches.
            top = stack.pop()
            if MATCHING[char] != top:
                return False
        else:
            # Any character other than (){}[] is not supported.
            return False

    # Valid only if no unmatched opening brackets remain.
    return len(stack) == 0


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 12 - DSA: Valid Parentheses using a Stack")
    print("=" * 60)
    print()

    examples = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(((", False),
        ("", True),
        ("[", False),
        ("]", False),
    ]

    print(f"{'Expression':<16} {'Expected':<10} {'Result':<10} {'Status'}")
    print("-" * 60)
    all_passed = True
    for expression, expected in examples:
        result = is_valid(expression)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"{expression!r:<16} {str(expected):<10} {str(result):<10} {status}")

    print()
    print("=" * 60)
    if all_passed:
        print("All examples verified.")
    else:
        print("Some examples failed!")
    print("=" * 60)


if __name__ == "__main__":
    main()