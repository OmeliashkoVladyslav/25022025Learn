from FixturesBooksLibrary import Book1, Book2
from FixturesBooksLibrary import Library1


class TestLibraryBooks:
    def test_book_in_library(self, Book1, Library1):
        Library1.add_book(Book1)
        assert Book1 in Library1.books

    def test_create_book(self, Book1):
        assert Book1.author == "John Tolkien"
        assert Book1.title == "The_Lord_Of_The_Rings"
        assert Book1.id == 143

    def test_add_book(self, Book1, Library1):
        Library1.add_book(Book1)
        assert Book1 in Library1.books

    def test_delete_book(self, Book1, Library1):
        Library1.delete_book(Book1.id)
        assert Book1.id not in Library1.books

    def test_duplicate_books(self, Book1, Library1):
        Library1.add_book(Book1)
        Library1.add_book(Book1)
        assert sum(1 for book in Library1.books if Book1.id == book.id) == 2

    def test_add_multiple_books(self, Book1, Book2, Library1):
        Library1.add_book(Book1)
        Library1.add_book(Book2)
        assert Book1 in Library1.books
        assert Book2 in Library1.books
