# Day 13 Report - Python File Handling and Min Stack

Date: 2026-11-10
Track: Python + DSA (Day 13 of the Python/DSA practice)
AI Engineer Journey counter: NOT advanced (remains at Day 2 model evaluation).

## Summary

Implemented and tested Day 13 of the Python + DSA practice:

1. **Python Fundamentals - File Handling (Read, Write, Append)**
2. **DSA - Min Stack (two-stack approach)**

All Day 13 tests pass. Day 11 and Day 12 remain unchanged (learner practice pending).

---

## 1. Python: File Handling

File: `01-python-fundamentals/day13-file-handling.py`
Tests: `01-python-fundamentals/test_day13_file_handling.py`

### Exercises implemented

#### `save_student_details(filename, name, marks)`

Writes a student's name and marks to a file using `with open()` in write mode (`"w"`).

- Write mode creates the file if it does not exist and overwrites any existing content.
- The `with` statement ensures the file is closed automatically.

Example:
- `save_student_details("student.txt", "Alice", 85)` writes:
  ```
  Student Details
  Name: Alice
  Marks: 85
  ```

#### `read_file(filename)`

Reads and returns the complete content of a file using `with open()` in read mode (`"r"`).

- Handles `FileNotFoundError` gracefully: returns a clear error message
  (`"Error: file '<filename>' not found."`) instead of crashing.

#### `append_student_subject(filename, subject)`

Appends a subject to the end of a file using `with open()` in append mode (`"a"`).

- Append mode adds content to the end of the file without overwriting existing content.
- Confirmed that previous content remains after appending.

### Test results

`python 01-python-fundamentals/test_day13_file_handling.py` → **all 7 tests passed**

| Test case | Result |
|-----------|--------|
| Write student details, read back name and marks | Pass |
| Write mode overwrites existing content | Pass |
| Read existing file returns complete content | Pass |
| Read missing file returns clear error message | Pass |
| Append a subject to the file | Pass |
| Appending preserves previous content | Pass |
| Append to an empty file | Pass |

Temporary files are used in all tests, so no existing user files are modified.

---

## 2. DSA: Min Stack

File: `02-data-structures-algorithms/stacks/day13-min-stack.py`
Tests: `02-data-structures-algorithms/stacks/test_day13_min_stack.py`

### Implementation

`MinStack` uses two stacks:

- `self.stack` — stores all values pushed onto the stack.
- `self.min_stack` — tracks minimum values; its top is always the current minimum.

How it works:

- `push(value)`: always appends to `self.stack`. Also appends to `self.min_stack`
  when `min_stack` is empty or when `value` is less than or equal to the current
  minimum (`min_stack[-1]`). Using `<=` correctly handles repeated minimum values.
- `pop()`: removes the top value from `self.stack`. If that value equals the current
  minimum, it is also removed from `self.min_stack`, revealing the previous minimum.
  Returns `None` on an empty stack.
- `top()`: returns `self.stack[-1]` without removing it. Returns `None` on an empty stack.
- `get_min()`: returns `self.min_stack[-1]` without removing it. Python's built-in
  `min()` is NOT used. Returns `None` on an empty stack.

Empty-stack behaviour is consistent: `pop()`, `top()`, and `get_min()` all return `None`.

No `min()` is used inside `get_min()`.

### Complexity

- Time complexity: **O(1)** for `push`, `pop`, `top`, and `get_min` — each performs a
  constant number of list append/pop/index operations.
- Space complexity: **O(n)** - in the worst case `min_stack` holds up to `n` values
  (for example, when values are pushed in decreasing order).

### Test results

`python 02-data-structures-algorithms/stacks/test_day13_min_stack.py` → **all 9 tests passed**

| Test case | Result |
|-----------|--------|
| Push positive numbers, get_min returns smallest | Pass |
| Push negative numbers, get_min returns most negative | Pass |
| Mix of positive and negative tracks true minimum | Pass |
| Repeated minimum values tracked across pops | Pass |
| Pop current minimum reveals next smallest | Pass |
| top() returns last pushed without removing | Pass |
| Empty stack: pop/top/get_min return None | Pass |
| get_min returns None after popping all elements | Pass |
| Sequence of multiple operations | Pass |

---

## 3. Day 11 and Day 12 Status (unchanged)

Day 11 and Day 12 files exist and their tests were verified passing previously:

- Python Day 11 dictionaries/frequency: `test_day11_dictionaries_frequency.py` passes.
- DSA Day 11 valid anagram: `test_day11_valid_anagram.py` passes.
- Python Day 12 exception handling: `test_day12_exception_handling.py` passes (10 tests).
- DSA Day 12 valid parentheses: `test_day12_valid_parentheses.py` passes (9 tests).

Day 11 and Day 12 remain recorded as **learner practice pending** in `PROGRESS.md`.
No changes were made to Day 11 or Day 12 records.

---

## 4. Day 13 completion status

- Python file handling: implemented + tests verified passing (7 tests).
- DSA Min Stack: implemented + tests verified passing (9 tests).
- Learner practice: **pending** (the learner should solve the exercises independently
  before marking the day complete).

This follows the same convention used for Days 9-12: implementation and tests are
verified, while learner practice remains pending.
