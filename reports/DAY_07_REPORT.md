# Day 7 Report — Linear Search, Binary Search, and Time Complexity Introduction

## 1. Topic and Objectives

- **Day:** Day 7 — 2026-11-01 (Python + DSA day counter, separate from the 180-day AI Engineer journey).
- **Python + DSA topic:** Searching algorithms — linear search and binary search — plus an introduction to time complexity.
- **Objectives:**
    1. Implement linear search with a `for` loop: check each element one by one, return the index or `-1`.
    2. Implement binary search with `low`, `high`, `mid`, and a `while` loop on a sorted list: return the index or `-1`.
    3. Explain why binary search requires sorted data.
    4. Compare best/average/worst case time complexity of both algorithms.
    5. Write and run automated tests for both algorithms.

## 2. Exercises Completed

1. **Linear Search — `day07-linear-search.py`**
   - `linear_search(numbers, target)` uses a `for` loop over `range(len(numbers))`.
   - Returns the index of the target if found, otherwise `-1`.
   - Demo: `numbers = [10, 20, 30, 40, 50]`, `target = 30` → `30 found at index 2`.
   - Works on sorted or unsorted lists.

2. **Binary Search — `day07-binary-search.py`**
   - `binary_search(numbers, target)` requires a sorted list (ascending order).
   - Uses `low = 0`, `high = len(numbers) - 1`, and `mid = (low + high) // 2` in a `while low <= high` loop.
   - Narrows the range: `low = mid + 1` when target is on the right, `high = mid - 1` when on the left.
   - Returns the index if found, otherwise `-1`.
   - Demo: `numbers = [10, 20, 30, 40, 50, 60, 70]`, `target = 50` → `50 found at index 4`.

3. **Comparison — `day07-search-comparison.md`**
   - How linear search works.
   - How binary search works.
   - Why binary search requires sorted data.
   - Time complexity of both algorithms.
   - Comparison table (best/average/worst case).

## 3. Files Created

| File | Purpose |
|------|---------|
| `02-data-structures-algorithms/arrays/day07-linear-search.py` | Linear search implementation and demo. |
| `02-data-structures-algorithms/arrays/day07-binary-search.py` | Binary search implementation and demo. |
| `02-data-structures-algorithms/arrays/day07-search-comparison.md` | Beginner-friendly algorithm comparison with table. |
| `02-data-structures-algorithms/arrays/test_day07-linear-search.py` | Tests for `linear_search()`. |
| `02-data-structures-algorithms/arrays/test_day07-binary-search.py` | Tests for `binary_search()`. |
| `learning-logs/2026/2026-11-01.md` | Day 7 learning log. |
| `reports/DAY_07_REPORT.md` | This report. |

## 4. Updated Documentation

- `02-data-structures-algorithms/README.md` — Day 7 entries, run/test instructions.
- `README.md` (root) — Day 7 added to Current Progress.
- `PROGRESS.md` — Day 7 section added with test results.
- `learning-logs/2026/2026-11-01.md` — Day 7 learning log.

## 5. Test Results

All tests were executed with Python and produced exit code 0.

| Test file | Command | Result |
|-----------|---------|--------|
| `test_day07-linear-search.py` | `python 02-data-structures-algorithms/arrays/test_day07-linear-search.py` | Passed — 7 tests (exists, missing, first, last, empty, single-element found, single-element missing) |
| `test_day07-binary-search.py` | `python 02-data-structures-algorithms/arrays/test_day07-binary-search.py` | Passed — 9 tests (exists odd-length, missing, first, last, empty, single-element found/missing, even-length, odd-length) |
| `day07-linear-search.py` | `python 02-data-structures-algorithms/arrays/day07-linear-search.py` | Output: `30 found at index 2` |
| `day07-binary-search.py` | `python 02-data-structures-algorithms/arrays/day07-binary-search.py` | Output: `50 found at index 4` |

### Linear Search Test Cases

| # | Case | List | Target | Expected | Actual |
|---|------|------|--------|----------|--------|
| 1 | Target exists | `[10, 20, 30, 40, 50]` | 30 | 2 | 2 ✅ |
| 2 | Target missing | `[10, 20, 30, 40, 50]` | 100 | -1 | -1 ✅ |
| 3 | First element | `[10, 20, 30, 40, 50]` | 10 | 0 | 0 ✅ |
| 4 | Last element | `[10, 20, 30, 40, 50]` | 50 | 4 | 4 ✅ |
| 5 | Empty list | `[]` | 10 | -1 | -1 ✅ |
| 6 | Single element found | `[42]` | 42 | 0 | 0 ✅ |
| 7 | Single element missing | `[42]` | 7 | -1 | -1 ✅ |

### Binary Search Test Cases

| # | Case | List | Target | Expected | Actual |
|---|------|------|--------|----------|--------|
| 1 | Target exists (odd length) | `[10, 20, 30, 40, 50, 60, 70]` | 50 | 4 | 4 ✅ |
| 2 | Target missing | `[10, 20, 30, 40, 50, 60, 70]` | 35 | -1 | -1 ✅ |
| 3 | First element | `[10, 20, 30, 40, 50, 60, 70]` | 10 | 0 | 0 ✅ |
| 4 | Last element | `[10, 20, 30, 40, 50, 60, 70]` | 70 | 6 | 6 ✅ |
| 5 | Empty list | `[]` | 10 | -1 | -1 ✅ |
| 6 | Single element found | `[99]` | 99 | 0 | 0 ✅ |
| 7 | Single element missing | `[99]` | 5 | -1 | -1 ✅ |
| 8 | Even number of elements | `[5, 15, 25, 35]` | 25 / 20 | 2 / -1 | 2 / -1 ✅ |
| 9 | Odd number of elements | `[5, 15, 25]` | 15 | 1 | 1 ✅ |

## 6. Complexity

| Algorithm     | Best Case | Average Case | Worst Case | Extra Space |
| ------------- | --------- | ------------ | ---------- | ----------- |
| Linear Search | O(1)      | O(n)         | O(n)       | O(1)        |
| Binary Search | O(1)      | O(log n)     | O(log n)   | O(1)        |

## 7. Problems Encountered

None. Both implementations and all tests ran as expected on the first verification run.

## 8. Completion Status

**Complete and verified.** Day 7 implementation, tests, comparison document,
documentation updates, learning log, and report are all in place.
GitHub upload status: pending (to be pushed in this session).

## 9. 180-Day AI Engineer Journey

No AI journey lesson was implemented in this session. The AI journey day
counter is separate from the Python + DSA counter and remains at Day 2.
The roadmap's next pending AI item is the already in-progress Day 2 ML
model evaluation; no new AI day files were created to avoid inventing or
duplicating a lesson.
