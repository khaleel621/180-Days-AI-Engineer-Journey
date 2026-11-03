# Day 9 Report — 2026-11-03

## Track A — Python + DSA (30-Day Challenge, Day 9)

### 1. Topic and Objectives

- **Python:** Learn and practice list comprehensions (`square_numbers`, `filter_even_numbers`).
- **DSA:** Implement Best Time to Buy and Sell Stock (`max_profit`) using a single-pass O(n) algorithm.

### 2. Files Created

| File | Purpose |
|------|---------|
| `01-python-fundamentals/day09-list-comprehensions.py` | `square_numbers()` and `filter_even_numbers()` using list comprehensions; includes `main()` demo |
| `01-python-fundamentals/test_day09_list_comprehensions.py` | 8 tests covering normal/empty/negative/zero/duplicate/no-even/unchanged-input cases |
| `02-data-structures-algorithms/arrays/day09-best-time-to-buy-and-sell-stock.py` | `max_profit(prices)` single-pass algorithm with complexity explanation |
| `02-data-structures-algorithms/arrays/test_day09_best_time_to_buy_and_sell_stock.py` | 11 tests covering all problem examples plus edge cases |

### 3. Python Day 9 — List Comprehensions

**`square_numbers(numbers)`**
- Uses `[x * x for x in numbers]`.
- Returns a new list; original list is not modified.
- Example: `[1, 2, 3, 4] -> [1, 4, 9, 16]`.

**`filter_even_numbers(numbers)`**
- Uses `[x for x in numbers if x % 2 == 0]`.
- Returns only even numbers; original list is not modified.
- Example: `[1, 2, 3, 4, 5, 6] -> [2, 4, 6]`.

No `map()` or `filter()` used.

### 4. DSA Day 9 — Best Time to Buy and Sell Stock

**`max_profit(prices)`**
- Single pass through the price list.
- Tracks `minimum_price` (lowest price seen so far) and `maximum_profit` (best profit achievable).
- For each price: computes profit against `minimum_price`, updates `maximum_profit` if better, updates `minimum_price` if lower.
- Buy day must be before sell day because `minimum_price` only reflects prices seen before the current index.
- Time complexity: O(n). Extra space complexity: O(1).
- No nested loops or sorting.

**Verified examples:**
| Input | Expected | Actual |
|-------|----------|--------|
| `[7, 1, 5, 3, 6, 4]` | 5 | 5 |
| `[7, 6, 4, 3, 1]` | 0 | 0 |
| `[2, 4, 1]` | 2 | 2 |
| `[3]` | 0 | 0 |
| `[]` | 0 | 0 |
| `[1, 1]` | 0 | 0 |

### 5. Tests and Actual Results

| Test File | Command | Result |
|-----------|---------|--------|
| `01-python-fundamentals/test_day09_list_comprehensions.py` | `python <file>` | **All 8 tests passed — EXIT 0** |
| `02-data-structures-algorithms/arrays/test_day09_best_time_to_buy_and_sell_stock.py` | `python <file>` | **All 11 tests passed — EXIT 0** |

### 6. Regression Check (Existing Tests Confirmed Unchanged)

| Test File | Result |
|-----------|--------|
| `test_day05_functions.py` | Passed |
| `test_day06_dictionaries.py` | Passed |
| `test_day07-linear-search.py` | Passed |
| `test_day07-binary-search.py` | Passed |
| `test_day08-bubble-sort.py` | Passed |
| `test_day08-selection-sort.py` | Passed |

### 7. Learner Practice Status

- **Python Day 9 list comprehensions:** Implementation and tests created and verified. **Learner practice pending.**
- **DSA Day 9 stock profit:** Implementation and tests created and verified. **Learner practice pending.**

## Track B — 180-Day AI Engineer Journey (Day 2 — Model Evaluation)

### 1. Script

`03-machine-learning/03-model-evaluation/iris-classification-evaluation.py`

### 2. Execution Result

**Could not run.** `ModuleNotFoundError: No module named 'sklearn'`. scikit-learn is not installed in this environment. Per project rules, no packages were installed.

This is consistent with prior documentation (DAY_01_REPORT.md section 8). The script itself was not modified.

### 3. Personal Review Status

**Pending.** The learner must run the script in an environment with scikit-learn and complete the five review questions documented in `03-machine-learning/03-model-evaluation/README.md`:

1. Test accuracy — what value and what fraction correct?
2. Confusion matrix diagonal — what do the diagonal cells represent?
3. Lowest recall class — which class and what does low recall mean?
4. Meaning of support — what does the support column represent?
5. Why accuracy alone may be insufficient — when do precision/recall matter more?

Until these answers are supplied by the learner, AI Journey Day 2 remains **In Progress**. Day 3 is NOT started.

### 4. README Update

Added a "Learner Review Exercise (Personal Review — Pending)" section to `03-machine-learning/03-model-evaluation/README.md` with the five review questions.

## 8. Documentation Updated

| File | Change |
|------|--------|
| `PROGRESS.md` | Added Day 9 entries (Python + DSA); updated Topic Folders status; learner practice marked pending; AI Day 2 kept In Progress |
| `01-python-fundamentals/README.md` | Added Day 9 to exercises table, how-to-run, and tests table |
| `02-data-structures-algorithms/README.md` | Added Day 9 to file inventory and how-to-run |
| `03-machine-learning/03-model-evaluation/README.md` | Added learner review exercise section |
| `learning-logs/2026/2026-11-03.md` | Created dated learning log for 2026-11-03 |
| `reports/DAY_09_REPORT.md` | Created this report |

## 9. Commit Status

Not yet committed. Relevant files are staged individually (not `git add .`).

## 10. GitHub Upload Status

Not yet pushed. Push to `origin/main` pending commit.

## 11. Next Learning Tasks

1. Complete Python Day 9 learner practice (manual list comprehension exercises).
2. Complete DSA Day 9 learner practice (manual trace of `max_profit`).
3. Run Iris evaluation script in an environment with scikit-learn; answer the five review questions.
4. Commit and push Day 9 changes to GitHub.
5. Do NOT start Day 10 or AI Journey Day 3.