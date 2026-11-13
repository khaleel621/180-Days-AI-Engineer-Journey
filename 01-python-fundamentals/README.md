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
| Day 9: List Comprehensions | `day09-list-comprehensions.py` | List comprehensions: `square_numbers(numbers)` returns squares via `[x * x for x in numbers]`; `filter_even_numbers(numbers)` returns even values via `[x for x in numbers if x % 2 == 0]`. Original list is not modified. No `map()` or `filter()` used. |
| Day 10: Tuples and Sets | `day10-tuples-and-sets.py` | Tuples: ordered, immutable collections with indexing. Sets: unordered collections of unique values with add/remove and set operations. Includes `tuple_information(items)` and `remove_duplicates(numbers)` exercises. |
| Day 11: Dictionaries and Frequency Counting | `day11-dictionaries-frequency.py` | Dictionaries: key-value pairs, creating, accessing, adding, updating, removing. Methods: keys(), values(), items(), get(), update(), pop(). Dictionary iteration. Frequency counting with dictionaries. Includes `calculate_total_marks(marks)` and `character_frequency(text)` exercises. |
| Day 12: Exception Handling | `day12-exception-handling.py` | Exception handling with try/except/else/finally. Includes `safe_divide(a, b)` (handles division by zero) and `convert_to_integer(value)` (handles invalid input with ValueError). |
| Day 13: File Handling | `day13-file-handling.py` | File handling: `save_student_details()` writes student details in write mode; `read_file()` reads complete file content and handles `FileNotFoundError`; `append_student_subject()` appends in append mode without overwriting existing content. Uses `with open()`. |
| Day 14: Modules and Packages | `day14-modules-and-packages.py` (plus helper `math_operations.py`) | Modules and packages: `calculate_circle_area(radius)` uses `math.pi`; `generate_random_number()` uses `random.randint(1, 100)`; importing from a custom module demonstrated with `import`, `from ... import`, and `... as`. `math_operations.py` provides `add`, `subtract`, `multiply`, `divide` (division by zero handled). |
| Day 15: Classes and Objects | `day15-oop-classes-and-objects.py` | Classes and objects: `Student` (`__init__`, `display_details`, `is_passed` with marks >= 40) and `BankAccount` (`__init__`, `deposit`, `withdraw`, `get_balance`) with input validation and object independence. |

## How to Run Each Exercise

From the repository root:

```bash
python 01-python-fundamentals/01-student-marks-analysis.py
python 01-python-fundamentals/03-multiplication-table.py
python 01-python-fundamentals/day05-functions.py
python 01-python-fundamentals/day06-dictionaries.py
python 01-python-fundamentals/day09-list-comprehensions.py
python 01-python-fundamentals/day10-tuples-and-sets.py
python 01-python-fundamentals/day11-dictionaries-frequency.py
```

`03-multiplication-table.py` prompts for an integer and prints its multiplication table from 1 to 10.

## Tests

Tests live beside the exercises they cover and run directly with Python:

| Test file | Covers | How to run | Result |
|-----------|--------|------------|--------|
| `test_student_marks.py` | Dictionary-based Student Marks Analysis | `python 01-python-fundamentals/test_student_marks.py` | Passes |
| `test_student_marks_oop.py` | `Student` and `MarksBook` OOP classes | `python 01-python-fundamentals/test_student_marks_oop.py` | Passes |
| `test_day02-conditions-loops.py` | Conditions and loops practice | `python 01-python-fundamentals/test_day02-conditions-loops.py` | Passes |
| `test_day05_functions.py` | `add_numbers()` in `day05-functions.py` | `python 01-python-fundamentals/test_day05_functions.py` | Passes |
| `test_day06_dictionaries.py` | Dictionary demo in `day06-dictionaries.py` | `python 01-python-fundamentals/test_day06_dictionaries.py` | Passes |
| `test_day09_list_comprehensions.py` | `square_numbers()` and `filter_even_numbers()` in `day09-list-comprehensions.py` | `python 01-python-fundamentals/test_day09_list_comprehensions.py` | Passes |
| `test_day10_tuples_and_sets.py` | `tuple_information()` and `remove_duplicates()` in `day10-tuples-and-sets.py` | `python 01-python-fundamentals/test_day10_tuples_and_sets.py` | Passes |
| `test_day11_dictionaries_frequency.py` | `calculate_total_marks()` and `character_frequency()` in `day11-dictionaries-frequency.py` | `python 01-python-fundamentals/test_day11_dictionaries_frequency.py` | Passes |
| `test_day12_exception_handling.py` | `safe_divide()` and `convert_to_integer()` in `day12-exception-handling.py` | `python 01-python-fundamentals/test_day12_exception_handling.py` | Passes |
| `test_day13_file_handling.py` | `save_student_details()`, `read_file()`, `append_student_subject()` in `day13-file-handling.py` | `python 01-python-fundamentals/test_day13_file_handling.py` | Passes |
| `test_day14_modules_and_packages.py` | `calculate_circle_area()`, `generate_random_number()`, and imports from `math_operations.py` in `day14-modules-and-packages.py` | `python 01-python-fundamentals/test_day14_modules_and_packages.py` | Passes |
| `test_day15_oop_classes_and_objects.py` | `Student` and `BankAccount` classes | `python 01-python-fundamentals/test_day15_oop_classes_and_objects.py` | Passes |

## Python Syntax Practice vs DSA Practice

This folder is for **Python language syntax practice**. Algorithmic problem-solving — arrays, searching, counting, complexity analysis — belongs in `02-data-structures-algorithms/`. For example, the loop-based even-number counting exercise is DSA work and is stored under `02-data-structures-algorithms/`, not here.

## Files Not Present

The following files are referenced in older notes but do **not** currently exist in this folder:

* `04-count-even-numbers.py` — no longer present
* `student-marks-input-practice.py` — not present
* `day04-strings.py` — not present

## Planned — Not Started

- Word Frequency Counter

These exercises are planned for future practice but have not been started yet.

## Completed — Learner Practice Pending

- Safe Division — implemented in Day 12 (`day12-exception-handling.py` as `safe_divide(a, b)`); tests pass. Learner practice is pending, so the day is not marked complete yet.
- File Handling — implemented in Day 13 (`day13-file-handling.py` as `save_student_details()`, `read_file()`, `append_student_subject()`); tests pass. Learner practice is pending, so the day is not marked complete yet.
- Modules and Packages — implemented in Day 14 (`day14-modules-and-packages.py` with helper `math_operations.py`); tests pass. Learner practice is pending, so the day is not marked complete yet.
