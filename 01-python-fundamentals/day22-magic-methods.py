"""
Day 22 - Python Fundamentals: OOP Magic Methods (Dunder Methods).

Topic: Magic methods — special Python methods whose names start and end
with double underscores, for example __init__, __str__, __repr__,
__len__, __eq__ and __add__.

Why are they called "dunder" methods?
    - "Dunder" is short for "double underscore".
    - __init__ is pronounced "dunder init", __str__ is "dunder str", and so on.

What are magic methods?
    - They are built into Python and define how objects behave with
      Python's functions and operators.
    - You usually do NOT call them directly. Python calls them for you.
      For example:
        print(book)     -> Python calls book.__str__()
        len(book)       -> Python calls book.__len__()
        book1 == book2  -> Python calls book1.__eq__(book2)
        book1 + book2   -> Python calls book1.__add__(book2)

Magic methods taught in this file:
  1. __init__()   - initializer: sets up a new object's attributes.
  2. __str__()    - friendly, readable string shown by print() and str().
  3. __repr__()   - developer-friendly representation shown by repr().
  4. __len__()    - length returned by len().
  5. __eq__()     - equality comparison used by ==.
  6. __add__()    - addition used by + (explained below; NOT implemented
                    for Book, because "book1 + book2" has no clear meaning).

Practical program: a Book class with a title, an author and a number of pages.
"""

class Book:
    """A book with a title, an author and a number of pages.

    Attributes:
        title:  Book title (non-empty text).
        author: Book author (non-empty text).
        pages:  Number of pages (a whole number >= 0).
    """

    def __init__(self, title, author, pages):
        """Initialize a book with title, author and pages.

        Args:
            title:  Book title (non-empty text).
            author: Book author (non-empty text).
            pages:  Number of pages (a whole number >= 0).

        Raises:
            TypeError:  If title or author is not text, or pages is not
                        a whole number.
            ValueError: If title or author is empty, or pages is negative.
        """
        # ------------------------------------------------------------------
        # Validate title.
        # ------------------------------------------------------------------
        if not isinstance(title, str):
            raise TypeError("title must be a string.")
        if title == "":
            raise ValueError("title must not be empty.")

        # ------------------------------------------------------------------
        # Validate author.
        # ------------------------------------------------------------------
        if not isinstance(author, str):
            raise TypeError("author must be a string.")
        if author == "":
            raise ValueError("author must not be empty.")

        # ------------------------------------------------------------------
        # Validate pages.
        # In Python, bool is a subclass of int, so True/False are rejected
        # explicitly to avoid accepting them as page counts.
        # ------------------------------------------------------------------
        if isinstance(pages, bool) or not isinstance(pages, int):
            raise TypeError("pages must be a whole number (integer).")
        if pages < 0:
            raise ValueError("pages must not be negative.")

        # Instance variables: belong to this book object only.
        self.title = title
        self.author = author
        self.pages = pages

    # ----------------------------------------------------------------------
    # __str__: friendly description for end users.
    # Called by print(book) and str(book).
    # ----------------------------------------------------------------------
    def __str__(self):
        """Return a friendly description of the book."""
        return f"Book: '{self.title}' by {self.author} ({self.pages} pages)"

    # ----------------------------------------------------------------------
    # __repr__: developer-friendly representation.
    # Called by repr(book); useful while debugging.
    # ----------------------------------------------------------------------
    def __repr__(self):
        """Return a code-like representation of the book."""
        return (
            f"Book(title='{self.title}', author='{self.author}', "
            f"pages={self.pages})"
        )

    # ----------------------------------------------------------------------
    # __len__: number of pages.
    # Called by len(book).
    # ----------------------------------------------------------------------
    def __len__(self):
        """Return the number of pages in the book."""
        return self.pages

    # ----------------------------------------------------------------------
    # __eq__: equality comparison.
    # Called by book1 == book2.
    # Two books are equal when title, author and pages all match.
    # ----------------------------------------------------------------------
    def __eq__(self, other):
        """Check whether two books are equal."""
        if not isinstance(other, Book):
            # Comparing a Book with something else: not equal.
            return NotImplemented
        return (
            self.title == other.title
            and self.author == other.author
            and self.pages == other.pages
        )

    # ----------------------------------------------------------------------
    # __add__ is intentionally NOT implemented for Book.
    #
    # Why? "book1 + book2" has no single, clearly defined meaning:
    #   - Should it join the two titles?
    #   - Should it add the page counts?
    #   - Should it keep both authors?
    # Because there is no obvious answer, Python should not guess.
    #
    # If you need total pages, write a plain function instead:
    #   total_pages = book1.pages + book2.pages
    #
    # __add__ IS appropriate when "+" has an obvious meaning, for example
    # adding two money amounts, two vectors, or two durations. For Book,
    # it is left out on purpose.
    # ----------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Day 22 - Python Fundamentals: OOP Magic Methods (Dunder Methods)")
    print("=" * 60)
    print()

    # --- Create book objects ---------------------------------------------
    print("--- Create book objects ---")
    book1 = Book("Python Basics", "Khalil", 100)
    book2 = Book("Data Structures 101", "Aisha", 250)
    book3 = Book("Python Basics", "Khalil", 100)  # same as book1
    print(f"book1 = {book1}")
    print(f"book2 = {book2}")
    print(f"book3 = {book3}")
    print()

    # --- __str__: print() uses __str__ -----------------------------------
    print("--- __str__: friendly description (print / str) ---")
    print(book1)
    print(f"str(book2) = {str(book2)}")
    print()

    # --- __repr__: developer representation -------------------------------
    print("--- __repr__: developer-friendly representation (repr) ---")
    print(repr(book1))
    print()

    # --- __len__: len(book) returns pages ---------------------------------
    print("--- __len__: number of pages ---")
    print(f"len(book1) = {len(book1)}   (expected 100)")
    print(f"len(book2) = {len(book2)}   (expected 250)")
    print()

    # --- __eq__: book1 == book2 ------------------------------------------
    print("--- __eq__: equality comparison ---")
    print(f"book1 == book2: {book1 == book2}   (expected False; different books)")
    print(f"book1 == book3: {book1 == book3}   (expected True; same book)")
    print(f"book1 == 'Python Basics': {book1 == 'Python Basics'}   (expected False)")
    print()

    # --- Invalid input handling ------------------------------------------
    print("--- Invalid input handling ---")
    invalid_cases = [
        (123, "Author", 100, "title must be a string"),
        ("Title", 123, 100, "author must be a string"),
        ("", "Author", 100, "title must not be empty"),
        ("Title", "", 100, "author must not be empty"),
        ("Title", "Author", -5, "pages must not be negative"),
        ("Title", "Author", 10.5, "pages must be a whole number"),
    ]
    for title, author, pages, description in invalid_cases:
        try:
            Book(title, author, pages)
            print(f"  Book({title!r}, {author!r}, {pages!r}): NO ERROR (unexpected!)")
        except (TypeError, ValueError) as error:
            print(f"  Book({title!r}, {author!r}, {pages!r}): {type(error).__name__} -> {error}")
    print()

    print("=" * 60)
    print("All demo cases verified.")
    print("=" * 60)


if __name__ == "__main__":
    main()
