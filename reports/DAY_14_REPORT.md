# Day 14 Report - Python Modules and Packages and Reverse Polish Notation

Date: 2026-11-11
Track: Python + DSA (Day 14 of the Python/DSA practice)
AI Engineer Journey counter: NOT advanced (remains at Day 2 model evaluation).

## Summary

Implemented and tested Day 14 of the Python + DSA practice:

1. **Python Fundamentals - Modules and Packages (import, from ... import, ... as)**
2. **DSA - Evaluate Reverse Polish Notation (Stack)**

All Day 14 tests pass. Day 11, Day 12 and Day 13 remain unchanged (learner practice pending).

---

## 1. Python: Modules and Packages

File: `01-python-fundamentals/day14-modules-and-packages.py`
Tests: `01-python-fundamentals/test_day14_modules_and_packages.py`
Helper module: `01-python-fundamentals/math_operations.py`

### Exercises implemented

#### `calculate_circle_area(radius)`
Uses the `math` module and `math.pi`, returning `math.pi * radius * radius`.
Raises `ValueError` for a negative radius.

#### `generate_random_number()`
Uses the `random` module and `random.randint(1, 100)`, returning a random
integer between 1 and 100.

#### Importing from a custom module
`math_operations.py` provides `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`
and `divide(a, b)`. `divide` handles division by zero clearly (returns an
error message instead of crashing). `day14-modules-and-packages.py` demonstrates
all three import styles:
- `import math_operations` → `math_operations.add(10, 5)`
- `from math_operations import add, subtract`
- `from math_operations import multiply as mul` (alias using `as`)

### Test results

`python 01-python-fundamentals/test_day14_modules_and_packages.py` → **all 12 tests passed**

| Test case | Result |
|-----------|--------|
| Circle area for positive radius equals math.pi * radius * radius | Pass |
| Circle area for radius 1 equals math.pi | Pass |
| Circle area for zero radius is 0.0 | Pass |
| Negative radius raises ValueError | Pass |
| Random number is an integer in 1..100 | Pass |
| Random number is not a fixed value | Pass |
| add() | Pass |
| subtract() | Pass |
| multiply() | Pass |
| divide() normal cases | Pass |
| divide() by zero returns clear error message | Pass |
| All three import styles produce correct results | Pass |

---

## 2. DSA: Evaluate Reverse Polish Notation

File: `02-data-structures-algorithms/stacks/day14-evaluate-reverse-polish-notation.py`
Tests: `02-data-structures-algorithms/stacks/test_day14_evaluate_reverse_polish_notation.py`

### Implementation

`eval_rpn(tokens)` uses a stack (Python list):

- Scan tokens left to right.
- Number token → push `int(token)` onto the stack (handles negatives like "-7").
- Operator token → pop the right operand first, then the left operand, apply
  the operator, and push the result. Operand order matters for `-` and `/`.
- Division truncates toward zero via `int(a / b)` (not `a // b`, which floors
  toward negative infinity).
- `eval()` is NOT used.
- After all tokens are processed, the last value on the stack is the result.

### Complexity

- Time complexity: **O(n)** — each token is processed once; stack operations
  are O(1).
- Space complexity: **O(n)** — the stack may hold up to n values.

### Test results

`python 02-data-structures-algorithms/stacks/test_day14_evaluate_reverse_polish_notation.py` → **all 11 tests passed**

| Test case | Result |
|-----------|--------|
| ["2","1","+","3","*"] → 9 | Pass |
| ["4","13","5","/","+"] → 6 | Pass |
| ["8","2","/"] → 4 | Pass |
| ["8","2","-"] → 6 | Pass |
| ["-7","2","/"] → -3 | Pass |
| Complex expression → 22 | Pass |
| Multiplication (incl. negatives) | Pass |
| Addition (incl. negatives) | Pass |
| Negative intermediate results | Pass |
| Division truncates toward zero (4 sign combinations) | Pass |
| Single operand | Pass |

---

## 3. Day 11, Day 12 and Day 13 Status (unchanged)

Day 11, Day 12 and Day 13 files exist and their tests were verified passing:

- Python Day 11 dictionaries/frequency: `test_day11_dictionaries_frequency.py` passes.
- DSA Day 11 valid anagram: `test_day11_valid_anagram.py` passes.
- Python Day 12 exception handling: `test_day12_exception_handling.py` passes.
- DSA Day 12 valid parentheses: `test_day12_valid_parentheses.py` passes.
- Python Day 13 file handling: `test_day13_file_handling.py` passes.
- DSA Day 13 min stack: `test_day13_min_stack.py` passes.

Day 11, Day 12 and Day 13 remain recorded as **learner practice pending** in
`PROGRESS.md`. No changes were made to Day 11, Day 12 or Day 13 records.

---

## 4. Day 14 completion status

- Python modules and packages: implemented + tests verified passing (12 tests).
- DSA Reverse Polish Notation: implemented + tests verified passing (11 tests).
- Learner practice: **pending** (the learner should solve the exercises
  independently before marking the day complete).

This follows the same convention used for Days 9-13: implementation and tests
are verified, while learner practice remains pending.
