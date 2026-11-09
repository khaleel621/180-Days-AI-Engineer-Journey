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
| Count Even Numbers (DSA) | `arrays/count-even-numbers.py` | Single loop with modulus check; O(n) time, O(1) extra space | Completed — verified |
| Count Even Numbers tests | `arrays/test_count_even_numbers.py` | Tests for `count_even_numbers()` | Passes |
| Frequency and duplicate tests | `arrays/test_day06-frequency-and-duplicates.py` | Tests for `count_frequency()` and `find_duplicates()` | Passes |
| Linear search (Day 7) | `arrays/day07-linear-search.py` | `linear_search()` with a `for` loop; checks each element one by one; returns index or `-1`; O(n) time, O(1) extra space | Completed — verified |
| Binary search (Day 7) | `arrays/day07-binary-search.py` | `binary_search()` with `low`, `high`, `mid` and a `while` loop on sorted lists; returns index or `-1`; O(log n) time, O(1) extra space | Completed — verified |
| Search comparison (Day 7) | `arrays/day07-search-comparison.md` | Linear vs binary search, sorted-data requirement, best/average/worst case table | Completed — verified |
| Linear search tests | `arrays/test_day07-linear-search.py` | Tests for `linear_search()` | Passes |
| Binary search tests | `arrays/test_day07-binary-search.py` | Tests for `binary_search()`, including even/odd-length lists | Passes |
| Bubble sort (Day 8) | `arrays/day08-bubble-sort.py` | Optimized bubble sort with swap flag; compares adjacent elements and swaps; O(n) best / O(n²) average / O(n²) worst; returns a new sorted list | Completed — verified |
| Selection sort (Day 8) | `arrays/day08-selection-sort.py` | Selection sort: finds minimum in unsorted section, swaps into place; O(n²) best / O(n²) average / O(n²) worst; returns a new sorted list | Completed — verified |
| Bubble sort tests | `arrays/test_day08-bubble-sort.py` | Tests for `bubble_sort()` | Passes |
| Selection sort tests | `arrays/test_day08-selection-sort.py` | Tests for `selection_sort()` | Passes |
| Sorting comparison (Day 8) | `arrays/day08-sorting-comparison.md` | Bubble sort vs selection sort, how each works, comparison table, why sorting is useful | Completed — verified |
| Best Time to Buy and Sell Stock (Day 9) | `arrays/day09-best-time-to-buy-and-sell-stock.py` | Single-pass maximum profit: track `minimum_price` and `maximum_profit`; O(n) time, O(1) extra space; no nested loops or sorting | Files created; tests pass |
| Contains Duplicate (Day 10) | `arrays/day10-contains-duplicate.py` | Duplicate detection using a set; O(n) time, O(n) extra space | Files created; tests pass |
| Best Time to Buy and Sell Stock tests | `arrays/test_day09_best_time_to_buy_and_sell_stock.py` | Tests for `max_profit()` covering all examples and edge cases | Passes |
| Contains Duplicate tests | `arrays/test_day10_contains_duplicate.py` | Tests for `contains_duplicate()` covering duplicates, no duplicates, empty, single element, negatives, repeats, larger input | Passes |
| Valid Anagram (Day 11) | `strings/is_anagram.py` | Anagram detection using dictionary frequency counting; O(n) time, O(k) extra space; no sorted() used | Files created; tests pass |
| Valid Anagram tests | `strings/test_day11_valid_anagram.py` | Tests for `is_anagram()` covering valid/invalid anagrams, different lengths, empty strings, single characters, repeated characters, case sensitivity | Passes |
| Valid Parentheses (Day 12) | `stacks/day12-valid-parentheses.py` | Valid parentheses using a stack (Python list) with `append()` and `pop()`. Supports `()`, `{}`, `[]`. O(n) time, O(n) extra space. | Files created; tests pass |
| Valid Parentheses tests (Day 12) | `stacks/test_day12_valid_parentheses.py` | Tests for `is_valid()` covering all 9 required cases. | Passes |

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

### Count Even Numbers — `arrays/count-even-numbers.py`

`count_even_numbers(numbers)` counts how many even values appear in a list using a single loop and the modulus operator (`% 2 == 0`). O(n) time, O(1) extra space. Handles empty lists, negative numbers, and zero.

Example: `count_even_numbers([12, 7, 4, 9, 6, 3, 8])` returns `4`.

Verified: all 6 tests in `arrays/test_count_even_numbers.py` pass.

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

### Day 11 — Valid Anagram — `strings/is_anagram.py`

`is_anagram(s, t)` determines whether two strings are anagrams using dictionary frequency counting.

**Approach:**
1. If the strings have different lengths, they cannot be anagrams → return `False`.
2. Count character frequencies in `s` using a dictionary.
3. For each character in `t`, decrement its count. If a character is missing or count goes negative → return `False`.
4. If all counts return to zero → return `True`.

Does NOT use `sorted()` or compare sorted strings.

Examples:
- `is_anagram("listen", "silent")` → `True`
- `is_anagram("hello", "world")` → `False`
- `is_anagram("anagram", "nagaram")` → `True`
- `is_anagram("rat", "car")` → `False`
- `is_anagram("a", "a")` → `True`
- `is_anagram("a", "ab")` → `False`
- `is_anagram("", "")` → `True`

- **Time complexity:** O(n) — one pass through each string.
- **Extra space complexity:** O(k) — k distinct characters stored in the dictionary.

Verified: all 14 tests in `strings/test_day11_valid_anagram.py` pass.

## Files Not Present

The following files are referenced in older notes but do **not** currently exist:

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
python 02-data-structures-algorithms/arrays/day08-bubble-sort.py
python 02-data-structures-algorithms/arrays/day08-selection-sort.py
python 02-data-structures-algorithms/arrays/test_day08-bubble-sort.py
python 02-data-structures-algorithms/arrays/test_day08-selection-sort.py
python 02-data-structures-algorithms/arrays/day09-best-time-to-buy-and-sell-stock.py
python 02-data-structures-algorithms/arrays/test_day09_best_time_to_buy_and_sell_stock.py
python 02-data-structures-algorithms/arrays/day10-contains-duplicate.py
python 02-data-structures-algorithms/arrays/test_day10_contains_duplicate.py
python 02-data-structures-algorithms/strings/is_anagram.py
python 02-data-structures-algorithms/strings/test_day11_valid_anagram.py
python 02-data-structures-algorithms/stacks/day12-valid-parentheses.py
python 02-data-structures-algorithms/stacks/test_day12_valid_parentheses.py
```

`day_02-even-odd.py` reads input from the keyboard; run it in an interactive terminal.
