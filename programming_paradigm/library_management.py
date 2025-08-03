class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """Mark the book as checked out if it's available. Return True if success."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """Return the book (make it available). Return True if it was checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # explicit initialization for tests

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title: str) -> bool:
        """Attempt to check out a book by title. Returns True if successful."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # not found

    def return_book(self, title: str) -> bool:
        """Attempt to return a book by title. Returns True if successful."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # not found

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No available books.")
            return
        for book in available:
            print(str(book))
