"""
Tests for Day 16 - Inheritance, Method Overriding and super() in
01-python-fundamentals/day16-inheritance-and-method-overriding.py.

Covers:
  - Employee: initialization, display_details, invalid name/salary.
  - Manager: initialization, inheritance from Employee, super() usage,
    method overriding (department shown), invalid name/salary/department.
  - Dog and Cat: method overriding of Animal.make_sound().
  - Rectangle: area, invalid dimensions.
  - Circle: area (uses math.pi), invalid radius.
  - Object independence.

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import contextlib
import importlib.util
import io
import math
import os

# Load day16-inheritance-and-method-overriding.py by file path.
_module_path = os.path.join(
    os.path.dirname(__file__), "day16-inheritance-and-method-overriding.py"
)
_spec = importlib.util.spec_from_file_location(
    "day16_inheritance_and_method_overriding", _module_path
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Employee = _module.Employee
Manager = _module.Manager
Animal = _module.Animal
Dog = _module.Dog
Cat = _module.Cat
Shape = _module.Shape
Rectangle = _module.Rectangle
Circle = _module.Circle


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _capture_display_details(obj):
    """Return the printed output of obj.display_details()."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        obj.display_details()
    return buffer.getvalue()


# ---------------------------------------------------------------------------
# Employee tests
# ---------------------------------------------------------------------------

def test_employee_stores_name_and_salary():
    employee = Employee("Ada", 50000)
    assert employee.name == "Ada"
    assert employee.salary == 50000


def test_employee_display_details_prints_name_and_salary():
    employee = Employee("Ben", 60000)
    output = _capture_display_details(employee)
    assert "Ben" in output
    assert "60000" in output


def test_employee_invalid_name_raises_value_error():
    for invalid_name in ["", "   ", None, 123]:
        try:
            Employee(invalid_name, 50000)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Employee({invalid_name!r}, 50000) did not raise ValueError"
            )


def test_employee_invalid_salary_raises_value_error():
    for invalid_salary in [-1, -0.01, "50000", None, True]:
        try:
            Employee("Ada", invalid_salary)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Employee('Ada', {invalid_salary!r}) did not raise ValueError"
            )


def test_two_employees_are_independent():
    employee1 = Employee("Ada", 50000)
    employee2 = Employee("Ben", 60000)
    employee1.salary = 55000
    assert employee2.salary == 60000  # employee2 unaffected


# ---------------------------------------------------------------------------
# Manager tests
# ---------------------------------------------------------------------------

def test_manager_stores_name_salary_and_department():
    manager = Manager("Ben", 75000, "Engineering")
    assert manager.name == "Ben"
    assert manager.salary == 75000
    assert manager.department == "Engineering"


def test_manager_is_an_employee():
    manager = Manager("Ben", 75000, "Engineering")
    assert isinstance(manager, Employee)


def test_manager_uses_super_and_inherits_employee_init():
    # Manager must initialize name and salary via Employee.__init__ (super()).
    manager = Manager("Cid", 90000, "HR")
    assert manager.name == "Cid"
    assert manager.salary == 90000


def test_manager_display_details_overrides_employee_and_shows_department():
    manager = Manager("Ben", 75000, "Engineering")
    output = _capture_display_details(manager)
    assert "Ben" in output
    assert "75000" in output
    assert "Engineering" in output


def test_manager_invalid_name_raises_value_error():
    try:
        Manager("", 75000, "Engineering")
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Manager('', 75000, 'Engineering') did not raise ValueError"
        )


def test_manager_invalid_salary_raises_value_error():
    try:
        Manager("Ben", -100, "Engineering")
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Manager('Ben', -100, 'Engineering') did not raise ValueError"
        )


def test_manager_invalid_department_raises_value_error():
    for invalid_department in ["", "   ", None, 123]:
        try:
            Manager("Ben", 75000, invalid_department)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Manager('Ben', 75000, {invalid_department!r}) did not raise "
                "ValueError"
            )


def test_two_managers_are_independent():
    manager1 = Manager("Ben", 75000, "Engineering")
    manager2 = Manager("Cid", 90000, "HR")
    manager1.salary = 80000
    assert manager2.salary == 90000  # manager2 unaffected
    assert manager1.department == "Engineering"
    assert manager2.department == "HR"


# ---------------------------------------------------------------------------
# Animal, Dog, Cat tests (method overriding)
# ---------------------------------------------------------------------------

def test_animal_make_sound_returns_generic_sound():
    animal = Animal()
    assert animal.make_sound() == "Some sound"


def test_dog_make_sound_overrides_animal():
    dog = Dog()
    assert isinstance(dog, Animal)
    assert dog.make_sound() == "Woof!"


def test_cat_make_sound_overrides_animal():
    cat = Cat()
    assert isinstance(cat, Animal)
    assert cat.make_sound() == "Meow!"


def test_dog_and_cat_sounds_are_different():
    assert Dog().make_sound() != Cat().make_sound()


# ---------------------------------------------------------------------------
# Rectangle tests
# ---------------------------------------------------------------------------

def test_rectangle_stores_length_and_width():
    rectangle = Rectangle(4, 5)
    assert rectangle.length == 4
    assert rectangle.width == 5


def test_rectangle_area():
    assert Rectangle(4, 5).area() == 20
    assert Rectangle(3, 7).area() == 21
    assert Rectangle(1.5, 2.0).area() == 3.0


def test_rectangle_is_a_shape():
    assert isinstance(Rectangle(4, 5), Shape)


def test_rectangle_invalid_length_raises_value_error():
    for invalid_length in [-1, 0, "4", None, True]:
        try:
            Rectangle(invalid_length, 5)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Rectangle({invalid_length!r}, 5) did not raise ValueError"
            )


def test_rectangle_invalid_width_raises_value_error():
    for invalid_width in [-1, 0, "5", None, True]:
        try:
            Rectangle(4, invalid_width)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Rectangle(4, {invalid_width!r}) did not raise ValueError"
            )


# ---------------------------------------------------------------------------
# Circle tests
# ---------------------------------------------------------------------------

def test_circle_stores_radius():
    circle = Circle(3)
    assert circle.radius == 3


def test_circle_area_uses_math_pi():
    circle = Circle(3)
    expected = math.pi * 3 * 3
    assert circle.area() == expected


def test_circle_is_a_shape():
    assert isinstance(Circle(3), Shape)


def test_circle_invalid_radius_raises_value_error():
    for invalid_radius in [-1, 0, "3", None, True]:
        try:
            Circle(invalid_radius)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Circle({invalid_radius!r}) did not raise ValueError"
            )


if __name__ == "__main__":
    test_employee_stores_name_and_salary()
    test_employee_display_details_prints_name_and_salary()
    test_employee_invalid_name_raises_value_error()
    test_employee_invalid_salary_raises_value_error()
    test_two_employees_are_independent()

    test_manager_stores_name_salary_and_department()
    test_manager_is_an_employee()
    test_manager_uses_super_and_inherits_employee_init()
    test_manager_display_details_overrides_employee_and_shows_department()
    test_manager_invalid_name_raises_value_error()
    test_manager_invalid_salary_raises_value_error()
    test_manager_invalid_department_raises_value_error()
    test_two_managers_are_independent()

    test_animal_make_sound_returns_generic_sound()
    test_dog_make_sound_overrides_animal()
    test_cat_make_sound_overrides_animal()
    test_dog_and_cat_sounds_are_different()

    test_rectangle_stores_length_and_width()
    test_rectangle_area()
    test_rectangle_is_a_shape()
    test_rectangle_invalid_length_raises_value_error()
    test_rectangle_invalid_width_raises_value_error()

    test_circle_stores_radius()
    test_circle_area_uses_math_pi()
    test_circle_is_a_shape()
    test_circle_invalid_radius_raises_value_error()

    print("All test_day16_inheritance_and_method_overriding tests passed!")