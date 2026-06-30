"""
EXAMPLE TEST FILE — this is here as a working pattern to copy.
In Week 7 (Unit Testing) you'll add more tests like the one below.

To run these tests: open a terminal in the project root and run `pytest`.
"""

from library_app.book import Book


def test_check_out_reduces_available_copies_by_one():
    # Arrange
    book = Book("Sample Title", "Sample Author", "0000000000000", 3)

    # Act
    book.check_out()

    # Assert
    assert book.available_copies == 2
