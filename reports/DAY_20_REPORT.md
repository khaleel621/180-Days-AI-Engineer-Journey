# Day 20 Report — Python OOP Encapsulation & Minimum Window Substring

## Date: 2026-11-19

## Topics Covered

### Track A — Python: OOP Encapsulation
- What encapsulation is: bundling data and methods into a class and restricting direct access to internal state.
- Public, protected, and private attributes: `account_holder_name`, `_account_number`, `__balance`.
- Private variables using double underscores and name mangling (`_BankAccount__balance`).
- Getters and setters via the `balance` property with validation.
- `BankAccount` class: `deposit()`, `withdraw()`, `display_balance()`; prevents negative deposits and overdrafts.
- Why encapsulation is useful: guards invariants and centralizes validation.

### Track B — DSA: Minimum Window Substring
- Function `min_window(s, t)` using a sliding window + frequency dictionary.
- `need` dictionary built from `t`; `window_counts` tracks the current window.
- `formed` vs `required` to know when the window is valid; shrink from the left to minimize.
- Duplicate characters in `t` handled via exact count matching.
- Returns `""` when no valid window exists (empty input, `t` longer than `s`, missing characters).
- Example: `s = "ADOBECODEBANC"`, `t = "ABC"` → `"BANC"`.
- Time complexity: O(|s| + |t|); Space complexity: O(|s| + |t|).

## Files Created

| Path | Purpose |
|------|---------|
| `01-python-fundamentals/day20-oop-encapsulation.py` | Source: `BankAccount` encapsulation example |
| `01-python-fundamentals/test_day20_oop_encapsulation.py` | Tests for encapsulation |
| `02-data-structures-algorithms/strings/day20-minimum-window-substring.py` | Source: `min_window()` |
| `02-data-structures-algorithms/strings/test_day20_minimum_window_substring.py` | Tests for `min_window()` |
| `learning-logs/2026/2026-11-19.md` | Learning log for Day 20 |
| `reports/DAY_20_REPORT.md` | This report |

## Test Results

All tests executed and verified:
- `01-python-fundamentals/test_day20_oop_encapsulation.py`: 17 tests passed (via `python` and `pytest`).
- `02-data-structures-algorithms/strings/test_day20_minimum_window_substring.py`: 9 tests passed (via `python` and `pytest`).
- Total: **26 passed, 0 failed**.

## Time and Space Complexity (DSA)

| Metric | Complexity | Explanation |
|--------|-----------|-------------|
| Time | O(|s| + |t|) | Each character of `s` is visited at most twice (right and left pointers); `t` is traversed once. |
| Space | O(|s| + |t|) | Two frequency dictionaries bounded by the number of distinct characters. |

## Practice Completion Status

| Track | Topic | Status |
|-------|-------|--------|
| Python | Day 20 OOP Encapsulation | Files created, tests written and verified. **Learner practice pending.** |
| DSA | Day 20 Minimum Window Substring | Files created, tests written and verified. **Learner practice pending.** |

Personal practice is NOT marked complete. It remains pending until the learner confirms completion.