"""
Day 21 - Python Fundamentals: OOP Class Methods and Static Methods.

Topic: Class methods and static methods — two special kinds of methods in a
Python class, besides the regular instance methods.

This file teaches beginner-friendly class/static methods with a Student example:

  1. What are class methods?
     - Methods that belong to the class itself, not to any one object.
     - They can access and change class variables (data shared by all objects).
     - Marked with the @classmethod decorator.

  2. What is the cls parameter?
     - The first parameter of a class method. By convention it is named cls.
     - It refers to the class (just like self refers to the object/instance).
     - Python passes the class automatically when you call the method.

  3. What are static methods?
     - Methods that belong to the class but do not touch the class or the
       object at all. They are just plain functions grouped inside a class
     for organisation.
     - They take neither self nor cls.
     - Marked with the @staticmethod decorator.

  4. Difference between instance, class and static methods:
     - Instance method (def method(self, ...)): works on one object's data.
     - Class method (@classmethod def method(cls, ...)): works on class-level
       data shared by all objects.
     - Static method (@staticmethod def method(...)): does not use object or
       class data; a utility related to the class.

  5. When should we use each?
     - Instance method: when you need the object's own attributes (self).
     - Class method: when you need to read/change a class variable or create
       objects in a special way.
     - Static method: when you need a helper function that does not touch
       object or class state.

Practical program: Student class with a shared school_name, an instance method
to display student information, a class method to change the school name, and
a static method to check whether a student passed.
"""

# ============================================================================
# Class: Student
# ============================================================================


class Student:
    """A student in a school.

    Attributes:
        name: The student's name (unique to each student).
        score: The student's latest score (unique to each student).
    """

    # ------------------------------------------------------------------
    # Class variable: shared by every Student object.
    # Changing it affects all students (unless one overrides it).
    # ------------------------------------------------------------------
    school_name = "Green Valley School"

    # Pass mark used by the static method. Kept as a class variable so it is
    # easy to find and change in one place.
    pass_mark = 40

    def __init__(self, name, score):
        """Initialize a student with a name and a score.

        Args:
            name:   Student's name.
            score:  Student's score (0-100).
        """
        # Instance variables: belong to this object only.
        self.name = name
        self.score = score

    # ------------------------------------------------------------------
    # Instance method: works on one student's own data (self).
    # ------------------------------------------------------------------
    def display_info(self):
        """Print this student's name, score and school."""
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"School: {self.school_name}")

    # ------------------------------------------------------------------
    # Class method: works on class-level data (cls).
    # ------------------------------------------------------------------
    @classmethod
    def change_school_name(cls, new_name):
        """Change the school name for all students.

        Args:
            new_name: The new school name.

        cls refers to the Student class itself (like self refers to an object).
        """
        cls.school_name = new_name

    # ------------------------------------------------------------------
    # Static method: a utility that does not use self or cls.
    # ------------------------------------------------------------------
    @staticmethod
    def is_passed(score):
        """Check whether a score is a pass.


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 21 - Python Fundamentals: Class Methods and Static Methods")
    print("=" * 60)
    print()

    # --- Create multiple student objects ----------------------------------
    print("--- Create student objects ---")
    student1 = Student("Khalil", 85)
    student2 = Student("Aisha", 32)
    student3 = Student("Rehan", 70)

    # --- Instance method: display each student's own information -----------
    print("\n--- Instance method: student1.display_info() ---")
    student1.display_info()
    print("\n--- Instance method: student2.display_info() ---")
    student2.display_info()

    # --- Class variable access (shared by all students) --------------------
    print("\n--- Class variable: school_name (shared) ---")
    print(f"student1.school_name = {student1.school_name}")
    print(f"student2.school_name = {student2.school_name}")
    print(f"Student.school_name = {Student.school_name}")

    # --- Class method: change the school name for everyone -----------------
    print("\n--- Class method: Student.change_school_name('Sunrise High School') ---")
    Student.change_school_name("Sunrise High School")
    print(f"student1.school_name = {student1.school_name}")
    print(f"student2.school_name = {student2.school_name}")
    print(f"student3.school_name = {student3.school_name}")
    print(f"Student.school_name = {Student.school_name}")

    # --- Static method: pass/fail check (no object or class data needed) ---
    print("\n--- Static method: Student.is_passed(score) ---")
    print(f"student1 score {student1.score}: passed = {Student.is_passed(student1.score)}")
    print(f"student2 score {student2.score}: passed = {Student.is_passed(student2.score)}")
    print(f"student3 score {student3.score}: passed = {Student.is_passed(student3.score)}")
    print(f"Borderline score 40: passed = {Student.is_passed(40)}")
    print(f"Borderline score 39: passed = {Student.is_passed(39)}")

    # --- Call static method through an object (also works, not recommended) --
    print("\n--- Static method called through an object ---")
    print(f"student1.is_passed(90) = {student1.is_passed(90)}")

    print()
    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()
        Args:
            score: The score to check.

        Returns:
            True if score is greater than or equal to the pass mark, else False.
        """
        return score >= Student.pass_mark