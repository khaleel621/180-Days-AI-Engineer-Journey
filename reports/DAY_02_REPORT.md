# Day 2 Report — Conditions, Loops & Problem-Solving

## 1. Topic and Objectives

- **Day:** Day 2 practice continuation; work and verification recorded on 2026-10-25.
- Use conditions and the modulus operator to classify integers as even or odd.
- Use a loop to print a multiplication table from 1 through 10.
- Count even values using a loop, condition, and counter.

The repository already records other Day 2 work (Two Sum and machine learning). This report covers only the requested conditions and loops exercises.

## 2. Concepts Practiced

- `%` (modulus) gives the remainder after division. An integer is even when `number % 2 == 0`; this also works for zero and negative integers.
- `if` conditions choose what to do based on a check.
- `for` and `range(1, 11)` repeat the table calculation for 1 through 10. The stop value 11 is excluded by `range`.
- A counter starts at zero and increases when a value meets the condition.
- A single pass through a list takes O(n) time; the counter uses O(1) extra space.

## 3. Problems Attempted and Approach

1. **Even or odd:** `even_or_odd(number)` checks whether the remainder after division by two is zero, then returns a clear result. Zero is even, and negative integers are handled by the same rule.
2. **Multiplication table:** `multiplication_table(number)` uses a `for` loop over 1 through 10 and builds one result line per multiplier.
3. **Count even numbers:** `count_even_numbers(numbers)` initializes `even_count` to zero, checks each number with an `if` condition, and increments the counter for each even value. It does not use `count()`.

The example list `[12, 7, 4, 9, 6, 3, 8]` produces `Even numbers count: 4`.

## 4. Complexity of the DSA Solution

For a list of n values, `count_even_numbers` checks each value once: **O(n) time**. It stores only the counter and current loop value, regardless of list size: **O(1) extra space**.

## 5. Tests and Actual Results

Executed `python practice/test_day02_loops.py` on 2026-10-25. **All 5 test functions passed** (exit code 0). Coverage included:

- Positive even and odd integers.
- Zero and positive/negative even and odd values.
- Tables for positive and negative inputs, each with 10 rows from multiplier 1 through 10.
- The given list, an empty list, an all-even list, and an all-odd list.

Also ran the interactive program with sample inputs `0` and `-3` using `"0`n-3" | python practice/day02_loops.py`. It exited with code 0, reported zero as even, printed the -3 table through 10, and printed `Even numbers count: 4`.

An initial interactive run without supplied input ended with `EOFError`; a first PowerShell input attempt used a literal newline marker and failed parsing. The corrected input run above succeeded. These were invocation issues, not failed test cases.

## 6. What I Learned

- Checking a remainder with `% 2` works for negative values and zero as well as positive values.
- `range(1, 11)` is a convenient way to repeat an operation ten times.
- A counter is a direct way to count matching values as a list is visited once.

## 7. Remaining Work

- The requested three exercises and their tests are implemented and verified.
- No Day 3 or later work was started.
- Review the changes before any later GitHub upload. No commit or push was made.
