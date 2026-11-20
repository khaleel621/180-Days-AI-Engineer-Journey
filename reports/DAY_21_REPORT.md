# Day 21 Report — Python Class/Static Methods, Heap & Iris Evaluation

## Date: 2026-11-20

## Topics Covered

### Track A — Python: OOP Class Methods and Static Methods
- Class methods: belong to the class, marked with `@classmethod`, use the `cls` parameter to access class-level data shared by all objects.
- The `cls` parameter: refers to the class itself (like `self` refers to an instance); passed automatically by Python.
- Static methods: belong to the class but use neither `self` nor `cls`; marked with `@staticmethod`; utility functions grouped in a class.
- Difference between instance, class and static methods:
  - Instance method → works on one object's data (`self`).
  - Class method → works on class-level data shared by all objects (`cls`).
  - Static method → does not use object or class state.
- When to use each: instance (object attributes), class (class variables / alternate constructors), static (helpers unrelated to state).
- `Student` class: class variable `school_name`, instance method `display_info()`, class method `change_school_name()`, static method `is_passed(score)`.

### Track B — DSA: Heap and Priority Queue
- Heap: complete binary tree with heap property; stored as a list; root at index 0.
- Min-heap root = minimum; max-heap root = maximum. Python's `heapq` provides a min-heap (negate values to simulate max-heap).
- `heapq` operations: `heapify()` (O(n)), `heappush()` (O(log n)), `heappop()` (O(log n)), `nlargest()`, `nsmallest()`.
- Main problem: Kth Largest Element in an Array. Example `nums = [3, 2, 1, 5, 6, 4]`, `k = 2` → `5`.
- Optimal approach: min-heap of size k; push each number; pop smallest when size > k; root = kth largest. Handles duplicates; validates k.
- Time complexity: O(n log k); Space complexity: O(k).

### Track C — Machine Learning: Iris Model Evaluation (In Progress)
- Continued the existing Iris project; no duplicate project created.
- Reused existing model, dataset and train/test split from `02-model-training/`.
- Improved `03-model-evaluation/iris-classification-evaluation.py`: explicit per-class precision, recall, F1-score and support, plus simple English explanations.
- Metrics covered: predictions, accuracy, confusion matrix, precision, recall, F1-score, classification report.
- scikit-learn not installed in this environment → Iris script/tests could not be executed here. Iris Model Evaluation remains **In Progress** pending your personal review.

## Files Created

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/day21-class-and-static-methods.py` | Source: `Student` class/static-methods example |
| `01-python-fundamentals/test_day21_class_and_static_methods.py` | Tests for class/static methods |
| `02-data-structures-algorithms/heaps/day21-kth-largest-element.py` | Source: `find_kth_largest()` min-heap solution |
| `02-data-structures-algorithms/heaps/test_day21_kth_largest_element.py` | Tests for Kth Largest Element |
| `learning-logs/2026/2026-11-20.md` | Learning log for Day 21 |
| `reports/DAY_21_REPORT.md` | This report |

## Files Modified

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/README.md` | Added Day 21 test row + learner-practice-pending entry |
| `02-data-structures-algorithms/README.md` | Added Day 21 heaps rows + how-to-run lines |
| `03-machine-learning/03-model-evaluation/iris-classification-evaluation.py` | Added explicit per-class metrics + explanations |
| `03-machine-learning/03-model-evaluation/README.md` | Noted the improvement |

## Test Results

All tests executed and verified:
- `01-python-fundamentals/test_day21_class_and_static_methods.py`: 8 tests passed (via `python` and `pytest`).
- `02-data-structures-algorithms/heaps/test_day21_kth_largest_element.py`: 10 tests passed (via `python` and `pytest`).
- Combined: **18 passed, 0 failed**.
- Iris evaluation tests: **could not run** — scikit-learn is not installed (`ModuleNotFoundError: No module named 'sklearn'`). Pre-existing blocker documented in PROGRESS.md.

## Time and Space Complexity (DSA)

| Metric | Complexity | Explanation |
|--------|-----------|-------------|
| Time | O(n log k) | Each of n elements costs O(log k) heap push/pop. |
| Space | O(k) | Heap holds at most k elements. |

## Practice Completion Status

| Track | Topic | Status |
|-------|-------|--------|
| Python | Day 21 Class Methods and Static Methods | Files created, tests verified (8 passed). **Learner practice pending.** |
| DSA | Day 21 Heap / Kth Largest Element | Files created, tests verified (10 passed). **Learner practice pending.** |
| ML | Iris Model Evaluation | Script improved. **In Progress** — pending your personal review and confirmation. |

Personal practice is NOT marked complete. It remains pending until you confirm completion.