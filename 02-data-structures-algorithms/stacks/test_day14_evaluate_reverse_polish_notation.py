"""
Tests for Day 14 - Evaluate Reverse Polish Notation in
02-data-structures-algorithms/stacks/day14-evaluate-reverse-polish-notation.py.

Covers all required test cases plus multiplication, addition, and negative
intermediate results. Division truncates toward zero; negative numbers and
negative intermediate results are handled.

The implementation is loaded by file path so the tests work regardless of the
current working directory. eval() is NOT used in the solution.
"""

import importlib.util
import os

# Load day14-evaluate-reverse-polish-notation.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day14-evaluate-reverse-polish-notation.py")
_spec = importlib.util.spec_from_file_location("day14_evaluate_rpn", _module_path)
_rpn_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_rpn_module)

eval_rpn = _rpn_module.eval_rpn


def _check(tokens, expected):
    """Helper: evaluate tokens and assert the result equals expected."""
    result = eval_rpn(list(tokens))
    assert result == expected, f"eval_rpn({tokens}) = {result}, expected {expected}"


# ------------------------------------------------------------
# Required test cases from the task
# ------------------------------------------------------------

def test_case_2_1_plus_3_multiply():
    """["2","1","+","3","*"] -> 9 : (2 + 1) * 3 = 9"""
    _check(["2", "1", "+", "3", "*"], 9)


def test_case_4_13_5_divide_plus():
    """["4","13","5","/","+"] -> 6 : 4 + (13 / 5 truncated to 2) = 6"""
    _check(["4", "13", "5", "/", "+"], 6)


def test_case_8_2_divide():
    """["8","2","/"] -> 4"""
    _check(["8", "2", "/"], 4)


def test_case_8_2_subtract():
    """["8","2","-"] -> 6 : operand order matters (8 - 2)"""
    _check(["8", "2", "-"], 6)


def test_case_negative_7_2_divide():
    """["-7","2","/"] -> -3 : truncation toward zero (-3.5 -> -3, not -4)"""
    _check(["-7", "2", "/"], -3)


def test_case_complex_expression():
    """["10","6","9","3","+","-11","*","/","*","17","+","5","+"] -> 22"""
    _check(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)


# ------------------------------------------------------------
# Additional checks: multiplication, addition, negatives
# ------------------------------------------------------------

def test_multiplication():
    _check(["3", "4", "*"], 12)
    _check(["-2", "3", "*"], -6)
    _check(["-2", "-3", "*"], 6)


def test_addition():
    _check(["5", "8", "+"], 13)
    _check(["-5", "8", "+"], 3)
    _check(["-5", "-8", "+"], -13)


def test_negative_intermediate_results():
    """Negative intermediate results are handled correctly."""
    # 1 + 2 = 3; 3 - 3 = 0
    _check(["1", "2", "+", "3", "-"], 0)
    # 5 + ((1 + 2) * 4) - 3 = 5 + 12 - 3 = 14
    _check(["5", "1", "2", "+", "4", "*", "+", "3", "-"], 14)
    # 7 - 10 = -3 (negative intermediate result)
    _check(["7", "10", "-"], -3)


def test_division_truncates_toward_zero():
    """Division truncates toward zero for both positive and negative results."""
    # 7 / 2 = 3.5 -> 3
    _check(["7", "2", "/"], 3)
    # -7 / 2 = -3.5 -> -3 (not -4)
    _check(["-7", "2", "/"], -3)
    # 7 / -2 = -3.5 -> -3
    _check(["7", "-2", "/"], -3)
    # -7 / -2 = 3.5 -> 3
    _check(["-7", "-2", "/"], 3)


def test_single_number():
    """A single operand with no operators returns that number."""
    _check(["42"], 42)
    _check(["-42"], -42)


if __name__ == "__main__":
    test_case_2_1_plus_3_multiply()
    test_case_4_13_5_divide_plus()
    test_case_8_2_divide()
    test_case_8_2_subtract()
    test_case_negative_7_2_divide()
    test_case_complex_expression()

    test_multiplication()
    test_addition()
    test_negative_intermediate_results()
    test_division_truncates_toward_zero()
    test_single_number()

    print("All day14-evaluate-reverse-polish-notation tests passed!")
