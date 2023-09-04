from problems.problem_48 import GroceryStore


def test_add_item():
    store = GroceryStore()
    store.add_item("Apple", 0.5, 10)
    store.add_item("Banana", 0.3, 20)

    assert "Apple" in store.inventory
    assert store.inventory["Apple"]["price"] == 0.5
    assert store.inventory["Apple"]["quantity"] == 10

    assert "Banana" in store.inventory
    assert store.inventory["Banana"]["price"] == 0.3
    assert store.inventory["Banana"]["quantity"] == 20



def test_remove_item():
    store = GroceryStore()
    store.add_item("Apple", 0.5, 10)
    store.remove_item("Apple")

    assert "Apple" not in store.inventory




def test_calculate_total():
    store = GroceryStore()
    store.add_item("Apple", 0.5, 10)
    store.add_item("Banana", 0.3, 20)

    total = store.calculate_total(["Apple", "Banana", "Apple"])
    assert total == 1.3

