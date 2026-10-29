"""
Tests for Day 6 — student dictionary demo in day06-dictionaries.py.

These tests verify dictionary access, adding a new student, updating
existing marks, and looping through all names and marks.
"""

import importlib.util
import os

# Load day06-dictionaries.py by file path so the test works regardless of
# the current working directory when it is executed.
_module_path = os.path.join(os.path.dirname(__file__), "day06-dictionaries.py")
_spec = importlib.util.spec_from_file_location("day06_dictionaries", _module_path)
_day06_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_day06_module)

build_student_marks = _day06_module.build_student_marks
get_marks = _day06_module.get_marks
add_student = _day06_module.add_student
update_marks = _day06_module.update_marks
list_all_students = _day06_module.list_all_students


def test_access_student_marks():
    """Reading a student's marks from the dictionary works by name."""
    students = build_student_marks()
    assert get_marks(students, "Ali") == 85
    assert get_marks(students, "Sara") == 92
    assert get_marks(students, "John") == 78


def test_add_new_student():
    """A new student can be added to the dictionary."""
    students = build_student_marks()
    add_student(students, "Maria", 88)
    assert get_marks(students, "Maria") == 88


def test_update_existing_marks():
    """An existing student's marks can be updated."""
    students = build_student_marks()
    update_marks(students, "John", 81)
    assert get_marks(students, "John") == 81


def test_missing_student_returns_none():
    """Asking for a missing student returns None instead of crashing."""
    students = build_student_marks()
    assert get_marks(students, "Nobody") is None


def test_loop_through_all_students():
    """Looping with .items() visits every name and marks pair."""
    students = build_student_marks()
    lines = list_all_students(students)
    assert len(lines) == 3
    assert "Ali: 85" in lines
    assert "Sara: 92" in lines
    assert "John: 78" in lines


if __name__ == "__main__":
    test_access_student_marks()
    test_add_new_student()
    test_update_existing_marks()
    test_missing_student_returns_none()
    test_loop_through_all_students()
    print("All day06-dictionaries tests passed!")