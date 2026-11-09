# Day 12 Report - Python Exception Handling and Valid Parentheses

Date: 2026-11-09
Track: Python + DSA (Day 12 of the Python/DSA practice)
AI Engineer Journey counter: NOT advanced (remains at Day 2 model evaluation).

## Summary

Implemented and tested Day 12 of the Python + DSA practice:

1. **Python Fundamentals - Exception Handling (`try`, `except`, `else`, `finally`)**
2. **DSA - Valid Parentheses using a Stack**

All tests pass. Day 11 remains pending learner practice and is unchanged.

---

## 1. Python: Exception Handling

File: `01-python-fundamentals/day12-exception-handling.py`
Tests: `01-python-fundamentals/test_day12_exception_handling.py`

### Exercises implemented

#### `safe_divide(a, b)`

Divides `a` by `b` and handles division by zero.

- `try`: attempts `a / b`.
- `except ZeroDivisionError`: catches division by zero and returns a clear
  message (`"Error: division by zero is not allowed."`) instead of crashing.
- `else`: returns the division result when no exception occurred.
- `finally`: always runs (demonstrates cleanup intent).

Example:
- `safe_divide(10, 2)` → `5.0`
- `safe_divide(10, 0)` → `"Error: division by zero is not allowed."`

#### `convert_to_integer(value)`

Converts a value (for example a numeric string) into an integer.

- `try`: attempts `int(value)`.
- `except ValueError`: catches invalid input and returns a clear message
  (`"Error: '<value>' is not a valid integer."`) instead of crashing.
- `else`: returns the integer when conversion succeeds.
- `finally`: always runs (demonstrates cleanup intent).

Example:
- `convert_to_integer("42")` → `42`
- `convert_to_integer("-7")` → `-7`
- `convert_to_integer("0")` → `0`
- `convert_to_integer("abc")` → `"Error: 'abc' is not a valid integer."`

### Test results

`python 01-python-fundamentals/test_day12_exception_handling.py` → **all 10 tests passed**

| Test case | Result |
|-----------|--------|
| `safe_divide(10, 2)` → `5.0` | Pass |
| `safe_divide(7, 2)` → `3.5` | Pass |
| `safe_divide(-10, 2)` → `-5.0` | Pass |
| `safe_divide(10, 0)` → clear error message | Pass |
| `safe_divide(0, 5)` → `0.0` | Pass |
| `convert_to_integer("42")` → `42` | Pass |
| `convert_to_integer("-7")` → `-7` | Pass |
| `convert_to_integer("0")` → `0` | Pass |
| `convert_to_integer("abc")` → clear error message | Pass |
| `convert_to_integer("3.14")` → clear error message | Pass |

---

## 2. DSA: Valid Parentheses using a Stack

File: `02-data-structures-algorithms/stacks/day12-valid-parentheses.py`
Tests: `02-data-structures-algorithms/stacks/test_day12_valid_parentheses.py`

### Implementation

`is_valid(s)` uses a stack implemented as a Python list:

- `append()` pushes opening brackets onto the stack.
- `pop()` removes the most recently added opening bracket (LIFO) when a
  closing bracket is seen, and checks that the types match.
- A closing bracket with an empty stack → `False` (unmatched closing).
- Mismatched pair → `False`.
- Any non-bracket character → `False`.
- After processing all characters, the stack must be empty → `True`; any
  remaining opening brackets → `False`.

Supports `()`, `{}`, and `[]`. An empty string returns `True`.

No `sorted()`, no regular expressions, and no simple counting is used in
place of the stack.

### Complexity

- Time complexity: **O(n)** - every character is visited exactly once.
- Space complexity: **O(n)** - the stack may hold up to `n` opening brackets.

### Test results

`python 02-data-structures-algorithms/stacks/test_day12_valid_parentheses.py` → **all 9 tests passed**

| Expression | Expected | Result |
|------------|----------|--------|
| `"()"` | True | Pass |
| `"()[]{}"` | True | Pass |
| `"(]"` | False | Pass |
| `"([)]"` | False | Pass |
| `"{[]}"` | True | Pass |
| `"((("` | False | Pass |
| `""` | True | Pass |
| `"["` | False | Pass |
| `"]"` | False | Pass |

---

## 3. Day 11 Status (unchanged)

Day 11 files exist and their tests were verified passing:

- `01-python-fundamentals/test_day11_dictionaries_frequency.py` — all tests pass.
- `02-data-structures-algorithms/strings/test_day11_valid_anagram.py` — all tests pass.

Day 11 remains recorded as **learner practice pending** in `PROGRESS.md`.
No changes were made to Day 11 records.

---

## 4. Day 12 completion status

- Python exception handling: implemented + tests verified passing.
- DSA valid parentheses: implemented + tests verified passing.
- Learner practice: **pending** (the learner should solve the exercises
  independently before marking the day complete).

This follows the same convention used for Days 9-11: implementation and
tests are verified, while learner practice remains pending.