# Day 17 Report - Python OOP (Encapsulation and Access Modifiers) and Largest Rectangle in Histogram

Date: 2026-11-15
Track: Python + DSA (Day 17 of the Python/DSA practice)
AI Engineer Journey counter: NOT advanced (remains at Day 2 model evaluation).

## Summary

Implemented and tested Day 17 of the Python + DSA practice:

1. **Python Fundamentals - OOP: Encapsulation and Access Modifiers**
   - `BankAccount(account_holder_name, account_number, initial_balance=0)`
   - Public attribute `account_holder_name`.
   - Protected attribute `_account_number` (internal by convention).
   - Private attribute `__balance` (name-mangled; direct outside access raises `AttributeError`).
   - `deposit(amount)`, `withdraw(amount)`, `get_balance()`.
   - Getter/setter for the account holder name: `get_account_holder_name()` / `set_account_holder_name()`.
   - `get_account_number()` for the protected attribute.
   - Validation: deposit/withdrawal amounts must be real numbers (bools rejected) and greater than zero; a withdrawal above the balance raises `ValueError`; account holder name and account number must be non-empty strings.

2. **DSA - Largest Rectangle in Histogram (Monotonic Stack)**
   - `largest_rectangle(heights)` using a monotonic increasing stack of indices.
   - O(n) time, O(n) extra space.
   - Handles empty input, single element, equal heights, increasing heights, decreasing heights, and mixed heights.
   - `[2, 1, 5, 6, 2, 3] -> 10`.

All Day 17 tests pass. Day 11, Day 12, Day 13, Day 14 and Day 15 remain unchanged (learner practice pending).

---

## 1. Python: Encapsulation and Access Modifiers

File: `01-python-fundamentals/day17-encapsulation.py`
Tests: `01-python-fundamentals/test_day17_encapsulation.py`

### Class implemented

#### `BankAccount(account_holder_name, account_number, initial_balance=0)`

- Stores the account holder's name (public), account number (protected) and balance (private).
- `deposit(amount)` adds money after validating the amount.
- `withdraw(amount)` removes money after validating the amount and sufficient funds.
- `get_balance()` returns the private balance (getter).

---

## 2. DSA: Largest Rectangle in Histogram (Monotonic Stack)

File: `02-data-structures-algorithms/stacks/day17-largest-rectangle.py`
Tests: `02-data-structures-algorithms/stacks/test_day17_largest_rectangle.py`

### Implementation

`largest_rectangle(heights)` uses a monotonic increasing stack (Python list with `append()`/`pop()`):

1. Walk through the bars from left to right, keeping their indices on a stack.
   The stack is monotonic increasing: bar heights at the stored indices increase from bottom to top.
2. For each bar, plus one extra sentinel bar of height 0 at the end:
   - While the stack is not empty and the current bar is lower than the bar at the stack's top index, the current bar is the right boundary for that stacked bar's tallest rectangle:
     - Pop the index from the stack. Its height is the rectangle's height.
     - The left boundary is the new stack top + 1 (all bars between are taller); if the stack is empty, the left boundary is 0.
     - The right boundary is the current index - 1.
     - `area = height * width`; keep the maximum.
   - Push the current index onto the stack.
3. Return the maximum area found.

The sentinel bar of height 0 forces every remaining bar to be popped and measured at the end. The original input list is never modified.

### Simple English explanation

Imagine each bar as a building. For every building, ask: "How wide a block of buildings can I cover if my height is limited to this building?" The answer stretches left and right until a shorter building blocks the way.

The monotonic increasing stack remembers buildings whose right boundary is still unknown. When a shorter building arrives, it is the right boundary for all taller buildings waiting on the stack, so we measure each of them and remove them. The shorter building is then pushed and waits for its own right boundary.

Because every building is pushed once and popped at most once, the whole scan is O(n) time, and the stack uses O(n) extra space.

### Complexity

- Time complexity: **O(n)** — each index is pushed once and popped at most once.
- Space complexity: **O(n)** — the stack holds up to n indices.

### Test results

`py -3.13 02-data-structures-algorithms/stacks/test_day17_largest_rectangle.py` → **all 9 tests passed**

| Test case | Result |
|-----------|--------|
| [2, 1, 5, 6, 2, 3] -> 10 | Pass |
| [] -> 0 | Pass |
| [5] -> 5 | Pass |
| [2, 2, 2] -> 6 | Pass |
| [1, 2, 3, 4] -> 6 | Pass |
| [4, 3, 2, 1] -> 6 | Pass |
| [2, 1, 2] -> 3 | Pass |
| [6, 2, 5, 4, 5, 1, 6] -> 12 | Pass |
| Input list not modified | Pass |

---

## 3. Days 11-15 Status (unchanged)

Day 11, Day 12, Day 13, Day 14 and Day 15 files exist and their tests were verified passing in earlier sessions. They remain recorded as **learner practice pending** in `PROGRESS.md`. No changes were made to Days 11-15.

---

## 4. Day 17 completion status

- Python: OOP Encapsulation and Access Modifiers (BankAccount): implemented + tests verified passing (14 tests).
- DSA: Largest Rectangle in Histogram (Monotonic Stack): implemented + tests verified passing (9 tests).
- Learner practice: **pending** (the learner should solve the exercises independently before marking the day complete).

This follows the same convention used for Days 9-16: implementation and tests are verified, while learner practice remains pending.
- `get_account_holder_name()` / `set_account_holder_name()` read and change the name with validation.
- `get_account_number()` returns the protected account number.
- Each object keeps its own data: changing one account never affects another.

### Error-handling behaviour

All invalid input raises `ValueError` with a clear message:
- `deposit(0)`, `deposit(-10)`, `deposit("100")`, `deposit(None)`, `deposit(True)` → `ValueError`
- `withdraw(0)`, `withdraw(-20)`, `withdraw("50")`, `withdraw(None)`, `withdraw(False)` → `ValueError`
- `withdraw(10000)` on a balance of 100 → `ValueError` (insufficient funds), balance unchanged
- `BankAccount("", "ACC-1")`, `BankAccount("Ada", "")` → `ValueError`
- `BankAccount("Ada", "ACC-1", -5)` → `ValueError`

### Test results

`py -3.13 01-python-fundamentals/test_day17_encapsulation.py` → **all 14 tests passed**

| Test case | Result |
|-----------|--------|
| Account stores name, number and initial balance | Pass |
| Account holder name is public | Pass |
| Default initial balance is zero | Pass |
| Deposit adds to balance | Pass |
| Invalid deposit amounts raise ValueError | Pass |
| Withdraw subtracts from balance | Pass |
| Invalid withdrawal amounts raise ValueError | Pass |
| Withdrawal above balance raises ValueError, balance unchanged | Pass |
| get_account_holder_name getter | Pass |
| set_account_holder_name setter | Pass |
| Invalid setter name raises ValueError | Pass |
| Private balance not accessible directly | Pass |
| Protected account number accessible by convention | Pass |
| Two accounts are independent | Pass |