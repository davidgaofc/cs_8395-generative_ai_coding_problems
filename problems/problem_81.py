class PhoneNumberValidator:
    """
    A class for validating phone numbers based on a set of rules.
    """

    def __init__(self, rules):
        """
        Initializes the PhoneNumberValidator with the provided rules.

        Args:
            rules (list): A list of callable functions that validate phone numbers.
        """
        self.rules = rules

    def validate(self, phone_number):
        """
        Validates the given phone number against the rules.

        Args:
            phone_number (str): The phone number to be validated.

        Returns:
            bool: True if the phone number is valid according to the rules, False otherwise.
        """
        pass