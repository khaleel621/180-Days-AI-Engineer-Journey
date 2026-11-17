"""
Day 19 - Python Fundamentals: OOP Abstraction.

Topic: Abstraction — hiding implementation details and showing only essential
features using abstract base classes.

This file teaches beginner-friendly abstraction with a Shape example:

  1. Abstraction
     - Lets you define what a class should do without specifying how.
     - An abstract class cannot be instantiated directly.
     - Subclasses must implement all abstract methods.

  2. ABC and abstractmethod
     - Imported from Python's abc module.
     - ABC is the base class for abstract base classes.
     - @abstractmethod marks a method that subclasses must override.

  3. Abstract class Shape
     - Cannot be created directly (Shape() raises TypeError).
     - Declares the abstract method area() that every shape must implement.

  4. Concrete subclasses Rectangle and Circle
     - Rectangle(length, width) implements area() as length * width.
     - Circle(radius) implements area() as pi * radius * radius.

  5. Beginner-friendly examples
     - Rectangle: length 10, width 5 → area 50.
     - Circle: radius 5 → area approximately 78.54.
"""

# ============================================================================
# Imports
# ============================================================================

import math
from abc import ABC, abstractmethod

# ============================================================================
# Abstract base class: Shape
# ============================================================================


class Shape(ABC):
    """An abstract base class for geometric shapes.

    Shape cannot be instantiated directly. Every concrete shape subclass
    must implement the area() method.
    """

    @abstractmethod
    def area(self):
        """Return the area of the shape.

        Subclasses must override this method with their own formula.
        """
        pass


# ============================================================================
# Concrete class: Rectangle
# ============================================================================


class Rectangle(Shape):
    """A rectangle with a length and a width."""

    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle: length * width."""
        return self.length * self.width


# ============================================================================
# Concrete class: Circle
# ============================================================================


class Circle(Shape):
    """A circle with a radius."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle: pi * radius * radius."""
        return math.pi * self.radius * self.radius


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 19 - Python Fundamentals: OOP Abstraction")
    print("=" * 60)
    print()

    # --- Abstract class cannot be instantiated directly ---
    print("--- Abstract class Shape cannot be instantiated ---")
    try:
        Shape()
    except TypeError as error:
        print(f"Shape() -> TypeError: {error}")
    print()

    # --- Rectangle ---
    print("--- Rectangle ---")
    rectangle = Rectangle(10, 5)
    print(f"Rectangle(length=10, width=5)")
    print(f"area() = {rectangle.area()}  (expected 50)")
    assert rectangle.area() == 50, f"Expected 50, got {rectangle.area()}"
    print()

    # --- Circle ---
    print("--- Circle ---")
    circle = Circle(5)
    circle_area = circle.area()
    print(f"Circle(radius=5)")
    print(f"area() = {circle_area:.2f}  (expected approximately 78.54)")
    assert abs(circle_area - 78.54) < 0.01, f"Expected ~78.54, got {circle_area}"
    print()

    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()