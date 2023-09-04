class EmailManager:
    """
    A class for managing emails and their attributes.
    """

    def __init__(self):
        """
        Initializes the EmailManager with an empty list of emails.
        """
        self.emails = []

    def send_email(self, sender, recipient, subject, message):
        """
        Sends an email from the sender to the recipient with the given subject and message.

        Args:
            sender (str): The sender's email address.
            recipient (str): The recipient's email address.
            subject (str): The subject of the email.
            message (str): The content of the email.
        """
        pass

    def get_inbox(self, email):
        """
        Retrieves the inbox of a specific email address.

        Args:
            email (str): The email address to retrieve the inbox for.

        Returns:
            list: A list of emails in the inbox.
        """
        pass

    def get_sent(self, email):
        """
        Retrieves the sent emails of a specific email address.

        Args:
            email (str): The email address to retrieve the sent emails for.

        Returns:
            list: A list of sent emails.
        """
        pass