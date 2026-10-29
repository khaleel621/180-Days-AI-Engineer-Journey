"""
Day 6 — Data Structures & Algorithms: Frequency Counting and Duplicate Detection

Topics:
- Dictionaries: count how often each value appears (frequency counting).
- Sets: store only unique values.
- Duplicate detection: find values that appear more than once.

Shortcuts such as list.count() or collections.Counter are intentionally
not used, so the counting pattern is shown explicitly with a loop
and a dictionary/set.
"""


def count_frequency(numbers):
    """
    Return a dictionary with the frequency of each number.

    Args:
        numbers: List of numbers.

    Returns:
        Dictionary mapping each number to how many times it appears.
        An empty list returns an empty dictionary.
    """
    frequency = {}  # start empty; fill it one number at a time

    for number in numbers:  # look at every number once
        if number in frequency:          # seen before? add one more
            frequency[number] += 1
        else:                            # first time seeing this number
            frequency[number] = 1

    return frequency


def show_frequency_changes(numbers):
    """
    Print the dictionary after each number is processed.
    Helpful for beginners to see how the dictionary grows.
    """
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
        print(f"After processing {number}: {frequency}")
    return frequency


def find_duplicates(numbers):
    """
    Return values that appear more than once.

    Each duplicate appears only once in the result, in the order in which
    the repetition is first detected.

    Args:
        numbers: List of numbers.

    Returns:
        List of duplicated values.
    """
    seen = set()              # values seen at least once
    duplicates = []           # duplicates, in order of first repeated detection
    already_recorded = set()  # duplicates already added to the result

    for number in numbers:
        if number in seen:
            # We have seen this number before -> it repeats.
            if number not in already_recorded:
                duplicates.append(number)
                already_recorded.add(number)
        else:
            seen.add(number)

    return duplicates


def sets_demo():
    """Show that a set keeps only unique values (display order is not guaranteed)."""
    numbers = [2, 5, 2, 8, 2, 5, 9]
    unique_numbers = set(numbers)
    print("Original list:", numbers)
    print("Unique values (set):", unique_numbers)
    return unique_numbers


def main():
    numbers = [2, 5, 2, 8, 2, 5, 9]

    print("=== Task B: Count Frequencies ===")
    frequency = count_frequency(numbers)
    print("Final frequency:", frequency)
    # Expected: {2: 3, 5: 2, 8: 1, 9: 1}

    print()
    print("=== Task C: Understand Sets ===")
    sets_demo()

    print()
    print("=== Task D: Detect Duplicates ===")
    print("Duplicates:", find_duplicates(numbers))
    # Expected: [2, 5]


if __name__ == "__main__":
    main()