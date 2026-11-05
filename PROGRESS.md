# Progress Tracking

## Day 1 — 2026-10-19: Python Fundamentals

| Exercise | Status | Details |
|----------|--------|---------|
| Student Marks Analysis | Completed | Dictionary, average, topper, pass/fail count; OOP `Student` and `MarksBook` classes (`__init__`/`self`), edge cases and invalid input handling. Verified: `test_student_marks.py` and `test_student_marks_oop.py` pass. |

### Concepts Learned
- [x] Dictionary storage and iteration
- [x] `for` loops over `.values()` and `.items()`
- [x] `if` conditions
- [x] f-string formatting
- [x] Classes and objects (`Student`, `MarksBook`)
- [x] `__init__` constructor and `self` parameter

## Day 2 — 2026-10-20: Python + DSA

| Exercise | Status | Details |
|----------|--------|---------|
| Two Sum (Nested Loop) | Completed | Nested loops, `range()`, `break`, found flag. File: `02-data-structures-algorithms/arrays/two-sum.py`. Verified: `day01_test_two_sum.py` passes. |

### Concepts Learned
- [x] List indexing
- [x] `range()` function
- [x] `if` conditions
- [x] `break` statement
- [x] Boolean flag pattern
- [x] Time complexity analysis (O(n²))

## Day 2 Practice Continuation — Conditions, Loops & Problem-Solving (2026-10-25)

| Exercise | Status | Details |
|----------|--------|---------|
| Even or Odd | Completed — verified | `even_or_odd(number)` in `02-data-structures-algorithms/arrays/day_02-even-odd.py`. Handles `% 2`, positive, zero, and negative integers. `test_day02-conditions-loops.py` now correctly loads from the DSA folder path and all tests pass. |
| Multiplication Table | Completed — verified | `multiplication_table(number)` in `01-python-fundamentals/03-multiplication-table.py`. Uses a `for` loop and `range(1, 11)`. Covered by `test_day02-conditions-loops.py` which now passes. |

### Concepts Practiced
- [x] Modulus (`%`) for even/odd checks
- [x] `for` loops with `range()`
- [x] Conditional counting with an initialized counter

## Day 2 — DSA: Array Counting

| Exercise | Status | Details |
|----------|--------|---------|
| Count Even Numbers (DSA) | Completed — verified | `count_even_numbers(numbers)` in `02-data-structures-algorithms/arrays/count-even-numbers.py`. Single loop with modulus check; O(n) time, O(1) extra space. Handles empty list, negative numbers, and zero. Verified: `test_count_even_numbers.py` passes (6 test cases). |

## Day 2 — 2026-10-20: Machine Learning

| Exercise | Status | Details |
|----------|--------|---------|
| Pandas and EDA | Completed | Data exploration with Pandas |
| Iris Classification — Model Training | Completed | Training accuracy observed in a verification run (Python 3.13.9, scikit-learn 1.9.1): 0.9750 |
| Iris Classification — Model Evaluation | In Progress | Script written; execution verified in a separate session on 2026-10-23; test accuracy observed: 1.0000 (30 test samples). Results may vary across environments; your personal review and exercise completion remain pending. |

### Concepts Learned (ML)
- [x] Pandas DataFrame operations
- [x] Exploratory data analysis (EDA)
- [x] Loading datasets from `sklearn.datasets`
- [x] Train/test split with `train_test_split`
- [x] Logistic Regression with `sklearn.linear_model`
- [x] Accuracy calculation with `accuracy_score`
- [ ] Confusion matrix interpretation
- [ ] Classification report (precision, recall, F1-score)
- [ ] Model evaluation verification

## Day 5 — 2026-10-28: Python Functions + DSA Counting Occurrences

| Exercise | Status | Details |
|----------|--------|---------|
| Add Two Numbers | Completed — verified | `add_numbers(a, b)` in `01-python-fundamentals/day05-functions.py`. Defines with `def`, takes two numeric parameters, returns their sum without printing inside the function, includes basic numeric input validation. Demo prints `Sum: 30` for 10 and 20. Verified: `test_day05_functions.py` passes (10+20=30, 0+0=0, -5+2=-3). |
| Count Occurrences (DSA) | Completed — verified | `count_occurrences(numbers, target)` in `02-data-structures-algorithms/arrays/day05-count-occurrences.py`. Initializes a counter to zero, uses a `for` loop, increments on a match, returns the count; no `.count()` or `collections.Counter`. Handles empty lists and absent targets (0). Demo prints `2 appears 3 times` for `[2, 5, 2, 8, 2, 10, 5]` with target `2`. Complexity: O(n) time, O(1) extra space. Verified: `test_day05_count_occurrences.py` passes (all 5 cases). |

### Concepts Learned

- [x] Defining functions with `def` and calling them
- [x] Parameters and arguments
- [x] `return` values vs `print()` output
- [x] Basic input validation (`isinstance` check)
- [x] Linear scan with an initialized counter
- [x] Time complexity O(n) and auxiliary space O(1)

## Day 6 — 2026-10-29: Dictionaries, Sets, Frequency Counting, and Duplicate Detection

| Exercise | Status | Details |
|----------|--------|---------|
| Student Marks Dictionary | Completed — verified | Dictionary access, add, update, and loop in `01-python-fundamentals/day06-dictionaries.py`. Verified: `test_day06_dictionaries.py` passes (5 tests: access, add, update, missing student, loop). |
| Count Frequencies | Completed — verified | `count_frequency(numbers)` in `02-data-structures-algorithms/arrays/day06-frequency-and-duplicates.py`. Loop + dictionary, no `list.count()` or `collections.Counter`. Handles empty list and negative/zero values. Verified: tests pass. |
| Understand Sets | Completed — verified | `set()` keeps only unique values; display order is not guaranteed. Demonstrated in `day06-frequency-and-duplicates.py`. |
| Detect Duplicates | Completed — verified | `find_duplicates(numbers)` in `02-data-structures-algorithms/arrays/day06-frequency-and-duplicates.py`. Loop + sets; each duplicate appears once, in order of first repeated detection. Handles empty list, unique-only input, all-same input, multiple duplicates, negatives, and zero. Verified: tests pass (10 cases). |

### Concepts Learned

- [x] Dictionary key/value pairs, access by key, add, update, `.items()` iteration
- [x] Frequency counting with a dictionary and one loop
- [x] Sets store unique values; sets are unordered
- [x] Duplicate detection with `seen` and `already_recorded` sets
- [x] `list.count()` and `collections.Counter` intentionally not used
- [x] O(n) time and O(k) auxiliary space for counting and duplicate detection

## Day 7 — 2026-11-01: Linear Search, Binary Search, and Time Complexity

| Exercise | Status | Details |
|----------|--------|---------|
| Linear Search | Completed — verified | `linear_search(numbers, target)` in `02-data-structures-algorithms/arrays/day07-linear-search.py`. Uses a `for` loop, checks each element one by one, returns the index if found and `-1` otherwise. Works on sorted or unsorted lists. Demo prints `30 found at index 2` for `[10, 20, 30, 40, 50]` with target `30`. Verified: `test_day07-linear-search.py` passes (7 tests). |
| Binary Search | Completed — verified | `binary_search(numbers, target)` in `02-data-structures-algorithms/arrays/day07-binary-search.py`. Requires a sorted list; uses `low`, `high`, `mid = (low + high) // 2` and a `while` loop; returns the index if found and `-1` otherwise. Demo prints `50 found at index 4` for `[10, 20, 30, 40, 50, 60, 70]` with target `50`. Verified: `test_day07-binary-search.py` passes (9 tests). |
| Search Comparison | Completed — verified | Beginner-friendly comparison in `02-data-structures-algorithms/arrays/day07-search-comparison.md`: how each algorithm works, why binary search requires sorted data, time complexity, and a best/average/worst case table. |

### Concepts Learned

- [x] Linear search: one `for` loop, check each element, return index or `-1`; O(n) time, O(1) extra space.
- [x] Binary search: `low`, `high`, `mid`, `while low <= high`, halve the range each step; O(log n) time, O(1) extra space.
- [x] Binary search requires sorted data; linear search does not.
- [x] Best case O(1) for both; average/worst O(n) for linear, O(log n) for binary.
- [x] Time complexity introduction: best, average, and worst case.

## Day 8 — 2026-11-02: Sorting Algorithms — Bubble Sort and Selection Sort

| Exercise | Status | Details |
|----------|--------|---------|
| Bubble Sort | Completed — verified | `bubble_sort(numbers)` in `02-data-structures-algorithms/arrays/day08-bubble-sort.py`. Uses nested loops, compares adjacent elements, swaps when in wrong order. Optimized with a swap flag to stop early if no swaps occur (best case O(n)). Returns a new sorted list; the original list is not modified. Demo: `[5, 3, 8, 1, 2]` → `[1, 2, 3, 5, 8]`. Verified: `test_day08-bubble-sort.py` passes (9 tests). |
| Selection Sort | Completed — verified | `selection_sort(numbers)` in `02-data-structures-algorithms/arrays/day08-selection-sort.py`. Finds the smallest element in the unsorted section and swaps it into the correct position at the boundary. Returns a new sorted list; the original list is not modified. Demo: `[64, 25, 12, 22, 11]` → `[11, 12, 22, 25, 64]`. Verified: `test_day08-selection-sort.py` passes (9 tests). |
| Sorting Comparison | Completed — verified | Beginner-friendly comparison in `02-data-structures-algorithms/arrays/day08-sorting-comparison.md`: what sorting means, how bubble sort works, how selection sort works, key differences, why sorting is useful, and a best/average/worst case time complexity table. |

### Concepts Learned

- [x] Bubble sort: nested loops, adjacent element comparison, swapping, O(n²) average/worst, O(n) best with early-exit optimization.
- [x] Selection sort: find minimum in unsorted section, swap into boundary position, O(n²) for all cases, at most n−1 swaps.
- [x] Both algorithms return a new sorted list without modifying the original.
- [x] Time complexity table: best/average/worst case for both algorithms.
- [x] Writing automated tests for edge cases: empty list, single element, duplicates, negatives, zeros, already sorted, reverse sorted.

## Day 9 — 2026-11-03: Python List Comprehensions + DSA Best Time to Buy and Sell Stock

| Exercise | Status | Details |
|----------|--------|---------|
| square_numbers(numbers) | Files created; tests pass | `square_numbers(numbers)` in `01-python-fundamentals/day09-list-comprehensions.py`. Uses a list comprehension `[x * x for x in numbers]` to return a new list of squares. Original list is not modified. Verified: `test_day09_list_comprehensions.py` passes (8 tests). |
| filter_even_numbers(numbers) | Files created; tests pass | `filter_even_numbers(numbers)` in `01-python-fundamentals/day09-list-comprehensions.py`. Uses a list comprehension with `if` condition `[x for x in numbers if x % 2 == 0]` to return only even numbers. Original list is not modified. Verified: `test_day09_list_comprehensions.py` passes (8 tests). |
| Best Time to Buy and Sell Stock (max_profit) | Files created; tests pass | `max_profit(prices)` in `02-data-structures-algorithms/arrays/day09-best-time-to-buy-and-sell-stock.py`. Single-pass algorithm tracking `minimum_price` and `maximum_profit`. O(n) time, O(1) extra space. Verified: `test_day09_best_time_to_buy_and_sell_stock.py` passes (11 tests). |

### Concepts Learned — Python Day 9

- [ ] List comprehensions: `[expression for item in iterable if condition]`
- [ ] `square_numbers()` — transform each element with a comprehension
- [ ] `filter_even_numbers()` — filter with an `if` condition in a comprehension
- [ ] `map()` and `filter()` intentionally not used
- [ ] Input list not modified — a new list is returned

### Concepts Learned — DSA Day 9

- [ ] Single-pass maximum profit: track `minimum_price` and `maximum_profit`
- [ ] Buy day must be before sell day — only earlier prices are considered for buying
- [ ] Minimum price updated during traversal to unlock future profits
- [ ] Time complexity: O(n); extra space complexity: O(1)
- [ ] No nested loops or sorting used

### Learner Practice Status

- Python Day 9 list comprehensions: Implementation and tests created and verified. **Learner practice pending.**
- DSA Day 9 stock profit: Implementation and tests created and verified. **Learner practice pending.**
- AI Journey Day 2 model evaluation: Script exists; execution blocked by missing scikit-learn in this environment. **Personal review pending.**

## Day 10 — 2026-11-05: Python Tuples and Sets + DSA Contains Duplicate

| Exercise | Status | Details |
|----------|--------|---------|
| tuple_information(items) | Files created; tests pass | `tuple_information(items)` in `01-python-fundamentals/day10-tuples-and-sets.py`. Returns count, first, last elements. Handles empty tuple safely. Verified: `test_day10_tuples_and_sets.py` passes (7 tests). |
| remove_duplicates(numbers) | Files created; tests pass | `remove_duplicates(numbers)` in `01-python-fundamentals/day10-tuples-and-sets.py`. Uses a set to remove duplicates. Original input not modified. Verified: `test_day10_tuples_and_sets.py` passes (7 tests). |
| contains_duplicate(numbers) | Files created; tests pass | `contains_duplicate(numbers)` in `02-data-structures-algorithms/arrays/day10-contains-duplicate.py`. Set-based duplicate detection. O(n) time, O(n) extra space. Verified: `test_day10_contains_duplicate.py` passes (9 tests). |

### Concepts Learned — Python Day 10

- [ ] Tuples: ordered, immutable collections created with `()`
- [ ] Tuple indexing: positive (from 0) and negative (from -1)
- [ ] Immutability: tuples cannot be modified after creation
- [ ] Sets: unordered collections of unique values created with `{}` or `set()`
- [ ] Set operations: add, remove, discard, pop, union, intersection, difference, symmetric difference
- [ ] Sets do not guarantee original ordering
- [ ] `tuple_information(items)` — count, first, last; empty tuple handled safely
- [ ] `remove_duplicates(numbers)` — set-based dedup, input not modified

### Concepts Learned — DSA Day 10

- [ ] Contains Duplicate: detect if any value appears at least twice
- [ ] Set-based approach: check membership in a set while iterating
- [ ] A set stores only unique values
- [ ] Time complexity: O(n) — one pass through the list
- [ ] Extra space complexity: O(n) — the set may store up to n elements

### Learner Practice Status

- Python Day 9 list comprehensions: Implementation and tests created and verified. **Learner practice pending.**
- DSA Day 9 stock profit: Implementation and tests created and verified. **Learner practice pending.**
- Python Day 10 tuples and sets: Implementation and tests created and verified. **Learner practice pending.**
- DSA Day 10 contains duplicate: Implementation and tests created and verified. **Learner practice pending.**
- AI Journey Day 2 model evaluation: Script exists; execution blocked by missing scikit-learn in this environment. **Personal review pending.**

## Upcoming / Planned

| Exercise | Status | Notes |
|----------|--------|-------|
| Word Frequency Counter | Planned — Not Started | Not practiced yet |
| Safe Division | Planned — Not Started | Not practiced yet |

## Topic Folders

| Folder | Status |
|--------|--------|
| `01-python-fundamentals` | In Progress (Day 10 created; learner practice pending) |
| `02-data-structures-algorithms` | In Progress (Day 10 created; learner practice pending) |
| `03-machine-learning` | In Progress |
| `04-deep-learning` | Not Started |
| `05-generative-ai` | Not Started |
| `06-llm-engineering` | Not Started |
| `07-rag-systems` | Not Started |
| `08-agentic-ai` | Not Started |
| `09-backend-and-apis` | Not Started |
| `10-deployment-and-mlops` | Not Started |
| `11-projects` | Not Started |
| `12-interview-preparation` | Not Started |
| `13-job-and-internship-preparation` | Not Started |
