from problems.problem_5 import ContactBook

def test_add_contact():
    book = ContactBook()
    book.add_contact("Alice", "1234567890")
    book.add_contact("Bob", "9876543210")
    book.add_contact("Eve", "5555555555")

    assert book.get_contact("Alice") == "1234567890"
    assert book.get_contact("Bob") == "9876543210"
    assert book.get_contact("Eve") == "5555555555"

def test_get_contact():
    book = ContactBook()
    book.add_contact("Alice", "1234567890")
    book.add_contact("Bob", "9876543210")
    book.add_contact("Eve", "5555555555")

    assert book.get_contact("Alice") == "1234567890"
    assert book.get_contact("Bob") == "9876543210"
    assert book.get_contact("Eve") == "5555555555"
    assert book.get_contact("Unknown") is None

def test_get_all_contacts():
    book = ContactBook()
    book.add_contact("Alice", "1234567890")
    book.add_contact("Bob", "9876543210")
    book.add_contact("Eve", "5555555555")

    all_contacts = book.get_all_contacts()
    assert len(all_contacts) == 3
    assert ("Alice", "1234567890") in all_contacts
    assert ("Bob", "9876543210") in all_contacts
    assert ("Eve", "5555555555") in all_contacts