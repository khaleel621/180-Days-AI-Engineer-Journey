"""
Tests for Day 21 - OOP Class Methods and Static Methods in
01-python-fundamentals/day21-class-and-static-methods.py.

Covers:
  - Student object creation with name and score.
  - Instance variables belong to each object (name, score).
  - Class variable school_name is shared by all students.
  - Class method change_school_name() updates the school for all students.
  - Static method is_passed(score) checks pass/fail without self or cls.
  - Instance method display_info() shows one student's own data.
  - Multiple student objects are independent.
  - Pass/fail boundary (pass mark 40).

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day21-class-and-static-methods.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day21-class-and-static-methods.py")
_spec = importlib.util.spec_from_file_location("day21_class_and_static_methods", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Student = _module.Student


def _make_student(name, score):
    return Student(name, score)


# -----------------------------------------------------------
# Object creation
# -----------------------------------------------------------

def test_student_creation():
    """A Student object stores its own name and score."""
    student = _make_student("Khalil", 85)
    assert student.name == "Khalil"
    assert student.score == 85


def test_student_objects_are_independent():
    """Each student keeps its own name and score."""
    s1 = _make_student("Khalil", 85)
    s2 = _make_student("Aisha", 32)
    assert s1.name == "Khalil"
    assert s1.score == 85
    assert s2.name == "Aisha"
    assert s2.score == 32


# -----------------------------------------------------------
# Class variable access
# -----------------------------------------------------------

def test_class_variable_is_shared():
    """school_name is a class variable shared by all students."""
    s1 = _make_student("Khalil", 85)
    s2 = _make_student("Aisha", 32)
    assert s1.school_name == "Green Valley School"
    assert s2.school_name == "Green Valley School"
    assert Student.school_name == "Green Valley School"


# -----------------------------------------------------------
# Class method: change school name
# -----------------------------------------------------------

def test_change_school_name_updates_all_students():
    """The class method changes school_name for every student."""
    s1 = _make_student("Khalil", 85)
    s2 = _make_student("Aisha", 32)
    Student.change_school_name("Sunrise High School")
    assert s1.school_name == "Sunrise High School"
    assert s2.school_name == "Sunrise High School"
    assert Student.school_name == "Sunrise High School"


# -----------------------------------------------------------
# Static method: pass / fail
# -----------------------------------------------------------

def test_is_passed_above_pass_mark():
    """is_passed() returns True for a score at or above the pass mark."""
    assert Student.is_passed(85) is True
    assert Student.is_passed(40) is True  # boundary: exactly the pass mark


def test_is_passed_below_pass_mark():
    """is_passed() returns False for a score below the pass mark."""
    assert Student.is_passed(32) is False
    assert Student.is_passed(39) is False
    assert Student.is_passed(0) is False


def test_static_method_via_object():
    """A static method can also be called through an object (not recommended)."""
    student = _make_student("Khalil", 90)
    assert student.is_passed(90) is True
    assert student.is_passed(20) is False


# -----------------------------------------------------------
# Instance method: display info
# -----------------------------------------------------------

def test_display_info_runs_without_error():
    """display_info() should execute and use the object's own data."""
    student = _make_student("Khalil", 85)
    # Simply calling it must not raise; it prints to stdout.
    student.display_info()
    assert student.name == "Khalil"
    assert student.score == 85


if __name__ == "__main__":
    test_student_creation()
    test_student_objects_are_independent()
    test_class_variable_is_shared()
    test_change_school_name_updates_all_students()
    test_is_passed_above_pass_mark()
    test_is_passed_below_pass_mark()
    test_static_method_via_object()
    test_display_info_runs_without_error()
    print("All test_day21_class_and_static_methods tests passed!")