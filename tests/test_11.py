from problems.problem_11 import Product, ShoppingCart

def test_add_item():
    product1 = Product(1, "Item1", 10.99)
    product2 = Product(2, "Item2", 20.49)

    cart = ShoppingCart()

    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    assert cart.items[0]["product"] == product1
    assert cart.items[0]["quantity"] == 2
    assert cart.items[1]["product"] == product2
    assert cart.items[1]["quantity"] == 1

def test_view_cart():
    product1 = Product(1, "Item1", 10.99)
    product2 = Product(2, "Item2", 20.49)

    cart = ShoppingCart()

    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    cart_items = cart.view_cart()
    assert "Item1 (2 units)" in cart_items
    assert "Item2 (1 unit)" in cart_items

def test_calculate_total():
    product1 = Product(1, "Item1", 10.99)
    product2 = Product(2, "Item2", 20.49)

    cart = ShoppingCart()

    cart.add_item(product1, 2)
    cart.add_item(product2, 1)

    total = cart.calculate_total()
    assert total == (2 * 10.99) + 20.49