"""
Day 11 — Python Fundamentals: Dictionary Methods and Frequency Counting

Topic: Dictionaries

This file teaches beginner-friendly dictionary concepts with examples,
plus two practice exercises:
  1. calculate_total_marks(marks)
  2. character_frequency(text)

Learner practice is pending — completing the exercises yourself is required
to mark this day complete.
"""

# ============================================================================
# 1. WHAT IS A DICTIONARY?
# ============================================================================
# A dictionary is a collection of key-value pairs.
# "Key" is like a label, and "value" is the data attached to that label.
# Dictionaries are written with curly braces {}.
# Each key must be unique, and keys are separated from values by a colon :.

# ============================================================================
# 2. CREATING DICTIONARIES
# ============================================================================

# Empty dictionary
empty_dict = {}

# Dictionary with key-value pairs (string keys, integer values)
student_marks = {
    "Maths": 85,
    "Python": 90,
    "English": 75
}

# Dictionary with string keys and string values
capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi"
}

# Dictionary with mixed value types
person = {
    "name": "Alice",
    "age": 25,
    "city": "London",
    "is_student": True
}

# ============================================================================
# 3. ACCESSING DICTIONARY VALUES
# ============================================================================

# Use square brackets with the key
print(student_marks["Maths"])      # 85
print(student_marks["Python"])     # 90
print(student_marks["English"])    # 75

# Using .get() — returns None if key is missing (safer than [])
print(student_marks.get("Maths"))   # 85
print(student_marks.get("Science")) # None (key does not exist)

# .get() with a default value
print(student_marks.get("Science", 0))  # 0 (default when key is missing)

# ============================================================================
# 4. ADDING AND UPDATING VALUES
# ============================================================================

# Add a new key-value pair
student_marks["Science"] = 88
print(student_marks["Science"])  # 88

# Update an existing value
student_marks["Maths"] = 95
print(student_marks["Maths"])    # 95

# Using .update() to add or update multiple items at once
student_marks.update({"History": 80, "Geography": 82})
print(student_marks["History"])   # 80
print(student_marks["Geography"]) # 82

# ============================================================================
# 5. REMOVING DICTIONARY ENTRIES
# ============================================================================

# Using .pop() — removes a key and returns its value
removed_value = student_marks.pop("History")
print(removed_value)   # 80
# "History" is no longer in student_marks

# Using del keyword
del student_marks["Geography"]
# "Geography" is no longer in student_marks

# ============================================================================
# 6. keys() — Get all keys
# ============================================================================

for subject in student_marks.keys():
    print(subject)     # Maths, Python, English, Science

# ============================================================================
# 7. values() — Get all values
# ============================================================================

for mark in student_marks.values():
    print(mark)        # 95, 90, 75, 88

# ============================================================================
# 8. items() — Get all key-value pairs
# ============================================================================

for subject, mark in student_marks.items():
    print(f"{subject}: {mark}")
    # Maths: 95
    # Python: 90
    # English: 75
    # Science: 88

# ============================================================================
# 9. Dictionary iteration
# ============================================================================

# Iterating over a dictionary directly iterates over its keys
for subject in student_marks:
    print(subject)     # Maths, Python, English, Science

# ============================================================================
# 10. Frequency counting with dictionaries
# ============================================================================

def character_frequency(text):
    """
    Count how many times each character appears in a string.

    Uses a dictionary where keys are characters and values are counts.

    Args:
        text: A string to count characters in.

    Returns:
        A dictionary mapping each character to its frequency.

    Example:
        character_frequency("banana")
        -> {"b": 1, "a": 3, "n": 2}
    """
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

def calculate_total_marks(marks):
    """
    Calculate the total of all marks in a dictionary.

    Args:
        marks: A dictionary mapping subject names to marks (integers).

    Returns:
        The sum of all marks as an integer.

    Example:
        calculate_total_marks({
            "Maths": 85,
            "Python": 90,
            "English": 75
        })
        -> 250
    """
    total = 0
    for mark in marks.values():
        total += mark
    return total


def main():
    print("=" * 60)
    print("Day 11 — Python Fundamentals: Dictionary Methods and Frequency Counting")
    print("=" * 60)
    print()

    # --- Creating dictionaries ---
    print("--- Creating Dictionaries ---")
    print(f"empty_dict: {empty_dict}")
    print(f"student_marks: {student_marks}")
    print(f"capitals: {capitals}")
    print(f"person: {person}")
    print()

    # --- Accessing values ---
    print("--- Accessing Values ---")
    print(f'student_marks["Maths"] = {student_marks["Maths"]}')
    print(f'student_marks.get("Python") = {student_marks.get("Python")}')
    print(f'student_marks.get("Science", 0) = {student_marks.get("Science", 0)}')
    print()

    # --- Adding and updating ---
    print("--- Adding and Updating ---")
    student_marks["Science"] = 88
    print(f'After student_marks["Science"] = 88: {student_marks["Science"]}')
    student_marks["Maths"] = 95
    print(f'After student_marks["Maths"] = 95: {student_marks["Maths"]}')
    student_marks.update({"History": 80, "Geography": 82})
    print(f'After update: {student_marks}')
    print()

    # --- Removing entries ---
    print("--- Removing Entries ---")
    removed = student_marks.pop("History")
    print(f'popped "History": {removed}')
    del student_marks["Geography"]
    print(f'After removals: {student_marks}')
    print()

    # --- keys(), values(), items() ---
    print("--- keys(), values(), items() ---")
    print(f"keys: {list(student_marks.keys())}")
    print(f"values: {list(student_marks.values())}")
    print(f"items: {list(student_marks.items())}")
    print()

    # --- Dictionary iteration ---
    print("--- Dictionary Iteration ---")
    for subject in student_marks:
        print(f"  {subject}: {student_marks[subject]}")
    print()

    # --- Frequency counting ---
    print("--- Frequency Counting ---")
    print(f'character_frequency("banana") = {character_frequency("banana")}')
    print()

    # --- Exercise 1 demo ---
    print("--- Exercise 1: calculate_total_marks ---")
    marks_example = {
        "Maths": 85,
        "Python": 90,
        "English": 75
    }
    print(f'calculate_total_marks({marks_example}) = {calculate_total_marks(marks_example)}')
    print()

    # --- Exercise 2 demo ---
    print("--- Exercise 2: character_frequency ---")
    print(f'character_frequency("banana") = {character_frequency("banana")}')
    print()

    print("=" * 60)
    print("Learner practice: complete the exercises yourself to mark Day 11 complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()