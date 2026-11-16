"""
Tests for Day 18 - Polymorphism, Method Overloading and Method Overriding in
01-python-fundamentals/day18-polymorphism.py.

Covers:
  - Animal.make_sound() returns a generic sound.
  - Dog.make_sound(), Cat.make_sound(), Cow.make_sound() override the parent.
  - animal_sound() works polymorphically with Dog, Cat and Cow.
  - Calculator.add() handles 0, 1, 2 and 3 arguments (Python-style overloading).
  - Calculator.add() rejects non-numeric arguments.
  - Duck typing: make_it_speak() works with any object that has .speak().
  - Multiple objects tested for each polymorphic function.

The implementation is loaded by file path so the tests work regardless of the
current working directory.
"""

import importlib.util
import os

# Load day18-polymorphism.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day18-polymorphism.py")
_spec = importlib.util.spec_from_file_location("day18_polymorphism", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Animal = _module.Animal
Dog = _module.Dog
Cat = _module.Cat
Cow = _module.Cow
animal_sound = _module.animal_sound
Calculator = _module.Calculator
DogDuck = _module.DogDuck
CatDuck = _module.CatDuck
RobotDuck = _module.RobotDuck
make_it_speak = _module.make_it_speak


# ---------------------------------------------------------------------------
# Polymorphism via method overriding
# ---------------------------------------------------------------------------

def test_animal_make_sound_returns_generic_sound():
    """Animal.make_sound() returns a generic string."""
    animal = Animal()
    assert animal.make_sound() == "Some generic animal sound"


def test_dog_make_sound_overrides_animal():
    """Dog.make_sound() overrides Animal.make_sound()."""
    dog = Dog()
    assert dog.make_sound() == "Woof!"


def test_cat_make_sound_overrides_animal():
    """Cat.make_sound() overrides Animal.make_sound()."""
    cat = Cat()
    assert cat.make_sound() == "Meow!"


def test_cow_make_sound_overrides_animal():
    """Cow.make_sound() overrides Animal.make_sound()."""
    cow = Cow()
    assert cow.make_sound() == "Moo!"


def test_animal_sound_works_polymorphically():
    """animal_sound() produces different output depending on the object."""
    dog = Dog()
    cat = Cat()
    cow = Cow()
    assert animal_sound(dog) == "Woof!"
    assert animal_sound(cat) == "Meow!"
    assert animal_sound(cow) == "Moo!"


def test_animal_sound_with_multiple_objects():
    """animal_sound() is tested with multiple objects of each type."""
    dogs = [Dog(), Dog(), Dog()]
    cats = [Cat(), Cat()]
    cows = [Cow(), Cow(), Cow(), Cow()]
    for dog in dogs:
        assert animal_sound(dog) == "Woof!"
    for cat in cats:
        assert animal_sound(cat) == "Meow!"
    for cow in cows:
        assert animal_sound(cow) == "Moo!"


# ---------------------------------------------------------------------------
# Method overloading (Python style)
# ---------------------------------------------------------------------------

def test_calculator_add_no_arguments():
    """calc.add() with no arguments returns 0."""
    calc = Calculator()
    assert calc.add() == 0


def test_calculator_add_one_argument():
    """calc.add(a) returns a."""
    calc = Calculator()
    assert calc.add(7) == 7


def test_calculator_add_two_arguments():
    """calc.add(a, b) returns a + b."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(10, 20) == 30
    assert calc.add(-1, 1) == 0


def test_calculator_add_three_arguments():
    """calc.add(a, b, c) returns a + b + c."""
    calc = Calculator()
    assert calc.add(1, 2, 3) == 6
    assert calc.add(0, 0, 0) == 0


def test_calculator_add_float_arguments():
    """calc.add() works with floats."""
    calc = Calculator()
    assert calc.add(1.5, 2.5) == 4.0


def test_calculator_add_rejects_non_numeric():
    """calc.add() raises TypeError for non-numeric arguments."""
    calc = Calculator()
    for bad in ["a", None, [1, 2], True]:
        try:
            calc.add(bad)
        except TypeError:
            pass
        else:
            raise AssertionError(
                f"calc.add({bad!r}) did not raise TypeError"
            )


# ---------------------------------------------------------------------------
# Duck typing
# ---------------------------------------------------------------------------

def test_dog_duck_speak():
    """DogDuck.speak() returns a string."""
    assert DogDuck().speak() == "Woof! (duck typing)"


def test_cat_duck_speak():
    """CatDuck.speak() returns a string."""
    assert CatDuck().speak() == "Meow! (duck typing)"


def test_robot_duck_speak():
    """RobotDuck.speak() returns a string."""
    assert RobotDuck().speak() == "Beep boop! (duck typing)"


def test_make_it_speak_works_with_any_speaking_object():
    """make_it_speak() works with any object that has .speak()."""
    speakers = [DogDuck(), CatDuck(), RobotDuck()]
    results = [make_it_speak(s) for s in speakers]
    assert "Woof! (duck typing)" in results
    assert "Meow! (duck typing)" in results
    assert "Beep boop! (duck typing)" in results


def test_make_it_speak_with_multiple_objects():
    """make_it_speak() is tested with multiple objects of each type."""
    dogs = [DogDuck(), DogDuck()]
    cats = [CatDuck(), CatDuck(), CatDuck()]
    robots = [RobotDuck()]
    for dog in dogs:
        assert make_it_speak(dog) == "Woof! (duck typing)"
    for cat in cats:
        assert make_it_speak(cat) == "Meow! (duck typing)"
    for robot in robots:
        assert make_it_speak(robot) == "Beep boop! (duck typing)"


if __name__ == "__main__":
    test_animal_make_sound_returns_generic_sound()
    test_dog_make_sound_overrides_animal()
    test_cat_make_sound_overrides_animal()
    test_cow_make_sound_overrides_animal()
    test_animal_sound_works_polymorphically()
    test_animal_sound_with_multiple_objects()

    test_calculator_add_no_arguments()
    test_calculator_add_one_argument()
    test_calculator_add_two_arguments()
    test_calculator_add_three_arguments()
    test_calculator_add_float_arguments()
    test_calculator_add_rejects_non_numeric()

    test_dog_duck_speak()
    test_cat_duck_speak()
    test_robot_duck_speak()
    test_make_it_speak_works_with_any_speaking_object()
    test_make_it_speak_with_multiple_objects()

    print("All test_day18_polymorphism tests passed!")