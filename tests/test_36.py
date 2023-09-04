from problems.problem_36 import HashmapOperations

def test_insert():
    hashmap = HashmapOperations()
    hashmap.insert("name", "John")
    hashmap.insert("age", 30)
    assert hashmap.get("name") == "John"
    assert hashmap.get("age") == 30

def test_get():
    hashmap = HashmapOperations()
    hashmap.insert("name", "John")
    hashmap.insert("age", 30)
    assert hashmap.get("name") == "John"
    assert hashmap.get("age") == 30
    assert hashmap.get("city") == -1

def test_delete():
    hashmap = HashmapOperations()
    hashmap.insert("name", "John")
    hashmap.insert("age", 30)
    hashmap.delete("age")
    assert hashmap.get("age") == -1