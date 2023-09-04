from problems.problem_69 import ShoppingCart


def test_add_item():
    cart = ShoppingCart()
    cart.add_item("Apple", 0.5, 10)
    cart.add_item("Banana", 0.3, 5)

    assert cart.get_total() == 5.5




def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("Apple", 0.5, 10)
    cart.add_item("Banana", 0.3, 5)

    cart.remove_item("Apple")
    assert cart.get_total() == 1.5

def test_get_total():
    cart = ShoppingCart()
    cart.add_item("Apple", 0.5, 10)
    cart.add_item("Banana", 0.3, 5)

    assert cart.get_total() == 5.5
    cart = ShoppingCart()
    cart.add_item("Apple", 0.5, 10)
    cart.add_item("Banana", 0.3, 5)

    cart.remove_item("Apple")
    assert cart.get_total() == 1.5

