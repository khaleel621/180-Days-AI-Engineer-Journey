# Day 22 Report — Python Magic Methods, Top K Frequent Elements & Iris Evaluation

## Date: 2026-11-21

## Topics Covered

### Track A — Python: OOP Magic Methods (Dunder Methods)

- Magic methods: special Python methods whose names start and end with double underscores; "dunder" = "double underscore".
- You usually do not call them directly; Python calls them for you:
  - `print(book)` → `book.__str__()`
  - `len(book)` → `book.__len__()`
  - `book1 == book2` → `book1.__eq__(book2)`
  - `book1 + book2` → `book1.__add__(book2)`
- `__init__()` — initializer: sets up a new object's attributes (title, author, pages for `Book`).
- `__str__()` — friendly, readable string shown by `print()` and `str()` (for end users).
- `__repr__()` — developer-friendly representation shown by `repr()` (for debugging).
- `__len__()` — length returned by `len()`; returns the number of pages for `Book`.
- `__eq__()` — equality comparison used by `==`; two books are equal when title, author and pages all match; returns `NotImplemented` for non-Book comparisons.
- `__add__()` — addition used by `+`; **NOT implemented for `Book`** because `book1 + book2` has no clearly defined meaning (join titles? add page counts? keep both authors?). A plain function such as `book1.pages + book2.pages` is clearer. `__add__` fits classes where `+` has an obvious meaning (money amounts, vectors, durations).
- Practical implementation: `Book` class in `01-python-fundamentals/day22-magic-methods.py` with input validation (TypeError/ValueError for bad types, empty title/author, negative or non-integer pages).

### Track B — DSA: Top K Frequent Elements

- Problem: given an integer array, return the K most frequent elements.
  - Example: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2` → `[1, 2]`.
- Frequency counting with dictionaries: loop once over the array; a dictionary maps each distinct number to its frequency (e.g. `{1: 3, 2: 2, 3: 1}`). Duplicates update the same key, so the result never contains a number twice.
- Approach 1 — Dictionary + sorting (`top_k_frequent_sorting`): count frequencies, sort distinct numbers by frequency (highest first), return the first k.
- Approach 2 — Heap with `heapq` (`top_k_frequent_heap`): count frequencies, push `(frequency, number)` pairs onto a min-heap of at most k items, popping the smallest frequency when the heap exceeds k; pop the heap to collect the answer.
- Both approaches implemented in `02-data-structures-algorithms/heaps/day22-top-k-frequent-elements.py` with beginner-friendly comments.
- Duplicate values, negative numbers, single-element arrays, `k = 1`, and `k = number of distinct elements` all handled correctly.
- Invalid `k` (non-integer, `< 1`, or `>` distinct count) raises `TypeError`/`ValueError`.
- Ties: any valid set of k elements is acceptable; tests compare results as sets.

### Time and Space Complexity (DSA)

| Metric | Dictionary + Sorting | Heap (heapq) | Explanation |
|--------|---------------------|--------------|-------------|
| Time | O(n + m log m) | O(n + m log k) | Counting is O(n) for both; sorting m distinct values costs O(m log m); each heap push/pop costs O(log k) for m values. |
| Space | O(m) | O(m) + O(k) | Dictionary holds m distinct values; heap holds at most k pairs. |

where n = len(nums) and m = number of distinct elements.
### Track C — Machine Learning: Iris Model Evaluation (In Progress)

- Continued the existing Iris project in `03-machine-learning/` (no duplicate project created).
- Reused the existing model, dataset and train/test split from `03-machine-learning/02-model-training/`; no retraining or replacement of the existing model.
- `iris-classification-evaluation.py` already implements all required evaluation steps:
  1. Model predictions on the test set (`model.predict(X_test)`)
  2. Accuracy score (`accuracy_score(y_test, y_pred)`)
  3. Confusion matrix (`confusion_matrix(y_test, y_pred)`)
  4. Precision (via `classification_report` and `precision_recall_fscore_support`)
  5. Recall (via `classification_report` and `precision_recall_fscore_support`)
  6. F1-score (via `classification_report` and `precision_recall_fscore_support`)
  7. Classification report (`classification_report` with `target_names`)
- Metrics explained in beginner-friendly English in the script output; per-class precision/recall/F1/support printed explicitly for the multiclass Iris problem (3 classes: setosa, versicolor, virginica).
- Averaging: `precision_recall_fscore_support(y_test, y_pred)` without `average=` gives per-class values for multiclass; `classification_report` also shows per-class rows plus macro/weighted averages.
- A confusion matrix visualization was NOT added because matplotlib is not installed in this environment and the addition could not be tested; consistent with the pre-existing scikit-learn blocker.
- scikit-learn is NOT installed in this environment (Python 3.11.9 only), so the Iris script and tests cannot be executed here. Iris Model Evaluation remains **In Progress** pending your personal review and confirmation.

## Files Created

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/day22-magic-methods.py` | Source: `Book` class with magic methods + demo |
| `01-python-fundamentals/test_day22_magic_methods.py` | Tests for magic methods |
| `02-data-structures-algorithms/heaps/day22-top-k-frequent-elements.py` | Source: `top_k_frequent_sorting()` and `top_k_frequent_heap()` |
| `02-data-structures-algorithms/heaps/test_day22_top_k_frequent_elements.py` | Tests for Top K Frequent Elements |
| `learning-logs/2026/2026-11-21.md` | Learning log for Day 22 |
| `reports/DAY_22_REPORT.md` | This report |

## Files Modified

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/README.md` | Added Day 22 exercise + test rows and learner-practice-pending entry |
| `02-data-structures-algorithms/README.md` | Added Day 22 heaps rows (file inventory + how-to-run) |
| `PROGRESS.md` | Added Day 22 Python + DSA entries; Iris Model Evaluation remains In Progress |

## Test Results

All tests executed and verified (Python 3.11.9, pytest 9.2.0):
- `01-python-fundamentals/test_day22_magic_methods.py`: **14 tests passed** (via `python` and `pytest`)
- `02-data-structures-algorithms/heaps/test_day22_top_k_frequent_elements.py`: **14 tests passed** (via `python` and `pytest`)
- Existing Day 20/21 tests also pass: **62 passed, 0 failed combined**
- Iris evaluation tests: **could not run** — scikit-learn is not installed (`ModuleNotFoundError: No module named 'sklearn'`). Pre-existing blocker documented in PROGRESS.md.

## Practice Completion Status

| Track | Topic | Status |
|-------|-------|--------|
| Python | Day 22 Magic Methods (Dunder Methods) | Files created, tests verified (14 passed). **Learner practice pending.** |
| DSA | Day 22 Top K Frequent Elements | Files created, tests verified (14 passed). **Learner practice pending.** |
| ML | Iris Model Evaluation | Script complete. **In Progress** — pending your personal review and confirmation. |

Personal practice is NOT marked complete. It remains pending until you confirm completion.

Important: Iris Model Evaluation must remain In Progress until you personally confirm you understand the evaluation results. Do not mark Day 3 of the AI Engineer Journey or any future topic as completed.