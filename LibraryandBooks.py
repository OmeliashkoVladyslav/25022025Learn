class Book:
    def __init__(self, author, title, id):
        self.author = author
        self.title = title
        self.id = id


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book_id):
        self.books = list(book for book in self.books if book.id != book_id)
