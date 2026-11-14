"""
Day 16 - Python Fundamentals: OOP — Inheritance, Method Overriding and super().

Topic: Inheritance, Method Overriding and super()

This file teaches beginner-friendly inheritance with parent and child classes:

  1. Employee(name, salary)                                    (parent class)
     - Stores the employee's name and salary.
     - display_details() prints the name and salary.

  2. Manager(Employee)                                         (child class)
     - Inherits name and salary from Employee.
     - Adds a department.
     - Uses super().__init__(name, salary) to let Employee initialize the
       inherited parts.
     - Overrides display_details() to also print the department.

  3. Animal                                                    (parent class)
     - make_sound() returns a generic sound.

  4. Dog(Animal)                                               (child class)
     - Overrides make_sound() to return "Woof!".

  5. Cat(Animal)                                               (child class)
     - Overrides make_sound() to return "Meow!".

  6. Shape                                                     (parent class)
     - area() returns 0 by default (no dimensions yet).

  7. Rectangle(Shape)                                          (child class)
     - __init__(length, width) with validation.
     - area() returns length * width.

  8. Circle(Shape)                                             (child class)
     - __init__(radius) with validation.
     - area() returns math.pi * radius * radius.

Each object keeps its own data: changing one object never affects another.

Error-handling behaviour (chosen and documented):
  - All invalid input raises ValueError with a clear message instead of
    silently doing the wrong thing.
  - Employee: name must be a non-empty string; salary must be a non-negative
    number.
  - Manager: name must be a non-empty string; salary must be non-negative;
    department must be a non-empty string.
  - Rectangle: length and width must be positive numbers.
  - Circle: radius must be a positive number.
  - bool values are rejected wherever a real number is expected.
"""

import math

# ============================================================================
# Class 1: Employee (parent class)
# ============================================================================


class Employee:
    """An employee with a name and a salary."""

    def __init__(self, name, salary):
        """Initialize an Employee with a name and a salary.

        Args:
            name: The employee's name (must be a non-empty string).
            salary: The employee's salary (must be a non-negative number).

        Raises:
            ValueError: If name is empty or salary is not a non-negative
                number.
        """
        # Validate the name: it must be a string and not empty or
        # whitespace only.
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Employee name must be a non-empty string.")

        # Validate the salary: must be a real number (bool is rejected)
        # and must not be negative.
        if isinstance(salary, bool) or not isinstance(salary, (int, float)):
            raise ValueError("Salary must be a number.")
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        # Each object stores its own name and salary (instance attributes).
        self.name = name
        self.salary = salary

    def display_details(self):
        """Display the employee's name and salary."""
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")


# ============================================================================
# Class 2: Manager (child class of Employee)
# ============================================================================


class Manager(Employee):
    """A manager is an employee who also belongs to a department.

    Inherits name and salary from Employee and adds a department.
    """

    def __init__(self, name, salary, department):
        """Initialize a Manager with a name, salary, and department.

        Args:
            name: The manager's name (must be a non-empty string).
            salary: The manager's salary (must be a non-negative number).
            department: The department name (must be a non-empty string).

        Raises:
            ValueError: If name or department is empty, or salary is invalid.
        """
        # Validate the Manager-specific field here. name and salary are
        # validated by Employee.__init__ through super().
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department must be a non-empty string.")

        # super() calls the parent class (Employee) __init__, so the inherited
        # name and salary are initialized exactly as for a plain Employee.
        super().__init__(name, salary)

        # Each Manager object stores its own department.
        self.department = department

    def display_details(self):
        """Display the manager's name, salary, and department.

        Overrides Employee.display_details() to also show the department.
        """
        # Reuse the parent's display for name and salary, then add the
        # department.
        super().display_details()
        print(f"Department: {self.department}")


# ============================================================================
# Class 3, 4, 5: Animal, Dog, Cat (method overriding)
# ============================================================================


class Animal:
    """An animal that can make a sound."""

    def make_sound(self):
        """Return the sound this animal makes.

        Returns:
            A generic placeholder sound.
        """
        return "Some sound"


class Dog(Animal):
    """A dog that overrides Animal.make_sound()."""

    def make_sound(self):
        """Return the sound a dog makes.

        Returns:
            "Woof!"
        """
        return "Woof!"


class Cat(Animal):
    """A cat that overrides Animal.make_sound()."""

    def make_sound(self):
        """Return the sound a cat makes.

        Returns:
            "Meow!"
        """
        return "Meow!"


# ============================================================================
# Class 6, 7, 8: Shape, Rectangle, Circle (area)
# ============================================================================


class Shape:
    """A shape with an area."""

    def area(self):
        """Return the area of the shape.

        Returns:
            0 by default; subclasses override this with a real formula.
        """
        return 0


class Rectangle(Shape):
    """A rectangle with a length and a width."""

    def __init__(self, length, width):
        """Initialize a Rectangle with a length and a width.

        Args:
            length: The rectangle's length (must be a positive number).
            width: The rectangle's width (must be a positive number).

        Raises:
            ValueError: If length or width is not a positive number.

        Error-handling behaviour:
            Both dimensions must be positive numbers. Zero or negative values
            raise ValueError because a rectangle with a non-positive side has
            no meaningful area. Non-numeric values (including booleans) also
            raise ValueError.
        """
        if isinstance(length, bool) or not isinstance(length, (int, float)):
            raise ValueError("Length must be a number.")
        if isinstance(width, bool) or not isinstance(width, (int, float)):
            raise ValueError("Width must be a number.")
        if length <= 0:
            raise ValueError("Length must be positive.")
        if width <= 0:
            raise ValueError("Width must be positive.")

        # Each object stores its own dimensions (instance attributes).
        self.length = length
        self.width = width

    def area(self):
        """Return the rectangle's area: length * width.

        Returns:
            The area as a number.
        """
        return self.length * self.width


class Circle(Shape):
    """A circle with a radius."""

    def __init__(self, radius):
        """Initialize a Circle with a radius.

        Args:
            radius: The circle's radius (must be a positive number).

        Raises:
            ValueError: If radius is not a positive number.

        Error-handling behaviour:
            The radius must be a positive number. Zero or negative values
            raise ValueError because a circle with a non-positive radius has
            no meaningful area. Non-numeric values (including booleans) also
            raise ValueError.
        """
        if isinstance(radius, bool) or not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        self.radius = radius

    def area(self):
        """Return the circle's area: math.pi * radius * radius.

        Returns:
            The area as a floating-point number.
        """
        return math.pi * self.radius * self.radius


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 16 - Python Fundamentals: Inheritance, Method Overriding and super()")
    print("=" * 60)
    print()

    # --- Employee and Manager (inheritance, super(), overriding) ----------
    print("--- Employee and Manager ---")
    employee = Employee("Ada", 50000)
    employee.display_details()
    print()

    manager = Manager("Ben", 75000, "Engineering")
    print(f"Is Manager an Employee? {isinstance(manager, Employee)}")  # True
    manager.display_details()
    print()

    # Object independence: each manager keeps its own data.
    manager2 = Manager("Cid", 90000, "HR")
    manager2.display_details()
    print(f"{manager.name}'s department is still {manager.department}.")
    print()

    # --- Animal, Dog, Cat (method overriding) ------------------------------
    print("--- Animal, Dog, Cat ---")
    animals = [Animal(), Dog(), Cat()]
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.make_sound()}")
    print()

    # --- Rectangle and Circle (area) ---------------------------------------
    print("--- Rectangle and Circle ---")
    rectangle = Rectangle(4, 5)
    print(f"Rectangle 4x5 area: {rectangle.area()}")  # 20
    circle = Circle(3)
    print(f"Circle radius 3 area: {circle.area():.2f}")  # ~28.27
    print()

    # Validation examples.
    for label, factory in [
        ("negative length", lambda: Rectangle(-1, 5)),
        ("zero width", lambda: Rectangle(4, 0)),
        ("negative radius", lambda: Circle(-2)),
    ]:
        try:
            factory()
        except ValueError as error:
            print(f"{label}: rejected - {error}")

    print()
    print("=" * 60)
    print("Demo complete. Each object keeps its own data.")
    print("=" * 60)


if __name__ == "__main__":
    main()