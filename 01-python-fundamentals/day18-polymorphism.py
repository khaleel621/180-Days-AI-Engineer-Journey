"""
Day 18 - Python Fundamentals: OOP - Polymorphism, Method Overloading and Method Overriding.

Topic: Polymorphism - same method name, different behavior.

This file teaches beginner-friendly polymorphism with practical examples:

  1. What is polymorphism?
     - Poly = many, morph = form.
     - One interface (method name) with many different implementations.
     - The same method call behaves differently depending on the object.

  2. Same method name with different behavior.
     - Different classes define the same method (e.g. make_sound()) but each
       class implements it in its own way.
     - Calling make_sound() on a Dog, a Cat or a Cow gives different results.

  3. Method overriding.
     - A child class redefines a method that already exists in its parent class.
     - The child's version replaces the parent's version for that child's objects.

  4. Method overloading in Python.
     - Python does NOT support traditional method overloading (multiple methods
       with the same name but different parameter lists).
     - Instead, use default arguments, *args / **kwargs, or isinstance() checks
       to handle different call patterns with a single method.

  5. Duck typing.
     - "If it walks like a duck and quacks like a duck, it's a duck."
     - We don't care about the object's type; we only care that it has the
       method we want to call.
     - Any object with a .speak() method can be passed to make_it_speak().

  6. Practical examples.
     - Animal hierarchy: make_sound() polymorphic via overriding.
     - Calculator: add() handles 0, 1, 2 or 3 arguments (overloading style).
     - Duck typing: Dog, Cat and Robot all have .speak() but no common parent.
"""


# ============================================================================
# Example 1: Polymorphism via method overriding (Animal hierarchy)
# ============================================================================


class Animal:
    """Base class for all animals.

    The make_sound() method defines the interface: every animal can make a
    sound, but the sound itself depends on the specific animal.
    """

    def make_sound(self):
        """Return a generic sound for an animal.

        Returns:
            A string describing a generic animal sound.
        """
        return "Some generic animal sound"


class Dog(Animal):
    """A dog that overrides make_sound()."""

    def make_sound(self):
        """Return the sound a dog makes.

        Returns:
            The string "Woof!".
        """
        return "Woof!"


class Cat(Animal):
    """A cat that overrides make_sound()."""

    def make_sound(self):
        """Return the sound a cat makes.

        Returns:
            The string "Meow!".
        """
        return "Meow!"


class Cow(Animal):
    """A cow that overrides make_sound()."""

    def make_sound(self):
        """Return the sound a cow makes.

        Returns:
            The string "Moo!".
        """
        return "Moo!"


def animal_sound(animal):
    """Demonstrate polymorphism: call make_sound() on any Animal.

    Because Dog, Cat and Cow all inherit from Animal and override make_sound(),
    this function works with any of them. The exact behavior depends on the
    object passed in - that is polymorphism.

    Args:
        animal: An object that has a make_sound() method.

    Returns:
        The sound string returned by animal.make_sound().
    """
    return animal.make_sound()


# ============================================================================
# Example 2: Method overloading in Python (Calculator)
# ============================================================================


class Calculator:
    """A calculator that demonstrates method overloading in Python.

    Python does not allow multiple methods with the same name and different
    parameter lists. Instead, we use a single method with *args (variable
    positional arguments) to handle calls with different numbers of arguments.
    """

    def add(self, *args):
        """Add together any number of numeric arguments.

        This single method replaces what in other languages would be several
        overloaded methods:
          - add()            -> 0
          - add(a)           -> a
          - add(a, b)        -> a + b
          - add(a, b, c)     -> a + b + c

        Args:
            *args: Zero or more numbers to add.

        Returns:
            The sum of all arguments. Returns 0 when called with no arguments.

        Raises:
            TypeError: If any argument is not a number (int or float).
        """
        total = 0
        for value in args:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("All arguments must be numbers (int or float).")
            total += value
        return total


# ============================================================================
# Example 3: Duck typing
# ============================================================================


class DogDuck:
    """A dog that can speak - no Animal parent class."""

    def speak(self):
        return "Woof! (duck typing)"


class CatDuck:
    """A cat that can speak - no Animal parent class."""

    def speak(self):
        return "Meow! (duck typing)"


class RobotDuck:
    """A robot that can speak - no Animal parent class, but still has speak()."""

    def speak(self):
        return "Beep boop! (duck typing)"


def make_it_speak(obj):
    """Demonstrate duck typing: call .speak() on any object that has it.

    We do not check obj's type or whether it inherits from a specific class.
    We only require that the object has a speak() method. If it does, we call
    it; if it does not, we raise AttributeError.

    Args:
        obj: Any object that has a speak() method.

    Returns:
        The string returned by obj.speak().
    """
    return obj.speak()


# ============================================================================
# DEMO
# ============================================================================


def main():
    print("=" * 60)
    print("Day 18 - Python Fundamentals: Polymorphism, Overloading, Overriding")
    print("=" * 60)
    print()

    # --- Polymorphism: same method name, different behavior ----
    print("--- Polymorphism via method overriding ---")
    animals = [Dog(), Cat(), Cow()]
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal_sound(animal)}")
    print()

    # The same function, animal_sound(), produces different output depending
    # on the object it receives. That is polymorphism.
    print("Same function, animal_sound(), different results per object.")
    print()

    # --- Method overloading (Python style) ----
    print("--- Method overloading (Calculator.add) ---")
    calc = Calculator()
    print(f"calc.add()              = {calc.add()}")            # 0
    print(f"calc.add(5)           = {calc.add(5)}")            # 5
    print(f"calc.add(2, 3)        = {calc.add(2, 3)}")        # 5
    print(f"calc.add(1, 2, 3)     = {calc.add(1, 2, 3)}")    # 6
    print()

    # Invalid argument type.
    try:
        calc.add("a", "b")
    except TypeError as error:
        print(f"calc.add('a', 'b') rejected: {error}")
    print()

    # --- Duck typing ----
    print("--- Duck typing ---")
    speakers = [DogDuck(), CatDuck(), RobotDuck()]
    for speaker in speakers:
        print(f"{speaker.__class__.__name__}: {make_it_speak(speaker)}")
    print()

    # All three objects have .speak() even though they share no parent class.
    print("make_it_speak() works with any object that has a .speak() method.")
    print()

    print("=" * 60)
    print("Demo complete. Polymorphism lets one interface serve many forms.")
    print("=" * 60)


if __name__ == "__main__":
    main()
