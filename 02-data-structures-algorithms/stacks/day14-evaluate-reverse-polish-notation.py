"""
Day 14 - Data Structures & Algorithms: Evaluate Reverse Polish Notation

Topic: Stacks

Problem:
Evaluate the value of an arithmetic expression in Reverse Polish Notation
(RPN), also known as postfix notation.

In RPN, every operator follows its operands. For example:
  - Infix:  (2 + 1) * 3
  - RPN:    ["2", "1", "+", "3", "*"]

Valid operators are +, -, * and /. Each operand may be an integer or another
expression. Division between two integers truncates toward zero.

Example:
  eval_rpn(["2","1","+","3","*"]) -> 9
  ((2 + 1) * 3) = 9

Approach - use a stack:
  1. Scan the tokens from left to right.
  2. If the token is a number, push it onto the stack.
  3. If the token is an operator (+, -, *, /):
       a. Pop the top value -> this is the RIGHT operand (b).
       b. Pop the next value -> this is the LEFT operand  (a).
          NOTE: order matters for subtraction and division. The value pushed
          earlier (a) is on the left; the value popped first (b) is on the right.
       c. Compute a operator b and push the result back onto the stack.
  4. Division truncates toward zero: int(a / b) (not a // b, which floors).
  5. After all tokens are processed, the stack holds exactly one value: the result.

Negative numbers are handled because int(token) converts strings like "-7" to -7.

This implementation does NOT use eval().

Time complexity:  O(n) - each token is processed once and each stack operation
                   is O(1).
Space complexity: O(n) - the stack can hold up to n values in the worst case
                   (when all tokens are numbers before any operator).
"""

# ============================================================================
# Evaluate Reverse Polish Notation
# ============================================================================


def eval_rpn(tokens):
    """
    Evaluate an arithmetic expression in Reverse Polish Notation.

    Args:
        tokens: A list of strings. Each string is either an integer
                operand (for example "3", "-7") or one of the operators
                "+", "-", "*", "/".

    Returns:
        The integer result of the expression.

    Example:
        eval_rpn(["2", "1", "+", "3", "*"])  -> 9
        eval_rpn(["4", "13", "5", "/", "+"]) -> 6
        eval_rpn(["-7", "2", "/"])           -> -3
    """
    stack = []  # our stack: Python list with append (push) and pop

    # The set of supported operators.
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            # ----------------------------------------------------------------
            # Operator: pop two operands and apply the operator.
            # The FIRST pop is the RIGHT operand (b); the SECOND pop is the
            # LEFT operand (a). Order matters for subtraction and division.
            # ----------------------------------------------------------------
            b = stack.pop()  # right operand (most recently pushed)
            a = stack.pop()  # left operand (pushed before b)

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:  # token == "/"
                # Division truncates toward zero.
                # a / b gives a float; int(...) truncates toward zero for both
                # positive and negative results (unlike a // b, which floors).
                result = int(a / b)

            # Push the result back onto the stack.
            stack.append(result)
        else:
            # ----------------------------------------------------------------
            # Operand: convert the string token to an integer and push it.
            # int("-7") correctly handles negative numbers.
            # ----------------------------------------------------------------
            stack.append(int(token))

    # After processing all tokens, exactly one value remains: the result.
    return stack.pop()


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 14 - DSA: Evaluate Reverse Polish Notation (Stack)")
    print("=" * 60)
    print()

    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["8", "2", "/"], 4),
        (["8", "2", "-"], 6),
        (["-7", "2", "/"], -3),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]

    for tokens, expected in test_cases:
        result = eval_rpn(list(tokens))
        status = "OK" if result == expected else "FAIL"
        print(f"eval_rpn({tokens}) = {result}  (expected {expected})  [{status}]")
        assert result == expected, f"Expected {expected}, got {result}"

    # Additional checks: multiplication, addition, negative intermediate results.
    print()
    print("--- Additional checks ---")
    print(f"eval_rpn([\"3\", \"4\", \"*\"]) = {eval_rpn(['3', '4', '*'])}   (expected 12)")
    print(f"eval_rpn([\"5\", \"8\", \"+\"]) = {eval_rpn(['5', '8', '+'])}   (expected 13)")
    print(f"eval_rpn([\"1\", \"2\", \"+\", \"3\", \"-\"]) = {eval_rpn(['1', '2', '+', '3', '-'])}   (expected 0)")
    print(f"eval_rpn([\"5\", \"1\", \"2\", \"+\", \"4\", \"*\", \"+\", \"3\", \"-\"]) = {eval_rpn(['5', '1', '2', '+', '4', '*', '+', '3', '-'])}   (expected 14)")

    print()
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()
