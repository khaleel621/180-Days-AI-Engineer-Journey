"""
Tests for Day 23 - OOP Composition in
01-python-fundamentals/day23-composition.py.

Covers:
    - Composition: one class (the whole) holds an object of another class
      (the part) as an attribute.
    - Car HAS-AN Engine: start/stop delegate to the engine.
    - Library HAS a list of Book objects.
    - Student HAS-AN Address object.
    - Room HAS a Lamp and a Fan.
    - Edge cases: car with no engine, empty library, invalid inputs.

The implementation is loaded by file path so the tests work regardless of
the current working directory.
"""

import importlib.util
import os

# Load day23-composition.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day23-composition.py")
_spec = importlib.util.spec_from_file_location("day23_composition", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Engine = _module.Engine
Car = _module.Car
Book = _module.Book
Library = _module.Library
Address = _module.Address
Student = _module.Student
Lamp = _module.Lamp
Fan = _module.Fan
Room = _module.Room


def _make_engine(fuel_type="Petrol"):
    return Engine(fuel_type)


def _make_car(brand="Toyota", model="Corolla", engine=None):
    return Car(brand, model, engine)


# -----------------------------------------------------------
# Composition relationship: the "whole" holds a "part" object
# -----------------------------------------------------------

def test_car_has_an_engine_object():
    """A Car object contains an Engine object as its engine attribute."""
    car = _make_car(engine=Engine("Petrol"))
    assert isinstance(car.engine, Engine)
    assert car.engine.fuel_type == "Petrol"


def test_car_start_delegates_to_engine():
    """Starting the car starts its composed Engine object."""
    car = _make_car(engine=Engine("Petrol"))
    result = car.start_car()
    assert result == "Petrol engine started."
    assert car.engine.is_running is True


def test_car_stop_delegates_to_engine():
    """Stopping the car stops its composed Engine object."""
    car = _make_car(engine=Engine("Petrol"))
    car.start_car()
    result = car.stop_car()
    assert result == "Petrol engine stopped."
    assert car.engine.is_running is False


def test_engine_is_none_when_not_provided():
    """If no engine is supplied, the car has no engine (engine is None)."""
    car = _make_car(engine=None)
    assert car.engine is None


def test_custom_engine_is_used():
    """A supplied Engine object is used by the Car."""
    electric = Engine("Electric")
    car = Car("Tesla", "Model 3", electric)
    assert car.engine is electric
    assert car.engine.fuel_type == "Electric"
    assert car.start_car() == "Electric engine started."


def test_engine_can_be_swapped_at_runtime():
    """Composition lets us replace the part object without changing Car."""
    car = _make_car(engine=Engine("Petrol"))
    assert car.engine.fuel_type == "Petrol"
    car.engine = Engine("Diesel")
    assert car.engine.fuel_type == "Diesel"
    assert car.start_car() == "Diesel engine started."
# -----------------------------------------------------------
# Edge cases
# -----------------------------------------------------------

def test_car_with_no_engine_cannot_start():
    """A Car built with engine=None reports it cannot start."""
    car = Car("Buggy", "Kit", None)
    assert car.engine is None
    result = car.start_car()
    assert "no engine" in result
    assert "cannot start" in result


def test_car_with_no_engine_has_nothing_to_stop():
    car = Car("Buggy", "Kit", None)
    result = car.stop_car()
    assert "no engine" in result


def test_empty_brand_raises_value_error():
    try:
        Car("", "Corolla")
    except ValueError:
        pass
    else:
        raise AssertionError('Car("", "Corolla") did not raise ValueError')


def test_empty_model_raises_value_error():
    try:
        Car("Toyota", "")
    except ValueError:
        pass
    else:
        raise AssertionError('Car("Toyota", "") did not raise ValueError')


# -----------------------------------------------------------
# Library HAS books (list of Book objects)
# -----------------------------------------------------------

def test_library_holds_book_objects():
    library = Library("City Central Library")
    book1 = Book("Python Basics", "Khalil")
    book2 = Book("Data Structures 101", "Aisha")
    library.add_book(book1)
    library.add_book(book2)

    assert len(library.books) == 2
    assert library.books[0] is book1
    assert library.books[1] is book2


def test_library_list_books_returns_descriptions():
    library = Library("City Library")
    library.add_book(Book("Python Basics", "Khalil"))
    descriptions = library.list_books()
    assert len(descriptions) == 1
    assert "Python Basics" in descriptions[0]
    assert "Khalil" in descriptions[0]


def test_empty_library_has_no_books():
    library = Library("Empty Library")
    assert library.books == []
    assert library.list_books() == []


# -----------------------------------------------------------
# Student HAS an Address
# -----------------------------------------------------------

def test_student_has_an_address_object():
    address = Address("123 Python Street", "Dhaka", "1200")
    student = Student("Khalil", address)
    assert student.address is address
    assert student.address.city == "Dhaka"
    assert "123 Python Street" in student.student_info()


# -----------------------------------------------------------
# Room HAS a Lamp and a Fan
# -----------------------------------------------------------

def test_room_has_lamp_and_fan():
    room = Room("Bedroom")
    assert isinstance(room.lamp, Lamp)
    assert isinstance(room.fan, Fan)
    assert room.lamp.is_on is False
    assert room.fan.is_on is False


def test_room_turn_all_on_and_off():
    room = Room("Bedroom")
    room.turn_all_on()
    assert room.lamp.is_on is True
    assert room.fan.is_on is True
    assert "ON" in room.room_status()

    room.turn_all_off()
    assert room.lamp.is_on is False
    assert room.fan.is_on is False
    assert "OFF" in room.room_status()


if __name__ == "__main__":
    test_car_has_an_engine_object()
    test_car_start_delegates_to_engine()
    test_car_stop_delegates_to_engine()
    test_engine_is_none_when_not_provided()
    test_custom_engine_is_used()
    test_engine_can_be_swapped_at_runtime()
    test_car_with_no_engine_cannot_start()
    test_car_with_no_engine_has_nothing_to_stop()
    test_empty_brand_raises_value_error()
    test_empty_model_raises_value_error()
    test_library_holds_book_objects()
    test_library_list_books_returns_descriptions()
    test_empty_library_has_no_books()
    test_student_has_an_address_object()
    test_room_has_lamp_and_fan()
    test_room_turn_all_on_and_off()
    print("All test_day23_composition tests passed!")