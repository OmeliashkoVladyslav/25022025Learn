import pytest
from LibraryandBooks import Book, Library


@pytest.fixture(scope="session")
def Book1() -> Book:
    The_Lord_Of_The_Rings = Book("John Tolkien", "The_Lord_Of_The_Rings", 143)
    return The_Lord_Of_The_Rings


@pytest.fixture(scope="session")
def Book2() -> Book:
    Don_Kihot = Book("Miguel de Cervantes", "Don Kihot", 834)
    return Don_Kihot


@pytest.fixture(scope="session")
def Book3() -> Book:
    Golden_Bug = Book("Golden Bug", "Don Kihot", 294)
    return Golden_Bug


@pytest.fixture(scope="session")
def Library1(Book1) -> Library:
    My_Library = Library("My home library")
    My_Library.add_book(Book1)
    return My_Library


@pytest.fixture(scope="session")
def Library2(Book3) -> Library:
    My_Friend_Library = Library("My friend library")
    My_Friend_Library.add_book(Book3)
    return My_Friend_Library
