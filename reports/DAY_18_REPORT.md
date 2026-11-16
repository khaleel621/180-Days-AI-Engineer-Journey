# Day 18 Report - Python OOP (Polymorphism, Overloading, Overriding) and Trapping Rain Water (Two Pointers)

Date: 2026-11-16
Track: Python + DSA (Day 18 of the Python/DSA practice)
AI Engineer Journey counter: NOT advanced (remains at Day 2 model evaluation).

## Summary

Implemented and tested Day 18 of the Python + DSA practice:

1. **Python Fundamentals - OOP: Polymorphism, Method Overloading and Method Overriding**
   - `Animal` base class with `make_sound()` returning a generic sound.
   - `Dog(Animal)`, `Cat(Animal)`, `Cow(Animal)` — each overrides `make_sound()`.
   - `animal_sound(animal)` — polymorphic function working with any Animal subclass.
   - `Calculator.add(*args)` — Python-style method overloading handling 0, 1, 2, or 3 numeric arguments; rejects non-numeric input with `TypeError`.
   - `DogDuck`, `CatDuck`, `RobotDuck` — classes with no common parent, each with a `.speak()` method.
   - `make_it_speak(obj)` — duck typing function calling `.speak()` on any object that has it.

2. **DSA - Trapping Rain Water (Two Pointers)**
   - `trap(height)` using the two-pointers approach.
   - O(n) time, O(1) additional space.
   - Handles empty input, single element, increasing heights, decreasing heights, equal heights, and multiple water-trapping sections.
   - `[] -> 0`, `[5] -> 0`, `[1, 2, 3, 4] -> 0`, `[4, 3, 2, 1] -> 0`, `[3, 0, 2, 0, 4] -> 7`, `[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> 6`.

All Day 18 tests pass. Day 11-17 remain unchanged (learner practice pending).

---

## 1. Python: Polymorphism, Method Overloading and Method Overriding

File: `01-python-fundamentals/day18-polymorphism.py`
Tests: `01-python-fundamentals/test_day18_polymorphism.py`

### Classes implemented

#### `Animal`
Base class with `make_sound()` returning `"Some generic animal sound"`.

#### `Dog(Animal)`
Overrides `make_sound()` to return `"Woof!"`.

#### `Cat(Animal)`
Overrides `make_sound()` to return `"Meow!"`.

#### `Cow(Animal)`
Overrides `make_sound()` to return `"Moo!"`.

#### `animal_sound(animal)`
Polymorphic function that calls `make_sound()` on any Animal subclass.

#### `Calculator`
`add(*args)` handles any number of numeric arguments using Python-style overloading via `*args`. Raises `TypeError` for non-numeric arguments.

#### `DogDuck`, `CatDuck`, `RobotDuck`
Classes with no common inheritance, each with a `.speak()` method.

#### `make_it_speak(obj)`
Duck typing function that calls `.speak()` on any object that has the method.

### Error-handling behaviour

- `Calculator.add()` raises `TypeError` if any argument is not a number (bool rejected).
- All classes validate inputs appropriately.

### Test results

`py -3.13 01-python-fundamentals/test_day18_polymorphism.py` → **all 15 tests passed**

| Test | Result |
|------|--------|
| Animal.make_sound returns generic sound | Pass |
| Dog.make_sound overrides Animal | Pass |
| Cat.make_sound overrides Animal | Pass |
| Cow.make_sound overrides Animal | Pass |
| animal_sound works polymorphically | Pass |
| animal_sound with multiple objects | Pass |
| Calculator.add no arguments | Pass |
| Calculator.add one argument | Pass |
| Calculator.add two arguments | Pass |
| Calculator.add three arguments | Pass |
| Calculator.add float arguments | Pass |
| Calculator.add rejects non-numeric | Pass |
| DogDuck.speak | Pass |
| CatDuck.speak | Pass |
| RobotDuck.speak | Pass |
| make_it_speak with any speaking object | Pass |
| make_it_speak with multiple objects | Pass |

---

## 2. DSA: Trapping Rain Water (Two Pointers)

File: `02-data-structures-algorithms/two-pointers/day18-trapping-rain-water.py`
Tests: `02-data-structures-algorithms/two-pointers/test_day18_trapping_rain_water.py`

### Implementation

`trap(height)` uses the two-pointers approach:

1. Start with `left = 0` and `right = len(height) - 1`.
2. Track `left_max` and `right_max` (highest bar seen from each side), both starting at 0.
3. While `left < right`:
   - If `height[left] < height[right]`:
     - If `height[left] >= left_max`, update `left_max = height[left]`.
     - Otherwise, `water += left_max - height[left]`.
     - Move `left` one step right.
   - Else:
     - If `height[right] >= right_max`, update `right_max = height[right]`.
     - Otherwise, `water += right_max - height[right]`.
     - Move `right` one step left.
4. Return the total water.

The key insight: always process the side with the smaller bar. Since the other side has a bar at least as tall, the water level at the current position is correctly bounded by the current side's max.

### Simple English explanation

Imagine standing on the leftmost bar with a friend on the rightmost bar. Whoever is on the shorter bar looks inward: "How much water can sit above me?" The answer depends on the tallest bar between you and the edge on your side (your max) and the fact that the other side has a bar at least as tall as yours. So you can safely calculate your trapped water using only your side's max. Then you move one step inward and repeat. When you meet in the middle, every bar has been checked exactly once.

### Complexity

- Time complexity: **O(n)** — each index is visited at most once.
- Space complexity: **O(1)** — only a few integer variables are used.

### Test results

`py -3.13 02-data-structures-algorithms/two-pointers/test_day18_trapping_rain_water.py` → **all 9 tests passed**

| Test case | Result |
|-----------|--------|
| [] -> 0 | Pass |
| [5] -> 0 | Pass |
| [1, 2, 3, 4] -> 0 | Pass |
| [4, 3, 2, 1] -> 0 | Pass |
| [3, 0, 2, 0, 4] -> 7 | Pass |
| [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> 6 | Pass |
| [2, 2, 2] -> 0 (equal heights) | Pass |
| [1, 2] -> 0 (two bars) | Pass |
| [4, 2, 0, 3, 2, 5] -> 9 (multiple sections) | Pass |
| Input list not modified | Pass |

---

## 3. Days 11-17 Status (unchanged)

Day 11, Day 12, Day 13, Day 14, Day 15, Day 16 and Day 17 files exist and their tests were verified passing in earlier sessions. They remain recorded as **learner practice pending** in `PROGRESS.md`. No changes were made to Days 11-17.

---

## 4. Day 18 completion status

- Python: OOP Polymorphism, Method Overloading and Method Overriding: implemented + tests verified passing (15 tests).
- DSA: Trapping Rain Water (Two Pointers): implemented + tests verified passing (9 tests).
- Learner practice: **pending** (the learner should solve the exercises independently before marking the day complete).

This follows the same convention used for Days 9-17: implementation and tests are verified, while learner practice remains pending.