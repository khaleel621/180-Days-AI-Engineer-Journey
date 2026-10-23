"""
Two Sum — Nested Loop Approach
Day 2 — 2026-10-20
Data Structures & Algorithms (Arrays)

Problem:
Given an array of integers and a target value, find two distinct indices
i and j such that nums[i] + nums[j] == target.

Approach: Nested loops (brute force)
- Outer loop picks the first element (index i).
- Inner loop picks the second element (index j), starting at i + 1.
- j starts at i + 1 to avoid:
    * Using the same element twice (i == j)
    * Checking duplicate pairs (e.g., (i, j) and (j, i))
- If a pair sums to the target, return the indices and break out of the loops.
- A found flag is used to break out of both the inner and outer loops.
"""

def two_sum(nums, target):
    """
    Find two indices whose values add up to the target using nested loops.

    Args:
        nums: List of integers.
        target: Target sum.

    Returns:
        Tuple of (i, j) indices if found, otherwise None.
    """
    found = False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                found = True
                break
        if found:
            break

    if found:
        return i, j
    return None


# Example input and output
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    result = two_sum(nums, target)

    print(f"Input: nums = {nums}, target = {target}")
    if result:
        print(f"Output: indices {result}")
        print(f"Explanation: nums[{result[0]}] + nums[{result[1]}] = "
              f"{nums[result[0]]} + {nums[result[1]]} = {target}")
    else:
        print("Output: No solution found")

    """
    Time Complexity: O(n^2)
    - Outer loop runs n times.
    - Inner loop runs up to n - 1 times for each outer iteration.
    - Total comparisons: (n-1) + (n-2) + ... + 1 = n*(n-1)/2
    - Quadratic time complexity.

    Space Complexity: O(1)
    - Only a fixed number of variables (i, j, found) are used,
      regardless of input size.
    """