"""
Day 13 - Python Fundamentals: File Handling (Read, Write, Append)

Topic: File Handling

This file teaches beginner-friendly file handling concepts with three exercises:

  1. save_student_details(filename, name, marks)
     - Writes student information to a file.
     - Uses `with open()` in write mode (`"w"`).

  2. read_file(filename)
     - Reads and returns the complete content of a file.
     - Handles `FileNotFoundError` gracefully.

  3. append_student_subject(filename, subject)
     - Appends a subject to an existing file.
     - Uses `with open()` in append mode (`"a"`), so existing content is
       never overwritten.

The `with` statement is used so the file is closed automatically, even if an
error occurs while reading or writing.

Learner practice is pending - completing the exercises yourself is required
to mark this day complete.
"""

# ============================================================================
# 1. EXERCISE 1: save_student_details(filename, name, marks)
# ============================================================================
# Write student information to a file using write mode ("w").
# Write mode creates the file if it does not exist and overwrites any
# existing content.


def save_student_details(filename, name, marks):
    """
    Save a student's name and marks to a file.

    Args:
        filename: Path to the file to write.
        name: The student's name.
        marks: The student's marks (can be a number or a string).

    Returns:
        None. The student details are written to the file.

    Example:
        save_student_details("student.txt", "Alice", 85)
        # File content becomes:
        # Student Details
        # Name: Alice
        # Marks: 85
    """
    with open(filename, "w") as file:
        # "w" = write mode. Creates the file if missing, overwrites if present.
        file.write("Student Details\n")
        file.write("Name: " + str(name) + "\n")
        file.write("Marks: " + str(marks) + "\n")


# ============================================================================
# 2. EXERCISE 2: read_file(filename)
# ============================================================================
# Read and return the complete content of a file.
# Handle FileNotFoundError so a missing file does not crash the program.


def read_file(filename):
    """
    Read and return the complete content of a file.

    Args:
        filename: Path to the file to read.

    Returns:
        The file content as a string if the file exists.
        If the file does not exist, returns a clear error message string
        instead of raising FileNotFoundError.

    Example:
        read_file("student.txt")   -> "Student Details\nName: Alice\nMarks: 85\n"
        read_file("missing.txt")   -> "Error: file 'missing.txt' not found."
    """
    try:
        with open(filename, "r") as file:
            # "r" = read mode. Reads the entire file content.
            return file.read()
    except FileNotFoundError:
        # Runs only when the file does not exist. Return a clear message
        # instead of letting the program crash.
        return "Error: file '" + filename + "' not found."


# ============================================================================
# 3. EXERCISE 3: append_student_subject(filename, subject)
# ============================================================================
# Append a subject to an existing file using append mode ("a").
# Append mode adds content to the end of the file without overwriting
# anything already in it.


def append_student_subject(filename, subject):
    """
    Append a subject to the end of a file without overwriting existing content.

    Args:
        filename: Path to the file to append to.
        subject: The subject text to append.

    Returns:
        None. The subject is appended to the file.

    Example:
        # If the file contains "Student Details\nName: Alice\nMarks: 85\n"
        append_student_subject("student.txt", "Math")
        # File content becomes:
        # Student Details
        # Name: Alice
        # Marks: 85
        # Subject: Math
    """
    with open(filename, "a") as file:
        # "a" = append mode. Adds content to the end of the file.
        # Existing content is preserved; nothing is overwritten.
        file.write("Subject: " + str(subject) + "\n")


# ============================================================================
# 4. DEMO
# ============================================================================


def main():
    demo_file = "day13_demo_student.txt"

    print("=" * 60)
    print("Day 13 - Python Fundamentals: File Handling")
    print("=" * 60)
    print()

    # --- Write student details ---
    print("--- save_student_details: write mode ---")
    save_student_details(demo_file, "Alice", 85)
    print(f"Wrote student details to '{demo_file}'.")
    print()

    # --- Read the file ---
    print("--- read_file: read mode ---")
    content = read_file(demo_file)
    print("File content:")
    print(content)

    # --- Append a subject ---
    print("--- append_student_subject: append mode ---")
    append_student_subject(demo_file, "Math")
    print(f"Appended subject 'Math' to '{demo_file}'.")
    print()

    # --- Read again to confirm previous content remains ---
    print("--- read_file after append (previous content preserved) ---")
    updated_content = read_file(demo_file)
    print("File content after appending:")
    print(updated_content)

    # --- Read a missing file ---
    print("--- read_file: missing file ---")
    missing = read_file("does_not_exist.txt")
    print(missing)

    print("=" * 60)
    print("Learner practice: complete the exercises yourself to mark Day 13 complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
