# Day 15 Report - Python OOP (Classes and Objects) and Next Greater Element

Date: 2026-11-13
Track: Python + DSA (Day 15 of the Python/DSA practice)
AI Engineer Journey counter: NOT advanced (remains at Day 2 model evaluation).

## Summary

Implemented and tested Day 15 of the Python + DSA practice:

1. **Python Fundamentals - Object-Oriented Programming: Classes and Objects**
   - `Student` class: `__init__`, `display_details`, `is_passed` (marks >= 40).
   - `BankAccount` class: `__init__`, `deposit`, `withdraw`, `get_balance`
     with input validation.
2. **DSA - Next Greater Element (Stack)**
   - `next_greater_element(numbers)` using a stack with right-to-left traversal.

All Day 15 tests pass. Day 11, Day 12, Day 13 and Day 14 remain unchanged
(learner practice pending).

---

## 1. Python: Classes and Objects

File: `01-python-fundamentals/day15-oop-classes-and-objects.py`
Tests: `01-python-fundamentals/test_day15_oop_classes_and_objects.py`

### Classes implemented

#### `Student(name, marks)`
- Stores the student's name and marks (instance attributes).
- `display_details()` prints the student's name and marks.
- `is_passed()` returns `True` when marks are at least 40, `False` otherwise.
- Raises `ValueError` for an empty name or marks outside 0..100.

#### `BankAccount(owner, balance)`
- Stores the account owner and the current balance.
- `deposit(amount)` adds a positive amount to the balance.
- `withdraw(amount)` removes the amount when sufficient balance exists.
- `get_balance()` returns the current balance.
- Rejects non-positive or non-numeric amounts, and withdrawals exceeding the
  balance (raises `ValueError`; balance left unchanged).
- Raises `ValueError` for an empty owner or a negative starting balance.

### Error-handling behaviour

All invalid input raises `ValueError` with a clear message:
- `Student("", 50)`, `Student("Ada", -1)`, `Student("Ada", 101)` → `ValueError`.
- `BankAccount("Ada", -5)` → `ValueError`.
- `deposit(0)`, `deposit(-10)`, `withdraw(0)`, `withdraw("50")` → `ValueError`.
- `withdraw(1000)` on a balance of 50 → `ValueError`, balance stays 50.

### Test results

`python 01-python-fundamentals/test_day15_oop_classes_and_objects.py` → **all 17 tests passed**

| Test case | Result |
|-----------|--------|
| Student stores name and marks | Pass |
| display_details prints name and marks | Pass |
| is_passed True for marks >= 40 (incl. boundary 40) | Pass |
| is_passed False for marks < 40 | Pass |
| Marks can be a float | Pass |
| Different students are independent | Pass |
| Invalid student name raises ValueError | Pass |
| Invalid student marks raises ValueError | Pass |
| BankAccount stores owner and balance | Pass |
| get_balance returns current balance | Pass |
| Positive deposit increases balance | Pass |
| Multiple deposits accumulate | Pass |
| Successful withdrawal reduces balance | Pass |
| Withdrawing the entire balance leaves zero | Pass |
| Insufficient balance raises ValueError, balance unchanged | Pass |
| Invalid deposit amounts raise ValueError, balance unchanged | Pass |
| Invalid withdrawal amounts raise ValueError, balance unchanged | Pass |
| Negative initial balance raises ValueError | Pass |
| Invalid owner raises ValueError | Pass |
| Two accounts are independent | Pass |

---

## 2. DSA: Next Greater Element (Stack)

File: `02-data-structures-algorithms/stacks/day15-next-greater-element.py`
Tests: `02-data-structures-algorithms/stacks/test_day15_next_greater_element.py`

### Implementation

`next_greater_element(numbers)` uses a stack (Python list with `append()`/`pop()`):

1. Create a result list filled with `-1` and an empty stack.
2. Traverse the input from right to left.
3. For the current element, pop every stack value that is not greater than it
   (`<= current`). Those values can never be the answer for this element or
   for any element further to the left.
4. If the stack is not empty, its top is the next greater element.
5. Push the current element onto the stack.
6. Return the result list.

The stack stays in decreasing order from bottom to top, so each element is
pushed once and popped at most once — no nested-loop main solution.

Duplicate values are handled correctly: equal values are popped, so the
result is the first **strictly** greater element (`[5, 5, 5] -> [-1, -1, -1]`).

The original input list is never modified — only a new result list is created.

### Complexity

- Time complexity: **O(n)** — each element is pushed once and popped at most
  once.
- Space complexity: **O(n)** — the stack and result list hold up to n
  elements.

### Test results

`python 02-data-structures-algorithms/stacks/test_day15_next_greater_element.py` → **all 11 tests passed**

| Test case | Result |
|-----------|--------|
| [4, 5, 2, 10, 8] -> [5, 10, 10, -1, -1] | Pass |
| [1, 2, 3, 4] -> [2, 3, 4, -1] | Pass |
| [4, 3, 2, 1] -> [-1, -1, -1, -1] | Pass |
| [5, 5, 5] -> [-1, -1, -1] (duplicates) | Pass |
| [2, 1, 3] -> [3, 3, -1] | Pass |
| [] -> [] | Pass |
| Single element [7] -> [-1] | Pass |
| Two increasing elements [3, 7] -> [7, -1] | Pass |
| Two decreasing elements [7, 3] -> [-1, -1] | Pass |
| Negative numbers [-3, -1, -2] | Pass |
| Original input not modified | Pass |

---

## 3. Days 11-14 Status (unchanged)

Day 11, Day 12, Day 13 and Day 14 files exist and their tests were verified
passing in earlier sessions. They remain recorded as **learner practice
pending** in `PROGRESS.md`. No changes were made to Days 11-14.

---

## 4. Day 15 completion status

- Python OOP (Classes and Objects): implemented + tests verified passing (17 tests).
- DSA Next Greater Element (Stack): implemented + tests verified passing (11 tests).
- Learner practice: **pending** (the learner should solve the exercises
  independently before marking the day complete).

This follows the same convention used for Days 9-14: implementation and tests
are verified, while learner practice remains pending.