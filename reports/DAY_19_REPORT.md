# Day 19 Report — Python OOP Abstraction & Sliding Window Maximum

## Date: 2026-11-17

## Topics Covered

### Track A — Python: OOP Abstraction
- Abstract Base Classes (ABC) and `abstractmethod` from the `abc` module.
- Abstract class `Shape` with abstract method `area()`.
- Concrete class `Rectangle(Shape)` implementing `area()` as `length * width`.
- Concrete class `Circle(Shape)` implementing `area()` as `pi * radius * radius`.
- Verification that `Shape()` raises `TypeError` (cannot instantiate abstract class).

### Track B — DSA: Sliding Window Maximum using Deque
- Function `max_sliding_window(numbers, k)` using `collections.deque`.
- Deque stores indices; maintains decreasing values; removes out-of-window indices.
- `ValueError` for invalid `k` (non-positive, larger than list, non-integer).
- Empty input returns empty list.
- Time complexity: O(n), Space complexity: O(k).

## Files Created

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/day19-oop-abstraction.py` | Source: Shape, Rectangle, Circle |
| `01-python-fundamentals/test_day19_oop_abstraction.py` | Tests for abstraction |
| `02-data-structures-algorithms/arrays/day19-sliding-window-maximum.py` | Source: sliding window maximum |
| `02-data-structures-algorithms/arrays/test_day19_sliding_window_maximum.py` | Tests for sliding window |
| `learning-logs/2026/2026-11-17.md` | Learning log for Day 19 |
| `reports/DAY_19_REPORT.md` | This report |

## Test Results

Tests have NOT yet been executed. They will be run with:
- `py -3.13 01-python-fundamentals/test_day19_oop_abstraction.py`
- `py -3.13 02-data-structures-algorithms/arrays/test_day19_sliding_window_maximum.py`

## Time and Space Complexity (DSA)

| Metric | Complexity | Explanation |
|--------|-----------|-------------|
| Time | O(n) | Each index is pushed and popped from the deque at most once. |
| Space | O(k) | The deque holds at most k indices at any time. |

## Practice Completion Status

| Track | Topic | Status |
|-------|-------|--------|
| Python | Day 19 OOP Abstraction | **Pending** — files created, tests written, not yet verified by learner |
| DSA | Day 19 Sliding Window Maximum | **Pending** — files created, tests written, not yet verified by learner |

Personal practice is NOT marked complete. It remains pending until the learner confirms.