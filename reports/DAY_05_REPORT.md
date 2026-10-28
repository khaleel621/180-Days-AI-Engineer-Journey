# Day 5 Report — Python Functions and DSA Occurrence Counting

## 1. Topic and Objectives

- **Day:** Day 5 — 2026-10-28.
- **Python topic:** Functions — define with `def`, parameters, `return` values, calling a function, `print()` vs `return`, basic input validation.
- **DSA topic:** Counting occurrences in an array using a counter and a `for` loop.

## 2. Exercises Completed

1. **Add Two Numbers** (`01-python-fundamentals/day05-functions.py`)
   - `add_numbers(a, b)` returns `a + b`; nothing is printed inside the function.
   - Basic validation: both arguments must be `int` or `float`.
   - Demonstration: `add_numbers(10, 20)` prints `Sum: 30`.
2. **Count Occurrences** (`02-data-structures-algorithms/arrays/day05-count-occurrences.py`)
   - `count_occurrences(numbers, target)` initializes a counter to zero, loops once over the list, increments on a match, and returns the count.
   - No `list.count()` or `collections.Counter`; handles empty lists and absent targets.
   - Demonstration: `[2, 5, 2, 8, 2, 10, 5]` with target `2` prints `2 appears 3 times`.

## 3. Files Created

- `01-python-fundamentals/day05-functions.py` — functions exercise.
- `01-python-fundamentals/test_day05_functions.py` — tests for `add_numbers()`.
- `02-data-structures-algorithms/arrays/day05-count-occurrences.py` — counting exercise.
- `02-data-structures-algorithms/arrays/test_day05_count_occurrences.py` — tests for `count_occurrences()`.
- `learning-logs/2026/2026-10-28.md` — Day 5 learning log.
- `reports/DAY_05_REPORT.md` — this report.

## 4. Updated Documentation

- `01-python-fundamentals/README.md` — Day 5 exercise, how to run, test result.
- `02-data-structures-algorithms/README.md` — Day 5 entry, algorithm explanation, complexity, run/test instructions.
- `README.md` — Day 5 added to Current Progress (verified).
- `PROGRESS.md` — Day 5 section added, marked completed — verified.

## 5. Test Results

| Test file | Command | Result |
|-----------|---------|--------|
| `test_day05_functions.py` | `python 01-python-fundamentals/test_day05_functions.py` | Passed — 3 tests: 10+20=30, 0+0=0, -5+2=-3 |
| `test_day05_count_occurrences.py` | `python 02-data-structures-algorithms/arrays/test_day05_count_occurrences.py` | Passed — 5 cases (basic, all-match, absent target, empty list, zeros/negatives) |
| `day05-functions.py` | `python 01-python-fundamentals/day05-functions.py` | Output: `Sum: 30` |
| `day05-count-occurrences.py` | `python 02-data-structures-algorithms/arrays/day05-count-occurrences.py` | Output: `2 appears 3 times` |

Existing checks re-run and still pass: `test_student_marks.py`, `test_student_marks_oop.py`, `day01_test_two_sum.py`.

## 6. Complexity of the DSA Solution

For a list of n values:

- **Time complexity:** O(n) — each element is examined exactly once.
- **Auxiliary space complexity:** O(1) — only a fixed number of variables (counter and loop value) are used, excluding the input list.

## 7. Problems Encountered

None. All Day 5 exercises and tests ran as expected on the first verification run.

## 8. Completion Status

**Complete and verified.** Day 5 implementation, tests, documentation, learning log, and report are all in place. Ready for review and GitHub upload.
