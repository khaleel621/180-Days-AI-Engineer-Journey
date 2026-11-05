# Day 10 Report — 2026-11-05

## Track A — Python + DSA (30-Day Challenge, Day 10)

### 1. Topic and Objectives

- **Python:** Learn and practice tuples and sets (`tuple_information`, `remove_duplicates`).
- **DSA:** Implement Contains Duplicate (`contains_duplicate`) using a set-based O(n) approach.

### 2. Files Created

| File | Purpose |
|------|---------|
| `01-python-fundamentals/day10-tuples-and-sets.py` | Tuple and set concepts, examples, `tuple_information()`, `remove_duplicates()`, with `main()` demo |
| `01-python-fundamentals/test_day10_tuples_and_sets.py` | 7 tests covering normal/empty/single-element/mixed-type tuples and duplicate removal, ordering, input-not-modified |
| `02-data-structures-algorithms/arrays/day10-contains-duplicate.py` | `contains_duplicate(numbers)` set-based solution with complexity explanation |
| `02-data-structures-algorithms/arrays/test_day10_contains_duplicate.py` | 9 tests covering duplicates, no duplicates, empty, single element, negatives, repeats, larger input |

### 3. Python Day 10 — Tuples and Sets

**`tuple_information(items)`**
- Returns `{"count": N, "first": first_item, "last": last_item}`
- Empty tuple returns `{"count": 0, "first": None, "last": None}`
- Example: `tuple_information((10, 20, 30))` → `{"count": 3, "first": 10, "last": 30}`

**`remove_duplicates(numbers)`**
- Uses `set()` to identify unique values
- Returns a list of unique values (order not guaranteed)
- Original input list is not modified
- Example: `remove_duplicates([1, 2, 2, 3, 1])` → `[1, 2, 3]` (order may vary)

### 4. DSA Day 10 — Contains Duplicate

**`contains_duplicate(numbers)`**
- Iterates through the list, checking membership in a set
- Returns `True` on first duplicate found, `False` if none
- Time complexity: O(n) — one pass
- Extra space complexity: O(n) — set may store up to n elements

**Verified examples:**
| Input | Expected | Actual |
|-------|----------|--------|
| `[1, 2, 3, 1]` | True | True |
| `[1, 2, 3, 4]` | False | False |
| `[]` | False | False |
| `[5, 5]` | True | True |

### 5. Tests and Actual Results

| Test File | Command | Result |
|-----------|---------|--------|
| `01-python-fundamentals/test_day10_tuples_and_sets.py` | `python <file>` | **All 7 tests passed — EXIT 0** |
| `02-data-structures-algorithms/arrays/test_day10_contains_duplicate.py` | `python <file>` | **All 9 tests passed — EXIT 0** |

### 6. Learner Practice Status

- **Python Day 10 tuples and sets:** Implementation and tests created and verified. **Learner practice pending.**
- **DSA Day 10 contains duplicate:** Implementation and tests created and verified. **Learner practice pending.**

## Track B — 180-Day AI Engineer Journey (Day 2 — Model Evaluation)

### 1. Script

`03-machine-learning/03-model-evaluation/iris-classification-evaluation.py`

### 2. Execution Result

**Could not run.** `scikit-learn` is not installed in this environment. The script produces no output when run with `py -3.13` because the `import sklearn` fails. Per project rules, no packages were installed.

This is consistent with prior documentation. The script itself was not modified.

### 3. Personal Review Status

**Pending.** The learner must run the script in an environment with scikit-learn and complete the five review questions documented in `03-machine-learning/03-model-evaluation/README.md`:

1. Test accuracy — what value and what fraction correct?
2. Confusion matrix diagonal — what do the diagonal cells represent?
3. Lowest recall class — which class and what does low recall mean?
4. Meaning of support — what does the support column represent?
5. Why accuracy alone may be insufficient — when do precision/recall matter more?

Until these answers are supplied by the learner, AI Journey Day 2 remains **In Progress**. Day 3 is NOT started.

### 4. README Update

Added a "Learner Review Exercise (Personal Review — Pending)" section to `03-machine-learning/03-model-evaluation/README.md` with the five review questions (already present from Day 9).

## 7. Documentation Updated

| File | Change |
|------|--------|
| `PROGRESS.md` | Added Day 10 entries (Python + DSA); updated Topic Folders status; learner practice marked pending; AI Day 2 kept In Progress |
| `01-python-fundamentals/README.md` | Added Day 10 to exercises table, how-to-run, and tests table |
| `02-data-structures-algorithms/README.md` | Added Day 10 to file inventory and how-to-run |
| `learning-logs/2026/2026-11-05.md` | Created dated learning log for 2026-11-05 |
| `reports/DAY_10_REPORT.md` | Created this report |

## 8. Commit Status

Not yet committed. Relevant files are staged individually (not `git add .`).

## 9. GitHub Upload Status

Not yet pushed. Push to `origin/main` pending commit.

## 10. Next Learning Tasks

1. Complete Python Day 9 learner practice (manual list comprehension exercises).
2. Complete DSA Day 9 learner practice (manual trace of `max_profit`).
3. Complete Python Day 10 learner practice (manual tuple and set exercises).
4. Complete DSA Day 10 learner practice (manual trace of `contains_duplicate`).
5. Run Iris evaluation script in an environment with scikit-learn; answer the five review questions.
6. Commit and push Day 10 changes to GitHub.
7. Do NOT start Day 11 or AI Journey Day 3.