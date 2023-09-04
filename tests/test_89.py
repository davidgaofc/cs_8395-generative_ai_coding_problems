from problems.problem_89 import DataStorage

def test_store():
    storage = DataStorage()

    storage.store("name", "Alice")
    storage.store("age", 30)

    assert storage.retrieve("name") == "Alice"
    assert storage.retrieve("age") == 30
    assert storage.retrieve("country") is None
def test_retrieve():
    storage = DataStorage()

    storage.store("name", "Alice")
    storage.store("age", 30)

    assert storage.retrieve("name") == "Alice"
    assert storage.retrieve("age") == 30
    assert storage.retrieve("country") is None
