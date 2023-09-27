#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class DataStorage:
    """
    A class for storing and retrieving data using a custom storage mechanism.
    """

    def __init__(self):
        """
        Initializes the DataStorage with an empty storage.
        """
        self.data = {}

    def store(self, key, value):
        """
        Stores the given value using the provided key.

        Args:
            key (str): The key for storing the value.
            value: The value to be stored.
        """
        pass

    def retrieve(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key (str): The key to retrieve the value.

        Returns:
            The retrieved value, or None if the key is not found.
        """
        pass