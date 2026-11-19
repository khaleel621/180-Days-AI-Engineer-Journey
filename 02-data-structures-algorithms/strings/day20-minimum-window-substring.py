"""
Day 20 - Data Structures & Algorithms: Minimum Window Substring.

Topic: Sliding Window + Frequency Dictionary.

Problem:
Given two strings s and t, find the smallest (shortest) substring of s that
contains all characters of t, including duplicate character requirements.

Example:
    s = "ADOBECODEBANC"
    t = "ABC"
    Output: "BANC"

If no such substring exists, return an empty string "".

Approach — sliding window with two frequency dictionaries:

  1. Build a frequency dictionary need for string t (how many of each
     character the window must contain).
  2. Expand the right end of the window over s, adding characters to a
     window_counts dictionary.
  3. Track formed: how many distinct characters have met their required
     count in the current window.
  4. When formed == required (all needed characters are satisfied), the
     window is valid. Record it if it is smaller than the best seen so far.
  5. Shrink the window from the left while it stays valid, to find the
     smallest valid window starting at the current left.
  6. Continue expanding the right end until the end of s.

Duplicate characters in t are handled because need stores exact counts and
formed only increases when a character's count in the window reaches its
required count (not merely when it appears).

Time complexity:  O(|s| + |t|) — each character of s is visited at most
twice (once by right, once by left), and t is traversed once.
Space complexity: O(|s| + |t|) in the worst case for the two dictionaries
(bounded by the number of distinct characters).
"""

# ============================================================================
# Solution
# ============================================================================


def min_window(s, t):
    """Return the smallest substring of s containing all characters of t.

    Args:
        s: The string to search in.
        t: The string whose characters (with duplicates) must be covered.

    Returns:
        The shortest valid substring of s, or "" if no such window exists.
    """
    # --- Edge cases: empty input or t longer than s --------------------
    if not s or not t:
        return ""
    if len(t) > len(s):
        return ""

    # --- 1. Frequency dictionary for t (the requirement) ---------------
    # need[char] = how many times char must appear in the window.
    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1

    # Number of distinct characters that must be satisfied.
    required = len(need)

    # --- 2. Sliding window state ----------------------------------------
    window_counts = {}   # frequency of characters inside the current window
    formed = 0           # how many distinct chars meet their required count
    left = 0             # left edge of the window

    # Best answer: (window_length, left_index, right_index)
    # Use infinity so any real window is smaller.
    best = (float("inf"), None, None)

    # --- 3. Expand the right edge of the window -------------------------
    for right, char in enumerate(s):
        # Add the new character to the window.
        window_counts[char] = window_counts.get(char, 0) + 1

        # If this character is needed and its count now matches the
        # requirement exactly, one more distinct character is satisfied.
        if char in need and window_counts[char] == need[char]:
            formed += 1

        # --- 4. While the window is valid, try to shrink from the left --
        while left <= right and formed == required:
            window_length = right - left + 1

            # Record this window if it is the smallest seen so far.
            if window_length < best[0]:
                best = (window_length, left, right)

            # Remove the leftmost character and move left edge rightward.
            left_char = s[left]
            window_counts[left_char] -= 1

            # If removing it breaks a requirement, the window is no longer
            # valid and we must stop shrinking.
            if left_char in need and window_counts[left_char] < need[left_char]:
                formed -= 1

            left += 1

    # --- 5. Return result -----------------------------------------------
    if best[0] == float("inf"):
        # No valid window was ever found.
        return ""
    return s[best[1]: best[2] + 1]


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 20 - DSA: Minimum Window Substring (Sliding Window)")
    print("=" * 60)
    print()

    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),        # normal example
        ("a", "a", "a"),                          # single-character match
        ("a", "aa", ""),                          # t longer than s -> no window
        ("ABC", "ABC", "ABC"),                    # exact match
        ("aabbcc", "aabc", "aabbc"),              # duplicates in t
        ("ABCDEF", "G", ""),                      # no valid window
        ("", "A", ""),                            # empty s
        ("A", "", ""),                            # empty t
    ]

    for s, t, expected in test_cases:
        result = min_window(s, t)
        status = "OK" if result == expected else "FAIL"
        print(f"min_window(s={s!r}, t={t!r}) = {result!r} "
              f"(expected {expected!r})  [{status}]")
        assert result == expected, f"Expected {expected!r}, got {result!r}"

    print()
    print("Time complexity:  O(|s| + |t|)")
    print("Space complexity: O(|s| + |t|)")
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()