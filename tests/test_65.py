from problems.problem_65 import ContactManager

def test_add_contact():
    manager = ContactManager()
    manager.add_contact("Alice", "123-456-7890")
    assert manager.contacts == [("Alice", "123-456-7890")]



def test_get_contact():
    manager = ContactManager()
    manager.add_contact("Bob", "987-654-3210")
    assert manager.get_contact("Bob") == "987-654-3210"

