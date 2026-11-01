# Day 7 — Linear Search vs Binary Search (Comparison)

This document compares the two searching algorithms practiced on Day 7
(Python + DSA day counter, separate from the 180-day AI Engineer journey).

## 1. Linear Search

**How it works:**
- Start at the first element (index 0).
- Compare each element with the target, one by one, using a `for` loop.
- If an element equals the target, return its index.
- If the end of the list is reached without a match, return `-1`.

**Example:**
```python
numbers = [10, 20, 30, 40, 50]
target = 30
# 10 != 30, 20 != 30, 30 == 30 -> found at index 2
```

**Does it require sorted data?** No. Linear search works on any list,
sorted or unsorted.

**Time complexity:**
- Best case: O(1) — target is the first element.
- Average case: O(n).
- Worst case: O(n) — target is the last element or not present.

---

## 2. Binary Search

**How it works:**
- Requires the list to be sorted (ascending order).
- Keep a search range defined by `low` and `high`.
- Repeatedly check the middle element (`mid = (low + high) // 2`):
    - If `numbers[mid] == target`, return `mid`.
    - If `numbers[mid] < target`, discard the left half: `low = mid + 1`.
    - If `numbers[mid] > target`, discard the right half: `high = mid - 1`.
- Stop when `low > high`; the target is not present, return `-1`.

**Example:**
```python
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50
# mid = 3 -> 40 < 50, search right half
# mid = 5 -> 60 > 50, search left half
# mid = 4 -> 50 == 50 -> found at index 4
```

**Does it require sorted data?** Yes. Binary search decides which half to
discard by comparing with the middle element, which only makes sense if
the list is sorted. On an unsorted list it can miss the target or return
a wrong index.

**Time complexity:**
- Best case: O(1) — target is the middle element.
- Average case: O(log n).
- Worst case: O(log n) — each step halves the search range.

---

## 3. Comparison Table

| Algorithm     | Best Case | Average Case | Worst Case | Requires Sorted Data? |
| ------------- | --------- | ------------ | ---------- | --------------------- |
| Linear Search | O(1)      | O(n)         | O(n)       | No                    |
| Binary Search | O(1)      | O(log n)     | O(log n)   | Yes                   |

---

## 4. When to Use Which

- Use **linear search** for small lists, unsorted lists, or when you
  only need to search once.
- Use **binary search** for large sorted lists, or when you will search
  the same sorted list many times (the cost of sorting once pays off).

---

## 5. Files

- `day07-linear-search.py` — linear search implementation and demo.
- `day07-binary-search.py` — binary search implementation and demo.
- `test_day07-linear-search.py` — tests for linear search.
- `test_day07-binary-search.py` — tests for binary search.
