class Book:
    """Base class representing a book with title and author."""

    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book with file size."""

    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book with page count."""

    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
