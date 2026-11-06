# Day 11 Report — 2026-11-06

## Track A — Python + DSA (30-Day Challenge, Day 11)

### 1. Topic and Objectives

- **Python:** Learn dictionary methods and frequency counting (`calculate_total_marks`, `character_frequency`).
- **DSA:** Implement Valid Anagram (`is_anagram`) using dictionary frequency counting, O(n) time, O(k) extra space, no `sorted()`.

### 2. Files Created

| File | Purpose |
|------|---------|
| `01-python-fundamentals/day11-dictionaries-frequency.py` | Dictionary concepts, examples, `calculate_total_marks()`, `character_frequency()`, with `main()` demo |
| `01-python-fundamentals/test_day11_dictionaries_frequency.py` | 12 tests covering dictionary methods, frequency counting, both exercises |
| `02-data-structures-algorithms/strings/is_anagram.py` | `is_anagram(s, t)` using dictionary frequency counting with complexity explanation |
| `02-data-structures-algorithms/strings/test_day11_valid_anagram.py` | 14 tests covering valid/invalid anagrams, different lengths, empty strings, single characters, repeated characters, case sensitivity |

### 3. Python Day 11 — Dictionary Methods and Frequency Counting

**`calculate_total_marks(marks)`**
- Returns the sum of all values in a marks dictionary
- Example: `{"Maths": 85, "Python": 90, "English": 75}` → `250`

**`character_frequency(text)`**
- Returns a dictionary mapping each character to its frequency count
- Example: `"banana"` → `{"b": 1, "a": 3, "n": 2}`

### 4. DSA Day 11 — Valid Anagram

**`is_anagram(s, t)`**
- Returns `False` immediately if lengths differ
- Counts character frequencies in `s`, decrements using `t`
- Returns `True` only if all counts return to zero
- Does NOT use `sorted()`
- Time complexity: O(n) — one pass through each string
- Extra space complexity: O(k) — k distinct characters

**Verified examples:**

| Input s | Input t | Expected | Actual |
|---------|---------|----------|--------|
| `"listen"` | `"silent"` | True | True |
| `"hello"` | `"world"` | False | False |
| `"anagram"` | `"nagaram"` | True | True |
| `"rat"` | `"car"` | False | False |
| `"a"` | `"a"` | True | True |
| `"a"` | `"ab"` | False | False |
| `""` | `""` | True | True |

### 5. Tests and Actual Results

| Test File | Command | Result |
|-----------|---------|--------|
| `01-python-fundamentals/test_day11_dictionaries_frequency.py` | `python <file>` | **All 12 tests passed — EXIT 0** |
| `02-data-structures-algorithms/strings/test_day11_valid_anagram.py` | `python <file>` | **All 14 tests passed — EXIT 0** |

### 6. Learner Practice Status

- **Python Day 11 dictionaries and frequency counting:** Implementation and tests created and verified. **Learner practice pending.**
- **DSA Day 11 valid anagram:** Implementation and tests created and verified. **Learner practice pending.**

## Track B — 180-Day AI Engineer Journey (Day 2 — Model Evaluation)

### 1. Script

`03-machine-learning/03-model-evaluation/iris-classification-evaluation.py`

### 2. Execution Result

**Could not run.** `scikit-learn` is not installed in this environment. Running `python 03-machine-learning/03-model-evaluation/iris-classification-evaluation.py` produced `ModuleNotFoundError: No module named 'sklearn'`. Per project rules, no packages were installed.

This is consistent with prior documentation. The script itself was not modified.

### 3. Personal Review Status

**Pending.** The learner must run the script in an environment with scikit-learn and complete the five review questions documented in `03-machine-learning/03-model-evaluation/README.md`:

1. Test accuracy — what value and what fraction correct?
2. Confusion matrix diagonal — what do the diagonal cells represent?
3. Lowest recall class — which class and what does low recall mean?
4. Meaning of support — what does the support column represent?
5. Why accuracy alone may be insufficient — when do precision/recall matter more?

Until these answers are supplied by the learner, AI Journey Day 2 remains **In Progress**. Day 3 is NOT started.

### 4. Actual Evaluation Metrics

Not available — scikit-learn is not installed in this environment.

## 7. Documentation Updated

| File | Change |
|------|--------|
| `PROGRESS.md` | Added Day 11 entries (Python + DSA); updated Topic Folders status; learner practice marked pending; AI Day 2 kept In Progress |
| `01-python-fundamentals/README.md` | Added Day 11 to exercises table, how-to-run, and tests table |
| `02-data-structures-algorithms/README.md` | Added Day 11 strings folder entry to file inventory, details section, and how-to-run |
| `learning-logs/2026/2026-11-06.md` | Created dated learning log for 2026-11-06 |
| `reports/DAY_11_REPORT.md` | Created this report |

## 8. Commit Status

Not yet committed. Relevant files are staged individually (not `git add .`).

## 9. GitHub Upload Status

Not yet pushed. Push to `origin/main` pending commit.

## 10. Next Learning Tasks

1. Complete Python Day 9 learner practice (manual list comprehension exercises).
2. Complete DSA Day 9 learner practice (manual trace of `max_profit`).
3. Complete Python Day 10 learner practice (manual tuple and set exercises).
4. Complete DSA Day 10 learner practice (manual trace of `contains_duplicate`).
5. Complete Python Day 11 learner practice (manual dictionary exercises).
6. Complete DSA Day 11 learner practice (manual trace of `is_anagram`).
7. Run Iris evaluation script in an environment with scikit-learn; answer the five review questions.
8. Commit and push Day 11 changes to GitHub.
9. Do NOT start Day 12 or AI Journey Day 3.