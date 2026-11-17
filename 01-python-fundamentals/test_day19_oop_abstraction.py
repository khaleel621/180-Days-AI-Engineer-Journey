"""
Tests for Day 19 - OOP Abstraction in
01-python-fundamentals/day19-oop-abstraction.py.

Covers:
  - Shape is an abstract class and cannot be instantiated directly.
  - Rectangle.area() returns length * width (10 * 5 = 50).
  - Circle.area() returns pi * radius * radius (radius 5 -> ~78.54).
  - Rectangle and Circle are instances of Shape.
  - Rectangle and Circle are not abstract (can be instantiated).

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day19-oop-abstraction.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day19-oop-abstraction.py")
_spec = importlib.util.spec_from_file_location("day19_oop_abstraction", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Shape = _module.Shape
Rectangle = _module.Rectangle
Circle = _module.Circle


def test_shape_cannot_be_instantiated_directly():
    """The abstract class Shape must not be instantiable."""
    try:
        Shape()
    except TypeError:
        pass
    else:
        raise AssertionError("Shape() did not raise TypeError")


def test_rectangle_area():
    """Rectangle(10, 5).area() should be 50."""
    rectangle = Rectangle(10, 5)
    assert rectangle.area() == 50


def test_circle_area():
    """Circle(5).area() should be approximately 78.54."""
    circle = Circle(5)
    assert abs(circle.area() - 78.54) < 0.01


def test_rectangle_is_instance_of_shape():
    """A Rectangle should be an instance of Shape."""
    rectangle = Rectangle(10, 5)
    assert isinstance(rectangle, Shape)


def test_circle_is_instance_of_shape():
    """A Circle should be an instance of Shape."""
    circle = Circle(5)
    assert isinstance(circle, Shape)


def test_rectangle_can_be_instantiated():
    """Rectangle is concrete and can be instantiated."""
    rectangle = Rectangle(3, 4)
    assert rectangle.length == 3
    assert rectangle.width == 4


def test_circle_can_be_instantiated():
    """Circle is concrete and can be instantiated."""
    circle = Circle(7)
    assert circle.radius == 7


if __name__ == "__main__":
    test_shape_cannot_be_instantiated_directly()
    test_rectangle_area()
    test_circle_area()
    test_rectangle_is_instance_of_shape()
    test_circle_is_instance_of_shape()
    test_rectangle_can_be_instantiated()
    test_circle_can_be_instantiated()
    print("All test_day19_oop_abstraction tests passed!")