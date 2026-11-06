"""
Day 11 — Data Structures & Algorithms: Valid Anagram

Topic: Strings — Anagram Detection with Dictionary Frequency Counting

Problem:
    Given two strings, determine whether they are anagrams.
    Two strings are anagrams if they contain the same characters
    with the same frequencies, just in a different order.

Approach — Dictionary Frequency Counting:
    1. If the strings have different lengths, they cannot be anagrams.
    2. Count character frequencies in the first string using a dictionary.
    3. Decrement counts using characters from the second string.
    4. If all counts return to zero, the strings are anagrams.

Time complexity: O(n) — one pass through each string.
Extra space complexity: O(k) — where k is the number of distinct characters.

Examples:
    is_anagram("listen", "silent") -> True
    is_anagram("hello", "world")   -> False
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car")       -> False
    is_anagram("a", "a")           -> True
    is_anagram("a", "ab")          -> False
"""


def is_anagram(s, t):
    """
    Determine whether two strings are anagrams.

    Uses a dictionary to count character frequencies in the first string,
    then decrements using characters from the second string.
    If all counts return to zero, the strings are anagrams.

    Does NOT use sorted() or compare sorted strings.

    Args:
        s: First string.
        t: Second string.

    Returns:
        True if s and t are anagrams, False otherwise.

    Example:
        is_anagram("listen", "silent") -> True
        is_anagram("hello", "world")   -> False
    """
    # Different lengths cannot be anagrams
    if len(s) != len(t):
        return False

    # Count character frequencies in s
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement counts using characters from t
    for char in t:
        if char not in char_count:
            # Character in t not present in s
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            # More occurrences in t than in s
            return False

    # All counts should be zero if strings are anagrams
    for count in char_count.values():
        if count != 0:
            return False

    return True


def main():
    print("=" * 60)
    print("Day 11 — DSA: Valid Anagram")
    print("=" * 60)
    print()

    examples = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True),
        ("a", "ab", False),
        ("", "", True),
    ]

    print("Examples:")
    print("-" * 60)
    for s, t, expected in examples:
        result = is_anagram(s, t)
        status = "OK" if result == expected else "FAIL"
        print(f'  is_anagram("{s}", "{t}") -> {result}  (expected: {expected})  [{status}]')

    print()
    print("How it works:")
    print("  1. If lengths differ, they cannot be anagrams -> return False.")
    print("  2. Count each character's frequency in s using a dictionary.")
    print("  3. For each character in t, decrement its count.")
    print("  4. If a character is missing or count goes negative -> False.")
    print("  5. If all counts return to zero -> True.")
    print()
    print("Time complexity:  O(n) — one pass through each string.")
    print("Extra space:      O(k) — k distinct characters stored in dictionary.")
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()