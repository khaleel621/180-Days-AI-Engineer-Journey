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
| Count Even Numbers tests | `arrays/test_count_even_numbers.py` | References `count-even-numbers.py` | Test present; solution missing |

## Details

### Two Sum — `arrays/two-sum.py`

Finds two indices whose values add up to a target using a nested-loop brute-force approach. Returns a tuple `(i, j)` or `None` when no pair exists.

Example: `two_sum([2, 7, 11, 15], 9)` returns `(0, 1)`.

### Even or Odd — `day_02-even-odd.py`

`even_or_odd(number)` returns `"{number} is even."` when `number % 2 == 0`, otherwise `"{number} is odd."`. Handles zero and negative integers.

Verified: `even_or_odd(8)` → `8 is even.`, `even_or_odd(7)` → `7 is odd.`, `even_or_odd(0)` → `0 is even.`, `even_or_odd(-3)` → `-3 is odd.`

### Strings — `arrays/day03-strings.py`

A minimal example: `word = "COMPUTER"; print(len(word))`. Not a complete exercise with functions or tests.

### Count Even Numbers — `arrays/test_count_even_numbers.py`

This test file loads `count-even-numbers.py`, but that solution file is **no longer present** in the repository (it was removed during reorganization). The test cannot run until the solution file is restored or the reference is corrected. Previously it counted even values in one list traversal: O(n) time, O(1) extra space.

## Files Not Present

The following files are referenced in older notes but do **not** currently exist:

* `arrays/count-even-numbers.py` — solution file missing
* `arrays/test_two_sum.py` — replaced by `arrays/day01_test_two_sum.py`

## How to Run

From the repository root:

```bash
python 02-data-structures-algorithms/arrays/two-sum.py
python 02-data-structures-algorithms/day_02-even-odd.py
python 02-data-structures-algorithms/arrays/day01_test_two_sum.py
```

`day_02-even-odd.py` reads input from the keyboard; run it in an interactive terminal.
