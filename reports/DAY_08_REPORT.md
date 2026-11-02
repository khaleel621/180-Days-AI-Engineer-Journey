# Day 8 Report — Sorting Algorithms: Bubble Sort and Selection Sort

## 1. Topic and Objectives

- **Day:** Day 8 — 2026-11-02 (Python + DSA day counter, separate from the 180-day AI Engineer journey).
- **Python + DSA topic:** Sorting algorithms — bubble sort and selection sort — plus time complexity comparison.
- **Objectives:**
    1. Implement bubble sort with nested loops, adjacent element comparison, and swapping; optimized with a swap flag for early exit.
    2. Implement selection sort by finding the minimum in the unsorted section and swapping it into the correct boundary position.
    3. Both algorithms return a new sorted list without modifying the original.
    4. Compare best/average/worst case time complexity of both algorithms.
    5. Write and run automated tests covering normal, sorted, reverse-sorted, empty, single-element, duplicate, negative, and zero-containing lists.

## 2. Exercises Completed

1. **Bubble Sort — `day08-bubble-sort.py`**
    - `bubble_sort(numbers)` uses nested loops: outer loop for passes, inner loop for adjacent comparisons.
    - Compares `sorted_nums[j]` with `sorted_nums[j + 1]`; swaps if left > right.
    - Optimized: `swapped` flag detects a pass with no swaps and breaks early.
    - Returns a new sorted list; the original list is not modified.
    - Demo: `numbers = [5, 3, 8, 1, 2]` → `[1, 2, 3, 5, 8]`.
    - Time complexity: best O(n), average O(n²), worst O(n²).

2. **Selection Sort — `day08-selection-sort.py`**
    - `selection_sort(numbers)` divides the list into sorted (left) and unsorted (right) parts.
    - Finds the smallest element in the unsorted section (from index i to end).
    - Swaps the smallest element into position i (the boundary).
    - Returns a new sorted list; the original list is not modified.
    - Demo: `numbers = [64, 25, 12, 22, 11]` → `[11, 12, 22, 25, 64]`.
    - Time complexity: best O(n²), average O(n²), worst O(n²).

3. **Comparison — `day08-sorting-comparison.md`**
    - What sorting means.
    - How bubble sort works (with example).
    - How selection sort works (with example).
    - Key differences between the two algorithms.
    - Why sorting is useful (searching, extremes, duplicates, analysis, UI).
    - Time complexity table (best/average/worst case).
    - Files overview.

## 3. Files Created

| File | Purpose |
|------|---------|
| `02-data-structures-algorithms/arrays/day08-bubble-sort.py` | Bubble sort implementation and demo. |
| `02-data-structures-algorithms/arrays/day08-selection-sort.py` | Selection sort implementation and demo. |
| `02-data-structures-algorithms/arrays/day08-sorting-comparison.md` | Beginner-friendly algorithm comparison with table. |
| `02-data-structures-algorithms/arrays/test_day08-bubble-sort.py` | Tests for `bubble_sort()`. |
| `02-data-structures-algorithms/arrays/test_day08-selection-sort.py` | Tests for `selection_sort()`. |
| `learning-logs/2026/2026-11-02.md` | Day 8 learning log. |
| `reports/DAY_08_REPORT.md` | This report. |

## 4. Updated Documentation

- `02-data-structures-algorithms/README.md` — Day 8 entries added to file inventory and run/test instructions.
- `README.md` (root) — Day 8 added to Current Progress.
- `PROGRESS.md` — Day 8 section added with concepts learned and test results.

## 5. Test Results

All tests were executed with Python and produced exit code 0.

| Test file | Command | Result |
|-----------|---------|--------|
| `test_day08-bubble-sort.py` | `python 02-data-structures-algorithms/arrays/test_day08-bubble-sort.py` | Passed — 9 tests |
| `test_day08-selection-sort.py` | `python 02-data-structures-algorithms/arrays/test_day08-selection-sort.py` | Passed — 9 tests |
| `day08-bubble-sort.py` | `python 02-data-structures-algorithms/arrays/day08-bubble-sort.py` | Output: `Sorted list: [1, 2, 3, 5, 8]`, original unchanged |
| `day08-selection-sort.py` | `python 02-data-structures-algorithms/arrays/day08-selection-sort.py` | Output: `Sorted list: [11, 12, 22, 25, 64]`, original unchanged |

### Bubble Sort Test Cases

| # | Case | Input | Target/Expected | Actual | Pass |
|---|------|-------|-----------------|--------|------|
| 1 | Normal unsorted | `[5, 3, 8, 1, 2]` | `[1, 2, 3, 5, 8]` | `[1, 2, 3, 5, 8]` | ✅ |
| 2 | Already sorted | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | ✅ |
| 3 | Reverse sorted | `[9, 7, 5, 3, 1]` | `[1, 3, 5, 7, 9]` | `[1, 3, 5, 7, 9]` | ✅ |
| 4 | Empty list | `[]` | `[]` | `[]` | ✅ |
| 5 | Single element | `[42]` | `[42]` | `[42]` | ✅ |
| 6 | Duplicates | `[3, 1, 2, 1, 3, 2]` | `[1, 1, 2, 2, 3, 3]` | `[1, 1, 2, 2, 3, 3]` | ✅ |
| 7 | Negative numbers | `[-3, 5, -1, 0, 2]` | `[-3, -1, 0, 2, 5]` | `[-3, -1, 0, 2, 5]` | ✅ |
| 8 | With zero | `[0, -1, 3, 0, 2]` | `[-1, 0, 0, 2, 3]` | `[-1, 0, 0, 2, 3]` | ✅ |
| 9 | Original not modified | `[5, 3, 8, 1, 2]` | unchanged | unchanged | ✅ |

### Selection Sort Test Cases

| # | Case | Input | Target/Expected | Actual | Pass |
|---|------|-------|-----------------|--------|------|
| 1 | Normal unsorted | `[64, 25, 12, 22, 11]` | `[11, 12, 22, 25, 64]` | `[11, 12, 22, 25, 64]` | ✅ |
| 2 | Already sorted | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | ✅ |
| 3 | Reverse sorted | `[9, 7, 5, 3, 1]` | `[1, 3, 5, 7, 9]` | `[1, 3, 5, 7, 9]` | ✅ |
| 4 | Empty list | `[]` | `[]` | `[]` | ✅ |
| 5 | Single element | `[42]` | `[42]` | `[42]` | ✅ |
| 6 | Duplicates | `[3, 1, 2, 1, 3, 2]` | `[1, 1, 2, 2, 3, 3]` | `[1, 1, 2, 2, 3, 3]` | ✅ |
| 7 | Negative numbers | `[-3, 5, -1, 0, 2]` | `[-3, -1, 0, 2, 5]` | `[-3, -1, 0, 2, 5]` | ✅ |
| 8 | With zero | `[0, -1, 3, 0, 2]` | `[-1, 0, 0, 2, 3]` | `[-1, 0, 0, 2, 3]` | ✅ |
| 9 | Original not modified | `[64, 25, 12, 22, 11]` | unchanged | unchanged | ✅ |

## 6. Complexity

| Algorithm | Best Case | Average Case | Worst Case | Extra Space (new list) |
|-----------|-----------|--------------|------------|------------------------|
| Bubble Sort (optimized) | O(n) | O(n²) | O(n²) | O(n) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(n) |

## 7. Problems Encountered

None. Both implementations and all 18 tests ran as expected on the first verification run.

## 8. Completion Status

**Complete and verified.** Day 8 implementation, tests, comparison document,
documentation updates, learning log, and report are all in place.
GitHub upload status: pending (to be pushed in this session).

## 9. 180-Day AI Engineer Journey

No AI journey lesson was implemented in this session. The AI journey day
counter is separate from the Python + DSA counter and remains at Day 2.
The roadmap's next pending AI item is the already in-progress Day 2 ML
model evaluation; no new AI day files were created to avoid inventing or
duplicating a lesson.