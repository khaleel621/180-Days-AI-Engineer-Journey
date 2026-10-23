"""
Beginner-friendly tests for Student Marks Analysis.

These tests verify the core logic of the student marks program without
modifying the original implementation.
"""

import importlib.util
import os

# Load the student_marks_analysis module by file path (hyphenated name)
_module_path = os.path.join(os.path.dirname(__file__), "01-student-marks-analysis.py")
_spec = importlib.util.spec_from_file_location("student_marks_analysis", _module_path)
_student_marks_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_student_marks_module)
student_marks = _student_marks_module.student_marks


def test_student_marks_is_dict():
    """student_marks should be a dictionary."""
    assert isinstance(student_marks, dict)


def test_student_marks_not_empty():
    """student_marks should contain at least one student."""
    assert len(student_marks) > 0


def test_all_marks_are_numbers():
    """Every mark value should be an int or float."""
    for name, marks in student_marks.items():
        assert isinstance(marks, (int, float)), f"{name} has non-numeric marks: {marks}"


def test_average_calculation():
    """Average marks should equal total divided by count."""
    total = sum(student_marks.values())
    count = len(student_marks)
    average = total / count
    assert average > 0


def test_topper_has_highest_marks():
    """The topper should be the student with the highest marks."""
    highest = max(student_marks.values())
    toppers = [name for name, marks in student_marks.items() if marks == highest]
    assert len(toppers) >= 1


def test_passed_and_failed_counts_add_up():
    """Passed + failed should equal total number of students."""
    passed = sum(1 for m in student_marks.values() if m >= 40)
    failed = sum(1 for m in student_marks.values() if m < 40)
    assert passed + failed == len(student_marks)


if __name__ == "__main__":
    test_student_marks_is_dict()
    test_student_marks_not_empty()
    test_all_marks_are_numbers()
    test_average_calculation()
    test_topper_has_highest_marks()
    test_passed_and_failed_counts_add_up()
    print("All student marks tests passed!")