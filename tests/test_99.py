from problems.problem_99 import OnlineStore

def test_add_product():
    store = OnlineStore()

    store.add_product("Laptop", 1000)
    store.add_product("Smartphone", 500)
    store.add_product("Headphones", 50)

    assert store.search_products("Phone") == ["Smartphone"]
    assert store.search_products("o") == ["Laptop", "Smartphone", "Headphones"]

    cart = ["Laptop", "Headphones"]
    assert store.checkout(cart) == 1050

    store.remove_product("Smartphone")
    assert store.search_products("Phone") == []
def test_remove_product():
    store = OnlineStore()

    store.add_product("Laptop", 1000)
    store.add_product("Smartphone", 500)
    store.add_product("Headphones", 50)

    assert store.search_products("Phone") == ["Smartphone"]
    assert store.search_products("o") == ["Laptop", "Smartphone", "Headphones"]

    cart = ["Laptop", "Headphones"]
    assert store.checkout(cart) == 1050

    store.remove_product("Smartphone")
    assert store.search_products("Phone") == []
def test_search_products():
    store = OnlineStore()

    store.add_product("Laptop", 1000)
    store.add_product("Smartphone", 500)
    store.add_product("Headphones", 50)

    assert store.search_products("Phone") == ["Smartphone"]
    assert store.search_products("o") == ["Laptop", "Smartphone", "Headphones"]

    cart = ["Laptop", "Headphones"]
    assert store.checkout(cart) == 1050

    store.remove_product("Smartphone")
    assert store.search_products("Phone") == []
def test_checkout():
    store = OnlineStore()

    store.add_product("Laptop", 1000)
    store.add_product("Smartphone", 500)
    store.add_product("Headphones", 50)

    assert store.search_products("Phone") == ["Smartphone"]
    assert store.search_products("o") == ["Laptop", "Smartphone", "Headphones"]

    cart = ["Laptop", "Headphones"]
    assert store.checkout(cart) == 1050

    store.remove_product("Smartphone")
    assert store.search_products("Phone") == []