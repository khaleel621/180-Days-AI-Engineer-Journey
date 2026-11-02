# Day 8 — Bubble Sort vs Selection Sort (Comparison)

This document compares the two sorting algorithms practiced on Day 8
(Python + DSA day counter, separate from the 180-day AI Engineer journey).

## 1. What Sorting Means

Sorting means arranging the elements of a list in a specific order —
usually ascending (smallest to largest) or descending (largest to smallest).
Sorted data is easier to search, analyze, and display.

## 2. Bubble Sort

**How it works:**
- Start at the beginning of the list.
- Compare each pair of adjacent elements.
- If the left element is greater than the right element, swap them.
- Repeat this process for multiple passes through the list.
- After each pass, the largest unsorted element "bubbles up" to its
  correct position at the end.

**Optimization:**
- A swap flag tracks whether any swap occurred during a pass.
- If a full pass completes with zero swaps, the list is already sorted
  and the algorithm stops early. This gives a best-case time of O(n).

**Example:**
```python
numbers = [5, 3, 8, 1, 2]
# Pass 1: compare 5 and 3 -> swap -> [3, 5, 8, 1, 2]
#         compare 5 and 8 -> no swap
#         compare 8 and 1 -> swap -> [3, 5, 1, 8, 2]
#         compare 8 and 2 -> swap -> [3, 5, 1, 2, 8]
# Pass 2: ... continue until no swaps remain
# Result: [1, 2, 3, 5, 8]
```

**Does it require sorted data?** No. Works on any list.

**Time complexity:**
- Best case: O(n) — list is already sorted (optimized version stops early).
- Average case: O(n²).
- Worst case: O(n²) — list is reverse-sorted.

**Auxiliary space complexity:** O(n) when returning a new list, or O(1)
if sorting in-place (this implementation returns a new list).

---

## 3. Selection Sort

**How it works:**
- Divide the list into a sorted part (left) and an unsorted part (right).
- Initially, the sorted part is empty and the unsorted part is the whole list.
- Find the smallest element in the unsorted part.
- Swap it with the first element of the unsorted part (the boundary).
- Move the boundary one step to the right and repeat.

**Example:**
```python
numbers = [64, 25, 12, 22, 11]
# Find smallest in [64, 25, 12, 22, 11] -> 11 at index 4
# Swap 64 and 11 -> [11, 25, 12, 22, 64]
# Find smallest in [25, 12, 22, 64] -> 12 at index 2
# Swap 25 and 12 -> [11, 12, 25, 22, 64]
# Find smallest in [25, 22, 64] -> 22 at index 3
# Swap 25 and 22 -> [11, 12, 22, 25, 64]
# Find smallest in [25, 64] -> 25 at index 3 (already in place)
# Result: [11, 12, 22, 25, 64]
```

**Does it require sorted data?** No. Works on any list.

**Time complexity:**
- Best case: O(n²) — always scans the full unsorted portion even if sorted.
- Average case: O(n²).
- Worst case: O(n²).

**Auxiliary space complexity:** O(n) when returning a new list, or O(1)
if sorting in-place (this implementation returns a new list).

---

## 4. Comparison Table

| Algorithm               | Best Case | Average Case | Worst Case |
| ----------------------- | --------- | ------------ | ---------- |
| Bubble Sort (optimized) | O(n)      | O(n²)        | O(n²)      |
| Selection Sort          | O(n²)     | O(n²)        | O(n²)      |

**Key differences:**
- **Bubble sort** compares and swaps adjacent elements. It can stop early
  if no swaps occur (best case O(n)).
- **Selection sort** finds the minimum element in the unsorted portion and
  places it at the boundary. It always scans the full unsorted portion,
  so even a sorted list takes O(n²).
- **Bubble sort** can make many swaps; **selection sort** makes at most
  n−1 swaps (one per pass), which can be useful when swaps are expensive.

---

## 5. Why Sorting Is Useful

- **Searching:** Binary search requires sorted data.
- **Finding extremes:** The smallest or largest element is at the ends.
- **Removing duplicates:** Duplicate values become adjacent after sorting.
- **Data analysis:** Sorted data makes it easier to compute medians,
  percentiles, and ranges.
- **User interfaces:** Sorted lists are easier for people to read.

---

## 6. Files

- `day08-bubble-sort.py` — bubble sort implementation and demo.
- `day08-selection-sort.py` — selection sort implementation and demo.
- `test_day08-bubble-sort.py` — tests for bubble sort.
- `test_day08-selection-sort.py` — tests for selection sort.