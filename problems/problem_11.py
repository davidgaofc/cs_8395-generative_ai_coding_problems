#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class Product:
    def __init__(self, product_id, name, price):
        """
        Represents a product for online shopping.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        """
        Represents an online shopping cart.

        This class allows customers to add products to their shopping cart,
        view the items in the cart, and calculate the total cost.
        """
        self.items = []

    def add_item(self, product, quantity):
        """
        Adds a product to the shopping cart with the given quantity.

        Args:
            product (Product): Product to be added.
            quantity (int): Quantity of the product to be added.
        """
        pass

    def view_cart(self):
        """
        Displays the products and quantities in the shopping cart.

        Returns:
            str: A formatted string displaying the cart items.
        """
        pass

    def calculate_total(self):
        """
        Calculates the total cost of all items in the cart.

        Returns:
            float: Total cost of items in the cart.
        """
        pass