# Data Structures & Algorithms

This folder contains algorithm- and data-structure-focused practice from the AI Engineer Journey. Python syntax lessons remain in `../01-python-fundamentals/`.

Exercises are organized by topic (for example, `arrays/`). Tests are kept beside the code they cover.

## File Inventory

| Exercise | File | Concept practiced | Status |
|----------|------|-------------------|--------|
| Two Sum (nested loop / brute force) | `arrays/two-sum.py` | Arrays, list indexing, nested loops, `range()`, `if`, `break`, boolean flag, O(n²) time, O(1) extra space | Completed — verified |
| Two Sum tests | `arrays/day01_test_two_sum.py` | Tests for `two_sum()` | Passes |
| Strings (`len()` example) | `arrays/day03-strings.py` | `len()` on a string | Example only (not a full exercise) |
| Even or Odd | `day_02-even-odd.py` | `%` modulus, `if`/`else`, zero and negative handling | Implemented — verified |
| Count occurrences (DSA) | `arrays/day05-count-occurrences.py` | Linear scan with a counter; O(n) time, O(1) extra space | Completed — verified |
| Frequency counting and duplicate detection (DSA) | `arrays/day06-frequency-and-duplicates.py` | `count_frequency()` with dictionary + loop, sets for unique values, `find_duplicates()` with sets; O(n) time, O(k) extra space | Completed — verified |
| Count Even Numbers tests | `arrays/test_count_even_numbers.py` | References `count-even-numbers.py` | Test present; solution missing |
| Frequency and duplicate tests | `arrays/test_day06-frequency-and-duplicates.py` | Tests for `count_frequency()` and `find_duplicates()` | Passes |
| Linear search (Day 7) | `arrays/day07-linear-search.py` | `linear_search()` with a `for` loop; checks each element one by one; returns index or `-1`; O(n) time, O(1) extra space | Completed — verified |
| Binary search (Day 7) | `arrays/day07-binary-search.py` | `binary_search()` with `low`, `high`, `mid` and a `while` loop on sorted lists; returns index or `-1`; O(log n) time, O(1) extra space | Completed — verified |
| Search comparison (Day 7) | `arrays/day07-search-comparison.md` | Linear vs binary search, sorted-data requirement, best/average/worst case table | Completed — verified |
| Linear search tests | `arrays/test_day07-linear-search.py` | Tests for `linear_search()` | Passes |
| Binary search tests | `arrays/test_day07-binary-search.py` | Tests for `binary_search()`, including even/odd-length lists | Passes |

## Details

### Two Sum — `arrays/two-sum.py`

Finds two indices whose values add up to a target using a nested-loop brute-force approach. Returns a tuple `(i, j)` or `None` when no pair exists.

Example: `two_sum([2, 7, 11, 15], 9)` returns `(0, 1)`.

### Even or Odd — `day_02-even-odd.py`

`even_or_odd(number)` returns `"{number} is even."` when `number % 2 == 0`, otherwise `"{number} is odd."`. Handles zero and negative integers.

Verified: `even_or_odd(8)` → `8 is even.`, `even_or_odd(7)` → `7 is odd.`, `even_or_odd(0)` → `0 is even.`, `even_or_odd(-3)` → `-3 is odd.`

### Count Occurrences — `arrays/day05-count-occurrences.py`

`count_occurrences(numbers, target)` counts how many times `target` appears in `numbers` using a single `for` loop and a counter initialized to zero. It does not use `list.count()` or `collections.Counter`.

Example: `count_occurrences([2, 5, 2, 8, 2, 10, 5], 2)` returns `3`, and the demo prints `2 appears 3 times`.

- **Why a counter and loop:** each element must be examined to decide whether it matches the target, so one counter updated in a single pass is the direct beginner-friendly approach.
- **Time complexity:** O(n) — the list is traversed once.
- **Auxiliary space complexity:** O(1) — only a fixed number of variables (counter and loop value) are used, excluding the input list.

Verified: `count_occurrences([2, 5, 2, 8, 2, 10, 5], 2)` → `3`, printing `2 appears 3 times`. All five tests in `arrays/test_day05_count_occurrences.py` pass.

### Strings — `arrays/day03-strings.py`

A minimal example: `word = "COMPUTER"; print(len(word))`. Not a complete exercise with functions or tests.

### Count Even Numbers — `arrays/test_count_even_numbers.py`

This test file loads `count-even-numbers.py`, but that solution file is **no longer present** in the repository (it was removed during reorganization). The test cannot run until the solution file is restored or the reference is corrected. Previously it counted even values in one list traversal: O(n) time, O(1) extra space.

### Day 7 — Searching Algorithms

#### Linear Search — `arrays/day07-linear-search.py`

`linear_search(numbers, target)` scans the list with a `for` loop, checking each element one by one from index 0. It returns the index of the target if found, or `-1` if the target is absent. It works on sorted or unsorted lists.

Example: `linear_search([10, 20, 30, 40, 50], 30)` returns `2`, and the demo prints `30 found at index 2`.

- **Time complexity:** O(n) — the list may be traversed once.
- **Auxiliary space complexity:** O(1) — only the index variable is used.
- Verified: all 7 tests in `arrays/test_day07-linear-search.py` pass.

#### Binary Search — `arrays/day07-binary-search.py`

`binary_search(numbers, target)` requires a sorted list. It keeps a search range with `low` and `high`, computes `mid = (low + high) // 2`, and halves the range each iteration of a `while` loop:
- `numbers[mid] == target` → return `mid`.
- `numbers[mid] < target` → search the right half (`low = mid + 1`).
- `numbers[mid] > target` → search the left half (`high = mid - 1`).

It returns the index if found, or `-1` if the range is empty.

Example: `binary_search([10, 20, 30, 40, 50, 60, 70], 50)` returns `4`, and the demo prints `50 found at index 4`.

- **Time complexity:** O(log n) — the search range is halved each step.
- **Auxiliary space complexity:** O(1).
- **Important:** the list must be sorted; otherwise the result can be wrong.
- Verified: all 9 tests in `arrays/test_day07-binary-search.py` pass.

#### Comparison — `arrays/day07-search-comparison.md`

Compares linear and binary search: how they work, why binary search requires sorted data, time complexity of both, and a best/average/worst case table.

## Files Not Present

The following files are referenced in older notes but do **not** currently exist:

* `arrays/count-even-numbers.py` — solution file missing
* `arrays/test_two_sum.py` — replaced by `arrays/day01_test_two_sum.py`

## How to Run

From the repository root:

```bash
python 02-data-structures-algorithms/arrays/two-sum.py
python 02-data-structures-algorithms/day_02-even-odd.py
python 02-data-structures-algorithms/arrays/day05-count-occurrences.py
python 02-data-structures-algorithms/arrays/day06-frequency-and-duplicates.py
python 02-data-structures-algorithms/arrays/day07-linear-search.py
python 02-data-structures-algorithms/arrays/day07-binary-search.py
python 02-data-structures-algorithms/arrays/day01_test_two_sum.py
python 02-data-structures-algorithms/arrays/test_day05_count_occurrences.py
python 02-data-structures-algorithms/arrays/test_day06-frequency-and-duplicates.py
python 02-data-structures-algorithms/arrays/test_day07-linear-search.py
python 02-data-structures-algorithms/arrays/test_day07-binary-search.py
```

`day_02-even-odd.py` reads input from the keyboard; run it in an interactive terminal.
