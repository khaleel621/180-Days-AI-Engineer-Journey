"""
Tests for Day 22 - OOP Magic Methods in
01-python-fundamentals/day22-magic-methods.py.

Covers:
  - Book object creation with title, author and pages.
  - __str__(): friendly string shown by print() and str().
  - __repr__(): developer representation shown by repr().
  - __len__(): number of pages returned by len().
  - __eq__(): equality of two books with ==.
  - Different books are not equal.
  - A book is not equal to a non-Book value.
  - Invalid input handling (wrong types, empty text, negative pages).

The implementation is loaded by file path so the tests work regardless of
the current working directory.
"""

import importlib.util
import os

# Load day22-magic-methods.py by file path.
_module_path = os.path.join(os.path.dirname(__file__), "day22-magic-methods.py")
_spec = importlib.util.spec_from_file_location("day22_magic_methods", _module_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

Book = _module.Book


def _make_book(title="Python Basics", author="Khalil", pages=100):
    return Book(title, author, pages)


# -----------------------------------------------------------
# Object creation
# -----------------------------------------------------------

def test_book_creation_stores_title_author_and_pages():
    """A Book object stores its own title, author and pages."""
    book = _make_book("Python Basics", "Khalil", 100)
    assert book.title == "Python Basics"
    assert book.author == "Khalil"
    assert book.pages == 100


def test_zero_pages_is_valid():
    """A book with 0 pages is valid (no pages yet)."""
    book = _make_book("Empty Book", "Author", 0)
    assert book.pages == 0


# -----------------------------------------------------------
# String representation
# -----------------------------------------------------------

def test_str_shows_book_information():
    """__str__() gives a friendly description with title, author and pages."""
    book = _make_book("Python Basics", "Khalil", 100)
    text = str(book)
    assert "Python Basics" in text
    assert "Khalil" in text
    assert "100" in text


def test_repr_is_developer_friendly():
    """__repr__() gives a code-like representation of the book."""
    book = _make_book("Python Basics", "Khalil", 100)
    text = repr(book)
    assert "Book(" in text
    assert "Python Basics" in text
    assert "Khalil" in text
    assert "pages=100" in text


# -----------------------------------------------------------
# Equality
# -----------------------------------------------------------

def test_equal_books_are_equal():
    """__eq__() returns True for two books with the same title, author
    and number of pages."""
    book1 = _make_book("Python Basics", "Khalil", 100)
    book2 = Book("Python Basics", "Khalil", 100)
    assert book1 == book2


def test_different_books_are_not_equal():
    """__eq__() returns False when title, author or pages differ."""
    book1 = _make_book("Python Basics", "Khalil", 100)
    different_pages = Book("Python Basics", "Khalil", 200)
    different_title = Book("Advanced Python", "Khalil", 100)
    different_author = Book("Python Basics", "Someone Else", 100)
    assert book1 != different_pages
    assert book1 != different_title
    assert book1 != different_author


def test_book_not_equal_to_other_types():
    """A Book is not equal to a string, number or None."""
    book = _make_book("Python Basics", "Khalil", 100)
    assert book != "Python Basics"
    assert book != 100
    assert book is not None


# -----------------------------------------------------------
# Invalid input handling
# -----------------------------------------------------------

def test_invalid_title_type_raises_type_error():
    """title must be a string."""
    try:
        Book(123, "Author", 100)
    except TypeError:
        pass
    else:
        raise AssertionError("Book(123, ...) did not raise TypeError")


def test_invalid_author_type_raises_type_error():
    """author must be a string."""
    try:
        Book("Title", 123, 100)
    except TypeError:
        pass
    else:
        raise AssertionError('Book(..., 123, ...) did not raise TypeError')


def test_empty_title_raises_value_error():
    """title must not be empty."""
    try:
        Book("", "Author", 100)
    except ValueError:
        pass
    else:
        raise AssertionError('Book("", ...) did not raise ValueError')


def test_empty_author_raises_value_error():
    """author must not be empty."""
    try:
        Book("Title", "", 100)
    except ValueError:
        pass
    else:
        raise AssertionError('Book(..., "", ...) did not raise ValueError')


def test_negative_pages_raises_value_error():
    """pages must not be negative."""
    try:
        Book("Title", "Author", -5)
    except ValueError:
        pass
    else:
        raise AssertionError("Book(..., -5) did not raise ValueError")


def test_pages_float_raises_type_error():
    """pages must be a whole number, not a float."""
    try:
        Book("Title", "Author", 10.5)
    except TypeError:
        pass
    else:
        raise AssertionError("Book(..., 10.5) did not raise TypeError")


# -----------------------------------------------------------
# Length
# -----------------------------------------------------------

def test_len_returns_number_of_pages():
    """__len__() returns the number of pages."""
    book = _make_book("Python Basics", "Khalil", 100)
    assert len(book) == 100

    short = _make_book("Short Story", "Author", 1)
    assert len(short) == 1

if __name__ == "__main__":
    test_book_creation_stores_title_author_and_pages()
    test_zero_pages_is_valid()
    test_str_shows_book_information()
    test_repr_is_developer_friendly()
    test_len_returns_number_of_pages()
    test_equal_books_are_equal()
    test_different_books_are_not_equal()
    test_book_not_equal_to_other_types()
    test_invalid_title_type_raises_type_error()
    test_invalid_author_type_raises_type_error()
    test_empty_title_raises_value_error()
    test_empty_author_raises_value_error()
    test_negative_pages_raises_value_error()
    test_pages_float_raises_type_error()
    print("All test_day22_magic_methods tests passed!")
