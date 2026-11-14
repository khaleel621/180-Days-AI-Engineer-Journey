# Day 16 Report - Python OOP (Inheritance, Method Overriding and super()) and Daily Temperatures

Date: 2026-11-14
Track: Python + DSA (Day 16 of the Python/DSA practice)
AI Engineer Journey counter: NOT advanced (remains at Day 2 model evaluation).

## Summary

Implemented and tested Day 16 of the Python + DSA practice:

1. **Python Fundamentals - OOP: Inheritance, Method Overriding and `super()`**
   - `Employee(name, salary)` with `display_details()`.
   - `Manager(Employee)`: inherits name/salary, adds `department`, uses
     `super().__init__(name, salary)`, overrides `display_details()`.
   - `Animal`, `Dog(Animal)`, `Cat(Animal)`: method overriding of
     `make_sound()`.
   - `Shape`, `Rectangle(Shape)`, `Circle(Shape)`: `area()` with `math.pi`
     for the circle.
   - Input validation with `ValueError`; each object's attributes are
     independent.

2. **DSA - Daily Temperatures (Monotonic Stack)**
   - `daily_temperatures(temperatures)` using a monotonic stack that stores
     indices, traversing left to right, with a zero-initialized result list.

All Day 16 tests pass. Day 11, Day 12, Day 13, Day 14 and Day 15 remain
unchanged (learner practice pending).

---

## 1. Python: Inheritance, Method Overriding and super()

File: `01-python-fundamentals/day16-inheritance-and-method-overriding.py`
Tests: `01-python-fundamentals/test_day16_inheritance_and_method_overriding.py`

### Classes implemented

#### `Employee(name, salary)` (parent class)
- Stores the employee's name and salary (instance attributes).
- `display_details()` prints the name and salary.
- Raises `ValueError` for an empty name or a negative/non-numeric salary.

#### `Manager(Employee)` (child class)
- Inherits `name` and `salary` from `Employee`.
- Adds a `department`.
- Uses `super().__init__(name, salary)` to initialize the inherited parts.
- Overrides `display_details()` to also print the department (reuses the
  parent's output via `super().display_details()`).
- Raises `ValueError` for an empty name/department or an invalid salary.

#### `Animal` / `Dog(Animal)` / `Cat(Animal)` (method overriding)
- `Animal.make_sound()` returns a generic sound.
- `Dog.make_sound()` overrides it to return `"Woof!"`.
- `Cat.make_sound()` overrides it to return `"Meow!"`.

#### `Shape` / `Rectangle(Shape)` / `Circle(Shape)` (area)
- `Shape.area()` returns `0` by default.
- `Rectangle(length, width).area()` returns `length * width`.
- `Circle(radius).area()` returns `math.pi * radius * radius`.
- Dimensions are validated: length, width and radius must be positive
  numbers; otherwise `ValueError` is raised.

### Error-handling behaviour

All invalid input raises `ValueError` with a clear message:
- `Employee("", 50000)`, `Employee("Ada", -1)`, `Employee("Ada", "50000")`,
  `Employee("Ada", True)` → `ValueError`.
- `Manager("Ben", 75000, "")`, `Manager("Ben", -100, "Engineering")`,
  `Manager("Ben", 75000, 123)` → `ValueError`.
- `Rectangle(-1, 5)`, `Rectangle(4, 0)`, `Rectangle("4", 5)` → `ValueError`.
- `Circle(-2)`, `Circle(0)`, `Circle("3")` → `ValueError`.

### Test results

`python 01-python-fundamentals/test_day16_inheritance_and_method_overriding.py` → **all 24 tests passed**

| Test case | Result |
|-----------|--------|
| Employee stores name and salary | Pass |
| display_details prints name and salary | Pass |
| Invalid employee name raises ValueError | Pass |
| Invalid employee salary raises ValueError | Pass |
| Two employees are independent | Pass |
| Manager stores name, salary and department | Pass |
| Manager is an Employee | Pass |
| Manager uses super() and inherits Employee init | Pass |
| Manager display_details overrides and shows department | Pass |
| Invalid manager name/salary/department raises ValueError | Pass |
| Two managers are independent | Pass |
| Animal make_sound returns generic sound | Pass |
| Dog make_sound overrides Animal | Pass |
| Cat make_sound overrides Animal | Pass |
| Dog and Cat sounds are different | Pass |
| Rectangle stores length and width | Pass |
| Rectangle area | Pass |
| Rectangle is a Shape | Pass |
| Invalid rectangle length/width raises ValueError | Pass |
| Circle stores radius | Pass |
| Circle area uses math.pi | Pass |
| Circle is a Shape | Pass |
| Invalid circle radius raises ValueError | Pass |

---

## 2. DSA: Daily Temperatures (Monotonic Stack)

File: `02-data-structures-algorithms/stacks/day16-daily-temperatures.py`
Tests: `02-data-structures-algorithms/stacks/test_day16_daily_temperatures.py`

### Implementation

`daily_temperatures(temperatures)` uses a monotonic stack (Python list with
`append()`/`pop()`):

1. Create a result list filled with `0` and an empty stack.
2. Traverse the input from left to right.
3. The stack stores indices of days whose warmer day has not been found yet,
   in decreasing temperature order.
4. For the current day, while the stack is not empty and the current
   temperature is strictly greater than the temperature at the stack's top
   index, pop that index and set `result[popped_index] =
   current_index - popped_index`.
5. Push the current index onto the stack.
6. Return the result list.

Each index is pushed once and popped at most once — no nested-loop main
solution.

The original input list is never modified — only a new result list is
created.

### Complexity

- Time complexity: **O(n)** — each index is pushed once and popped at most
  once.
- Space complexity: **O(n)** — the stack and result list hold up to n
  entries.

### Test results

`python 02-data-structures-algorithms/stacks/test_day16_daily_temperatures.py` → **all 10 tests passed**

| Test case | Result |
|-----------|--------|
| [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0] | Pass |
| [30, 40, 50, 60] -> [1, 1, 1, 0] | Pass |
| [60, 50, 40, 30] -> [0, 0, 0, 0] | Pass |
| [30, 30, 30] -> [0, 0, 0] | Pass |
| [30, 35, 30, 40] -> [1, 2, 1, 0] | Pass |
| [] -> [] | Pass |
| Single element [70] -> [0] | Pass |
| Two warmer elements [70, 80] -> [1, 0] | Pass |
| Two cooler elements [80, 70] -> [0, 0] | Pass |
| Original input not modified | Pass |

---

## 3. Days 11-15 Status (unchanged)

Day 11, Day 12, Day 13, Day 14 and Day 15 files exist and their tests were
verified passing in earlier sessions. They remain recorded as **learner
practice pending** in `PROGRESS.md`. No changes were made to Days 11-15.

---

## 4. Day 16 completion status

- Python: Inheritance, Method Overriding and `super()`: implemented +
  tests verified passing (24 tests).
- DSA Daily Temperatures (Monotonic Stack): implemented + tests verified
  passing (10 tests).
- Learner practice: **pending** (the learner should solve the exercises
  independently before marking the day complete).

This follows the same convention used for Days 9-15: implementation and tests
are verified, while learner practice remains pending.