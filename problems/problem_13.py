#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class Book:
    def __init__(self, title, author, isbn):
        """
        Represents a book in the library catalog.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            isbn (str): ISBN number of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    # TODO: Implement this function
    def check_out(self):
        """
        Marks the book as checked out.
        """
        pass

    # TODO: Implement this function
    def check_in(self):
        """
        Marks the book as checked in and available.
        """
        pass

class Library:
    def __init__(self):
        """
        Represents a library catalog system.

        This class allows librarians to manage books, add books to the catalog,
        and handle check-outs and check-ins.
        """
        self.books = {}

    # TODO: Implement this function
    def add_book(self, book):
        """
        Adds a book to the library catalog.

        Args:
            book (Book): Book object to be added.
        """
        pass

    # TODO: Implement this function
    def find_available_books(self):
        """
        Retrieves a list of available books in the library.

        Returns:
            list: List of available Book objects.
        """
        pass