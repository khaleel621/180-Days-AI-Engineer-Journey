"""
Tests for Day 13 - File Handling in
01-python-fundamentals/day13-file-handling.py.

Covers: save_student_details (write mode), read_file (read mode and
FileNotFoundError handling), append_student_subject (append mode without
overwriting existing content).

Temporary files are used so that no existing user files are modified.
"""

import importlib.util
import os
import tempfile

# Load day13-file-handling.py by file path so the test works regardless
# of the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day13-file-handling.py")
_spec = importlib.util.spec_from_file_location("day13_file_handling", _module_path)
_day13_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day13_module)

save_student_details = _day13_module.save_student_details
read_file = _day13_module.read_file
append_student_subject = _day13_module.append_student_subject


def _temp_file_path():
    """Create a temporary file path and return it. The file is deleted."""
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    return path


def _remove_file(path):
    """Remove a file if it exists, ignoring errors."""
    try:
        os.remove(path)
    except OSError:
        pass


# ------------------------------------------------------------
# save_student_details + read_file tests
# ------------------------------------------------------------


def test_save_and_read_student_details():
    """Writing student details then reading them back should preserve name
    and marks."""
    path = _temp_file_path()
    try:
        save_student_details(path, "Alice", 85)
        content = read_file(path)
        assert "Alice" in content
        assert "85" in content
        assert "Student Details" in content
        assert "Name: Alice" in content
        assert "Marks: 85" in content
    finally:
        _remove_file(path)


def test_save_student_details_overwrites():
    """Write mode overwrites any existing content instead of appending."""
    path = _temp_file_path()
    try:
        save_student_details(path, "Bob", 90)
        save_student_details(path, "Carol", 78)
        content = read_file(path)
        assert "Carol" in content
        assert "78" in content
        assert "Bob" not in content
    finally:
        _remove_file(path)


def test_read_existing_file():
    """Reading an existing file returns its complete content."""
    path = _temp_file_path()
    try:
        with open(path, "w") as file:
            file.write("Hello, file handling!\n")
        content = read_file(path)
        assert content == "Hello, file handling!\n"
    finally:
        _remove_file(path)


def test_read_missing_file():
    """Reading a missing file must not crash; a clear message is returned."""
    path = _temp_file_path()
    _remove_file(path)  # ensure the file does not exist
    result = read_file(path)
    assert isinstance(result, str)
    assert "not found" in result.lower()
    assert path in result


# ------------------------------------------------------------
# append_student_subject tests
# ------------------------------------------------------------


def test_append_student_subject():
    """Appending a subject adds it to the end of the file."""
    path = _temp_file_path()
    try:
        save_student_details(path, "Alice", 85)
        append_student_subject(path, "Math")
        content = read_file(path)
        assert "Math" in content
        assert "Subject: Math" in content
    finally:
        _remove_file(path)


def test_append_preserves_previous_content():
    """Appending must not overwrite existing content: the student details
    written earlier must still be present after appending."""
    path = _temp_file_path()
    try:
        save_student_details(path, "Alice", 85)
        append_student_subject(path, "Math")
        append_student_subject(path, "Science")
        content = read_file(path)
        assert "Alice" in content
        assert "85" in content
        assert "Math" in content
        assert "Science" in content
        # Math was appended before Science, so Math appears first.
        math_index = content.index("Math")
        science_index = content.index("Science")
        assert math_index < science_index
    finally:
        _remove_file(path)


def test_append_to_empty_file():
    """Appending to an empty file adds the subject without crashing."""
    path = _temp_file_path()
    try:
        with open(path, "w") as file:
            file.write("")
        append_student_subject(path, "History")
        content = read_file(path)
        assert "Subject: History" in content
    finally:
        _remove_file(path)


if __name__ == "__main__":
    test_save_and_read_student_details()
    test_save_student_details_overwrites()
    test_read_existing_file()
    test_read_missing_file()
    test_append_student_subject()
    test_append_preserves_previous_content()
    test_append_to_empty_file()

    print("All day13-file-handling tests passed!")
