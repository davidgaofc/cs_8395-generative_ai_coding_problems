#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class VendingMachine:
    """
    A class representing a simple vending machine.
    """

    def __init__(self):
        """
        Initializes a VendingMachine with initial stock and prices.
        """
        self.stock = {}  # A dictionary mapping item names to available quantities
        self.prices = {}  # A dictionary mapping item names to their prices

    def add_item(self, item_name, quantity, price):
        """
        Adds a new item to the vending machine.

        Args:
            item_name (str): The name of the item.
            quantity (int): The initial quantity of the item.
            price (float): The price of the item.
        """
        pass

    def purchase(self, item_name, amount_paid):
        """
        Handles a purchase attempt and returns the appropriate response.

        Args:
            item_name (str): The name of the item.
            amount_paid (float): The amount paid by the customer.

        Returns:
            str: A message indicating whether the purchase was successful or not.
        """
        pass