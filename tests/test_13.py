from problems.problem_13 import Book, Library

def test_check_out():
    book = Book("The Hobbit", "J.R.R. Tolkien", "9780547928227")
    book.check_out()
    assert not book.available

def test_check_in():
    book = Book("The Hobbit", "J.R.R. Tolkien", "9780547928227")
    book.check_out()
    book.check_in()
    assert book.available

def test_add_book():
    library = Library()
    book = Book("Harry Potter", "J.K. Rowling", "9780439554930")
    library.add_book(book)
    assert book.isbn in library.books
    assert library.books[book.isbn] == book

def test_find_available_books():
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book1.check_out()

    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

    library.add_book(book1)
    library.add_book(book2)

    available_books = library.find_available_books()
    assert len(available_books) == 1
    assert available_books[0].title == "To Kill a Mockingbird"