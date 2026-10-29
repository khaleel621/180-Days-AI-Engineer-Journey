"""
Day 6 — Python Fundamentals: Dictionaries

Topic: Store related data in key/value pairs using a dictionary.

Exercise A: Store student names and marks in a dictionary, then access,
            add a new student, update existing marks, and loop through
            all names and marks.
"""


def build_student_marks():
    """Create a dictionary mapping student names to their marks."""
    students = {
        "Ali": 85,
        "Sara": 92,
        "John": 78,
    }
    return students


def get_marks(students, name):
    """Return the marks for a student, or None if the student is missing."""
    if name in students:
        return students[name]
    return None


def add_student(students, name, marks):
    """Add a new student and their marks to the dictionary."""
    students[name] = marks


def update_marks(students, name, marks):
    """Update an existing student's marks. Does nothing if the student is missing."""
    if name in students:
        students[name] = marks


def list_all_students(students):
    """Return a list of "name: marks" strings, one per student."""
    result = []
    for name, marks in students.items():
        result.append(f"{name}: {marks}")
    return result


def student_marks_demo():
    """Run the beginner demonstration and print each step."""
    students = build_student_marks()

    # Access a student's marks.
    print("Ali's marks:", get_marks(students, "Ali"))

    # Add a new student.
    add_student(students, "Maria", 88)

    # Update existing marks.
    update_marks(students, "John", 81)

    # Loop through student names and marks.
    for line in list_all_students(students):
        print(line)

    return students


def main():
    student_marks_demo()


if __name__ == "__main__":
    main()