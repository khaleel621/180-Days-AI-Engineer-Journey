"""
Day 23 - Python Fundamentals: OOP Composition.

Topic: Composition — building complex classes by combining objects of other classes.

================================================================================
1. WHAT IS COMPOSITION?
================================================================================
Composition is a way to build a complex class from simpler classes. In
composition, one class (the "whole") HAS-AN object of another class (the "part")
stored as one of its attributes.

Real-life analogy:
    - A car HAS-AN engine.
    - A library HAS books.
    - A student HAS an address.
    - A room HAS a lamp and a fan.

In code, the "whole" class creates an instance of the "part" class inside its
constructor (__init__) and keeps it as self.<attribute>. The whole class can then
call methods on the part object.

================================================================================
2. WHY DO WE USE COMPOSITION?
================================================================================
    - Code reuse: write the Engine class once, reuse it in Car, Truck, etc.
    - Small, focused classes: each class does ONE job (Engine starts/stops;
      Car drives).
    - Loose coupling: Car does not need to know how Engine works inside. It only
      needs to call engine.start().
    - Flexibility: you can swap the part object at runtime (for example, replace
      a petrol engine with an electric engine) without changing the Car class.

================================================================================
3. INHERITANCE VS COMPOSITION
================================================================================
    | Inheritance                            | Composition                        |
    |----------------------------------------|------------------------------------|
    | "is-a" relationship                    | "has-a" relationship               |
    | Example: Car IS-A Vehicle              | Example: Car HAS-AN Engine         |
    | One class derives from another         | One class contains an object of    |
    | (class Car(Vehicle):)                  | another class (self.engine = ...)  |
    | Tightly coupled: parent changes can    | Loosely coupled: parts change      |
    | affect children                        | independently                      |
    | Hard to change at runtime              | Easy to swap parts at runtime      |

Rule of thumb: prefer composition unless there is a clear "is-a" relationship.

================================================================================
4. HOW ONE CLASS CAN CONTAIN AN OBJECT OF ANOTHER CLASS
================================================================================
    - Define the "part" class first.
    - Inside the "whole" class __init__, create an instance of the part class
      and store it as self.<attribute>.
    - The whole class methods can call the part object's methods.

================================================================================
5. REAL-WORLD EXAMPLES IMPLEMENTED BELOW
================================================================================
    1. Car and Engine        - Car has an Engine.
    2. Library and Book      - Library has a list of Book objects.
    3. Student and Address   - Student has an Address object.
    4. Room, Lamp and Fan    - Room has Lamp and Fan objects.
"""

# ---------------------------------------------------------------------------
# Example 1: Car HAS-AN Engine
# ---------------------------------------------------------------------------
class Engine:
    """An engine that can be started and stopped.

    Attributes:
        is_running: True if the engine is currently running, False otherwise.
    """

    def __init__(self, fuel_type="Petrol"):
        """Initialize the engine.

        Args:
            fuel_type: Type of fuel the engine uses (e.g. "Petrol", "Diesel",
                       "Electric").
        """
        self.fuel_type = fuel_type
        self.is_running = False

    def start(self):
        """Start the engine."""
        self.is_running = True
        return f"{self.fuel_type} engine started."

    def stop(self):
        """Stop the engine."""
        self.is_running = False
        return f"{self.fuel_type} engine stopped."


class Car:
    """A car that HAS-AN Engine (composition).

    Attributes:
        brand: Car brand name.
        model: Car model name.
        engine: An Engine object owned by this car.
    """

    def __init__(self, brand, model, engine=None):
        """Initialize a car.

        Args:
            brand: Car brand (non-empty text).
            model: Car model (non-empty text).
            engine: Optional Engine object. If None, a default Petrol engine
                    is created for the car.

        Raises:
            ValueError: If brand or model is empty.
        """
        if brand == "":
            raise ValueError("brand must not be empty.")
        if model == "":
            raise ValueError("model must not be empty.")

        self.brand = brand
        self.model = model

        # ------------------------------------------------------------------
        # COMPOSITION: Car contains an Engine object as an attribute.
        # The engine is a separate object; it may be None (an engineless car).
        # ------------------------------------------------------------------
        self.engine = engine

    def start_car(self):
        """Start the car by starting its engine."""
        if self.engine is None:
            return f"{self.brand} {self.model} has no engine and cannot start."
        return self.engine.start()

    def stop_car(self):
        """Stop the car by stopping its engine."""
        if self.engine is None:
            return f"{self.brand} {self.model} has no engine to stop."
        return self.engine.stop()

    def car_info(self):
        """Return a short description of the car and its engine."""
        return (f"{self.brand} {self.model} with a "
                f"{self.engine.fuel_type} engine "
                f"({'running' if self.engine.is_running else 'off'})")
# ---------------------------------------------------------------------------
# Example 2: Library HAS books (a list of Book objects)
# ---------------------------------------------------------------------------
class Book:
    """A book with a title and an author."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Library:
    """A library that HAS a collection of Book objects (composition).

    Attributes:
        name: Library name.
        books: List of Book objects in the library.
    """

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """Add a Book object to the library."""
        self.books.append(book)

    def list_books(self):
        """Return a list of string descriptions of all books."""
        return [str(book) for book in self.books]


# ---------------------------------------------------------------------------
# Example 3: Student HAS an Address
# ---------------------------------------------------------------------------
class Address:
    """An address with street, city and postal code."""

    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def __str__(self):
        return f"{self.street}, {self.city} - {self.postal_code}"


class Student:
    """A student that HAS-AN Address (composition).

    Attributes:
        name: Student name.
        address: An Address object belonging to this student.
    """

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def student_info(self):
        return f"{self.name} lives at {self.address}"
# ---------------------------------------------------------------------------
# Example 4: Room HAS a Lamp and a Fan
# ---------------------------------------------------------------------------
class Lamp:
    """A lamp that can be turned on or off."""

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return "Lamp is ON."

    def turn_off(self):
        self.is_on = False
        return "Lamp is OFF."


class Fan:
    """A fan that can be turned on or off."""

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return "Fan is ON."

    def turn_off(self):
        self.is_on = False
        return "Fan is OFF."


class Room:
    """A room that HAS a Lamp and a Fan (composition with multiple parts).

    Attributes:
        name: Room name.
        lamp: A Lamp object in the room.
        fan: A Fan object in the room.
    """

    def __init__(self, name):
        self.name = name
        self.lamp = Lamp()    # Room creates and owns a Lamp object.
        self.fan = Fan()      # Room creates and owns a Fan object.

    def turn_all_on(self):
        """Turn on both the lamp and the fan."""
        return f"{self.name}: {self.lamp.turn_on()} {self.fan.turn_on()}"

    def turn_all_off(self):
        """Turn off both the lamp and the fan."""
        return f"{self.name}: {self.lamp.turn_off()} {self.fan.turn_off()}"

    def room_status(self):
        return (f"{self.name} - Lamp: {'ON' if self.lamp.is_on else 'OFF'}, "
                f"Fan: {'ON' if self.fan.is_on else 'OFF'}")


# ---------------------------------------------------------------------------
# PRACTICAL EXERCISES (try these yourself after reading the examples above)
# ---------------------------------------------------------------------------
#
# Exercise 1:
#   Create a class Wallet with an attribute balance and methods
#   add_money(amount) and spend_money(amount). Then create a class Person
#   that HAS-AN Address and a Wallet. Person should have a method
#   pay(amount) that calls wallet.spend_money(amount).
#
# Exercise 2:
#   Create a class Team that HAS a list of Player objects. Each Player has a
#   name and a score. Team should have methods add_player(player) and
#   total_score() that returns the sum of all players' scores.
#
# Exercise 3:
#   Look at day16-inheritance-and-method-overriding.py (Manager IS-A Employee).
#   Rewrite that relationship using composition: a Department HAS-A list of
#   Employee objects instead of Manager inheriting from Employee.
#
# Exercise 4:
#   What happens if a Car's engine is replaced with an Electric engine?
#   Try: car.engine = Engine("Electric") and then car.start_car().


def main():
    print("=" * 60)
    print("Day 23 - Python Fundamentals: OOP Composition")
    print("=" * 60)
    print()

    # ------------------------------------------------------------------
    # Example 1: Car HAS-AN Engine
    # ------------------------------------------------------------------
    print("--- Example 1: Car has an Engine ---")
    default_car = Car("Toyota", "Corolla", Engine("Petrol"))
    print(default_car.car_info())        # expected: petrol engine, off
    print(default_car.start_car())       # expected: Petrol engine started.
    print(default_car.car_info())        # expected: running
    print(default_car.stop_car())        # expected: Petrol engine stopped.
    print()

    # Swap the engine at runtime (composition flexibility).
    electric_car = Car("Tesla", "Model 3", Engine("Electric"))
    print(electric_car.car_info())       # expected: electric engine, off
    print(electric_car.start_car())      # expected: Electric engine started.
    print()

    # Edge case: car with no engine.
    engineless = Car("Buggy", "Kit", None)
    print(engineless.start_car())        # expected: has no engine and cannot start
    print()

    # ------------------------------------------------------------------
    # Example 2: Library HAS books
    # ------------------------------------------------------------------
    print("--- Example 2: Library has books ---")
    library = Library("City Central Library")
    library.add_book(Book("Python Basics", "Khalil"))
    library.add_book(Book("Data Structures 101", "Aisha"))
    print(f"Library: {library.name}")
    for book_desc in library.list_books():
        print("  -", book_desc)
    print(f"Total books: {len(library.books)}  (expected 2)")
    print()

    # Edge case: empty library.
    empty_library = Library("Empty Library")
    print(f"Empty library books: {empty_library.list_books()}  (expected [])")
    print()

    # ------------------------------------------------------------------
    # Example 3: Student HAS an Address
    # ------------------------------------------------------------------
    print("--- Example 3: Student has an Address ---")
    address = Address("123 Python Street", "Dhaka", "1200")
    student = Student("Khalil", address)
    print(student.student_info())
    print()

    # ------------------------------------------------------------------
    # Example 4: Room HAS a Lamp and a Fan
    # ------------------------------------------------------------------
    print("--- Example 4: Room has a Lamp and a Fan ---")
    bedroom = Room("Bedroom")
    print(bedroom.room_status())           # expected: both OFF
    print(bedroom.turn_all_on())           # expected: both ON
    print(bedroom.room_status())           # expected: both ON
    print(bedroom.turn_all_off())          # expected: both OFF
    print()

    print("=" * 60)
    print("All composition demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()