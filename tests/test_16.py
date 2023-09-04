from problems.problem_16 import Product, ShoppingCart, User, Order

def test_add_product():
    cart = ShoppingCart()
    product = Product(1, "Laptop", 999.99)
    cart.add_product(product)
    assert len(cart.products) == 1
    assert cart.products[0] == product

def test_calculate_total():
    cart = ShoppingCart()
    product1 = Product(2, "Phone", 599.99)
    product2 = Product(3, "Headphones", 99.99)
    cart.add_product(product1)
    cart.add_product(product2)
    total_price = cart.calculate_total()
    assert total_price == 699.98

def test_place_order():
    cart = ShoppingCart()
    product = Product(4, "Tablet", 299.99)
    cart.add_product(product)

    user = User(1, "John Doe", "john@example.com")
    order = Order(101, user, cart)
    order.place_order()

    assert len(cart.products) == 0