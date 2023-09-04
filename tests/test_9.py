from problems.problem_9 import SocialNetwork


def test_add_friend():
    network = SocialNetwork()

    network.add_friend("Alice", "Bob")
    assert "Bob" in network.find_friends("Alice")
    assert "Alice" in network.find_friends("Bob")

    network.add_friend("Alice", "Charlie")
    assert "Charlie" in network.find_friends("Alice")
    assert "Alice" in network.find_friends("Charlie")

def test_find_mutual_friends():
    network = SocialNetwork()

    network.add_friend("Alice", "Bob")
    network.add_friend("Alice", "Charlie")
    network.add_friend("Charlie", "David")
    network.add_friend("Charlie", "Eve")

    assert network.find_mutual_friends("Alice", "Charlie") == []
    assert network.find_mutual_friends("Alice", "David") == []
    assert network.find_mutual_friends("Charlie", "Eve") == []

    network.add_friend("Bob", "David")
    network.add_friend("Charlie", "Eve")

    assert network.find_mutual_friends("Alice", "Charlie") == []
    assert network.find_mutual_friends("Bob", "David") == []
    assert network.find_mutual_friends("Charlie", "Eve") == ["Charlie"]

def test_suggest_connections():
    network = SocialNetwork()

    network.add_friend("Alice", "Bob")
    network.add_friend("Bob", "Charlie")
    network.add_friend("Charlie", "David")
    network.add_friend("Charlie", "Eve")

    assert network.suggest_connections("Alice") == []
    assert network.suggest_connections("Charlie") == []

def test_find_friends():
    network = SocialNetwork()

    network.add_friend("Alice", "Bob")
    network.add_friend("Alice", "Charlie")

    assert "Bob" in network.find_friends("Alice")
    assert "Charlie" in network.find_friends("Alice")
    assert "Alice" in network.find_friends("Bob")
    assert "Alice" in network.find_friends("Charlie")
