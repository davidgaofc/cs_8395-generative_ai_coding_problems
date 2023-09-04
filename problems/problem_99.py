class OnlineStore:
    """
    A class representing an online store.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        """
        Adds a new product to the online store.

        Args:
            product_name: The name of the product.
            price: The price of the product.
        """
        pass

    def remove_product(self, product_name):
        """
        Removes a product from the online store.

        Args:
            product_name: The name of the product to be removed.
        """
        pass

    def search_products(self, keyword):
        """
        Searches for products containing a given keyword.

        Args:
            keyword: The keyword to search for.

        Returns:
            A list of product names containing the keyword.
        """
        pass

    def checkout(self, cart):
        """
        Performs checkout for the items in the cart.

        Args:
            cart: A list of product names in the cart.

        Returns:
            The total price of the items in the cart.
        """
        pass