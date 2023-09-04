from problems.problem_100 import SystemDesign

def test_add_product():
    system = SystemDesign()

    system.add_product("p1", "Laptop", 1000)
    system.add_product("p2", "Phone", 800)

    system.add_user("u1", "Alice")
    system.add_user("u2", "Bob")

    system.purchase_product("u1", "p1")
    system.purchase_product("u1", "p2")
    system.purchase_product("u2", "p2")

    user1_purchases = system.get_user_purchases("u1")
    user2_purchases = system.get_user_purchases("u2")

    assert len(user1_purchases) == 2
    assert len(user2_purchases) == 1
    assert user1_purchases == ["Laptop", "Phone"]
    assert user2_purchases == ["Phone"]

def test_add_user():
    system = SystemDesign()

    system.add_product("p1", "Laptop", 1000)
    system.add_product("p2", "Phone", 800)

    system.add_user("u1", "Alice")
    system.add_user("u2", "Bob")

    system.purchase_product("u1", "p1")
    system.purchase_product("u1", "p2")
    system.purchase_product("u2", "p2")

    user1_purchases = system.get_user_purchases("u1")
    user2_purchases = system.get_user_purchases("u2")

    assert len(user1_purchases) == 2
    assert len(user2_purchases) == 1
    assert user1_purchases == ["Laptop", "Phone"]
    assert user2_purchases == ["Phone"]
def test_purchase_product():
    system = SystemDesign()

    system.add_product("p1", "Laptop", 1000)
    system.add_product("p2", "Phone", 800)

    system.add_user("u1", "Alice")
    system.add_user("u2", "Bob")

    system.purchase_product("u1", "p1")
    system.purchase_product("u1", "p2")
    system.purchase_product("u2", "p2")

    user1_purchases = system.get_user_purchases("u1")
    user2_purchases = system.get_user_purchases("u2")

    assert len(user1_purchases) == 2
    assert len(user2_purchases) == 1
    assert user1_purchases == ["Laptop", "Phone"]
    assert user2_purchases == ["Phone"]
def test_get_user_purchases():
    system = SystemDesign()

    system.add_product("p1", "Laptop", 1000)
    system.add_product("p2", "Phone", 800)

    system.add_user("u1", "Alice")
    system.add_user("u2", "Bob")

    system.purchase_product("u1", "p1")
    system.purchase_product("u1", "p2")
    system.purchase_product("u2", "p2")

    user1_purchases = system.get_user_purchases("u1")
    user2_purchases = system.get_user_purchases("u2")

    assert len(user1_purchases) == 2
    assert len(user2_purchases) == 1
    assert user1_purchases == ["Laptop", "Phone"]
    assert user2_purchases == ["Phone"]