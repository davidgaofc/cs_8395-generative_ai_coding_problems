#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class EmailValidator:
    """
    A class for validating email addresses.
    """

    def __init__(self, domain_whitelist):
        """
        Initializes the EmailValidator with a list of allowed email domains.

        Args:
            domain_whitelist (list): List of allowed email domains.
        """
        self.domain_whitelist = domain_whitelist

    def validate_email(self, email):
        """
        Validates an email address.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        pass