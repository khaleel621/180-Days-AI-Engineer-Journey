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
| Even or Odd | Implemented | `even_or_odd(number)` in `02-data-structures-algorithms/day_02-even-odd.py`. Handles `% 2`, positive, zero, and negative integers. Behavior verified directly. Note: `test_day02-conditions-loops.py` references `02-even-odd.py`, which is no longer present, so that test currently errors until its reference is updated. |
| Multiplication Table | Implemented | `multiplication_table(number)` in `01-python-fundamentals/03-multiplication-table.py`. Uses a `for` loop and `range(1, 11)`. Behavior verified directly. Covered by `test_day02-conditions-loops.py` (which currently errors on the missing `02-even-odd.py`). |

### Concepts Practiced
- [x] Modulus (`%`) for even/odd checks
- [x] `for` loops with `range()`
- [x] Conditional counting with an initialized counter

## Day 2 — DSA: Array Counting

| Exercise | Status | Details |
|----------|--------|---------|
| Count Even Numbers (DSA) | In Progress — solution missing | `test_count_even_numbers.py` exists in `02-data-structures-algorithms/arrays/`, but it loads `count-even-numbers.py`, which is no longer present. Cannot be verified until the solution file is restored or the test reference corrected. |

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

## Upcoming / Planned

| Exercise | Status | Notes |
|----------|--------|-------|
| Word Frequency Counter | Planned — Not Started | Not practiced yet |
| Safe Division | Planned — Not Started | Not practiced yet |

## Topic Folders

| Folder | Status |
|--------|--------|
| `01-python-fundamentals` | In Progress (Day 6 complete) |
| `02-data-structures-algorithms` | In Progress (Day 6 complete) |
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
