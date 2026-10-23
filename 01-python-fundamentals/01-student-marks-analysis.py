"""
Student Marks Analysis Program
Day 1 — 2026-10-19
Python Fundamentals

This program stores student marks in a dictionary, calculates the average,
finds the topper (student with highest marks), and counts passed/failed students.
"""

# Store student marks in a dictionary: {student_name: marks}
student_marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 68,
    "Ethan": 55,
    "Fiona": 88,
    "George": 45,
    "Hannah": 79,
}

# Calculate average marks
total_marks = 0
for marks in student_marks.values():
    total_marks += marks

average_marks = total_marks / len(student_marks)

# Find the topper (student with the highest marks)
topper = None
highest_marks = -1
for name, marks in student_marks.items():
    if marks > highest_marks:
        highest_marks = marks
        topper = name

# Count passed and failed students (pass mark is 40)
passed = 0
failed = 0
for marks in student_marks.values():
    if marks >= 40:
        passed += 1
    else:
        failed += 1

# Display results
print("Student Marks Analysis")
print("=" * 30)
print(f"Student marks: {student_marks}")
print(f"Total students: {len(student_marks)}")
print(f"Average marks: {average_marks:.2f}")
print(f"Topper: {topper} with {highest_marks} marks")
print(f"Passed students: {passed}")
print(f"Failed students: {failed}")