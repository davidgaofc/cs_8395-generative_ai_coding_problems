from problems.problem_44 import SocialNetwork

def test_add_user():
    network = SocialNetwork()
    network.add_user("Alice")
    assert "Alice" in network.users

def test_add_connection():
    network = SocialNetwork()
    network.add_user("Alice")
    network.add_user("Bob")
    network.add_connection("Alice", "Bob")
    assert network.are_connected("Alice", "Bob")

def test_get_friends():
    network = SocialNetwork()
    network.add_user("Alice")
    network.add_user("Bob")
    network.add_user("Charlie")
    network.add_connection("Alice", "Bob")
    network.add_connection("Bob", "Charlie")
    assert network.get_friends("Bob") == ["Alice", "Charlie"]

def test_are_connected():
    network = SocialNetwork()
    network.add_user("Alice")
    network.add_user("Bob")
    network.add_connection("Alice", "Bob")
    assert network.are_connected("Alice", "Bob")

def test_get_common_friends():
    network = SocialNetwork()
    network.add_user("Alice")
    network.add_user("Bob")
    network.add_user("Charlie")
    network.add_connection("Alice", "Bob")
    network.add_connection("Bob", "Charlie")
    assert network.get_common_friends("Alice", "Charlie") == ["Bob"]

def test_get_user_with_max_friends():
    network = SocialNetwork()
    network.add_user("Alice")
    network.add_user("Bob")
    network.add_user("Charlie")
    network.add_connection("Alice", "Bob")
    network.add_connection("Bob", "Charlie")
    assert network.get_user_with_max_friends() == "Bob"