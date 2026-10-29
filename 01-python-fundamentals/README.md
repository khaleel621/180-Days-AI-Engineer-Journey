# Python Fundamentals

This folder contains Python language fundamentals practice for the AI Engineer Journey. It covers beginner programming exercises: variables, data types, conditions, loops, input/output, functions, and basic object-oriented programming.

Algorithm-focused problems (for example Two Sum, array counting) belong in `../02-data-structures-algorithms/`, not here.

## Exercises in This Folder

| Exercise | File | What it teaches |
|----------|------|-----------------|
| Student Marks Analysis | `01-student-marks-analysis.py` | Dictionary storage and iteration, average calculation, topper identification, pass/fail counting, f-strings. Also defines the `Student` and `MarksBook` OOP classes (`__init__`, `self`) with edge-case and invalid-input handling. |
| Multiplication Table | `03-multiplication-table.py` | `for` loops, `range(1, 11)`, functions, and user input. Prints a multiplication table from 1 to 10 for a given integer. |
| Day 5: Functions | `day05-functions.py` | Defining functions with `def`, parameters, `return` values, `print()` vs `return`, calling a function, and basic input validation. Exercise: `add_numbers(a, b)` returns the sum (example: 10 + 20 = 30). |
| Day 6: Dictionaries | `day06-dictionaries.py` | Dictionaries: student names mapped to marks; access a student's marks, add a new student, update existing marks, and loop through names and marks with `.items()`. |

## How to Run Each Exercise

From the repository root:

```bash
python 01-python-fundamentals/01-student-marks-analysis.py
python 01-python-fundamentals/03-multiplication-table.py
python 01-python-fundamentals/day05-functions.py
python 01-python-fundamentals/day06-dictionaries.py
```

`03-multiplication-table.py` prompts for an integer and prints its multiplication table from 1 to 10.

## Tests

Tests live beside the exercises they cover and run directly with Python:

| Test file | Covers | How to run | Result |
|-----------|--------|------------|--------|
| `test_student_marks.py` | Dictionary-based Student Marks Analysis | `python 01-python-fundamentals/test_student_marks.py` | Passes |
| `test_student_marks_oop.py` | `Student` and `MarksBook` OOP classes | `python 01-python-fundamentals/test_student_marks_oop.py` | Passes |
| `test_day02-conditions-loops.py` | Conditions and loops practice | `python 01-python-fundamentals/test_day02-conditions-loops.py` | Errors (see below) |
| `test_day05_functions.py` | `add_numbers()` in `day05-functions.py` | `python 01-python-fundamentals/test_day05_functions.py` | Passes |
| `test_day06_dictionaries.py` | Dictionary demo in `day06-dictionaries.py` | `python 01-python-fundamentals/test_day06_dictionaries.py` | Passes |

### Important: `test_day02-conditions-loops.py` references a missing file

`test_day02-conditions-loops.py` loads `02-even-odd.py`, but that file is **no longer in this folder**. The even/odd exercise now lives in the DSA folder as `02-data-structures-algorithms/day_02-even-odd.py`. Because of this move, `test_day02-conditions-loops.py` raises `FileNotFoundError` until its reference is updated. The multiplication-table portion of the exercise (`03-multiplication-table.py`) still works and is covered by the same test file.

## Python Syntax Practice vs DSA Practice

This folder is for **Python language syntax practice**. Algorithmic problem-solving — arrays, searching, counting, complexity analysis — belongs in `02-data-structures-algorithms/`. For example, the loop-based even-number counting exercise is DSA work and is stored under `02-data-structures-algorithms/`, not here.

## Files Not Present

The following files are referenced in older notes but do **not** currently exist in this folder:

* `02-even-odd.py` — moved to `02-data-structures-algorithms/day_02-even-odd.py`
* `04-count-even-numbers.py` — no longer present
* `student-marks-input-practice.py` — not present
* `day04-strings.py` — not present

## Planned — Not Started

- Word Frequency Counter
- Safe Division

These exercises are planned for future practice but have not been started yet.
