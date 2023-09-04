class SocialNetwork:
    def __init__(self):
        """
        Initializes a social network graph.

        This class simulates a social network graph with the ability to add friends,
        find mutual friends, and suggest new connections based on common interests.
        """
        # TODO: Implement initialization
        pass

    def add_friend(self, user1, user2):
        """
        Adds a friend connection between two users.

        Args:
            user1 (str): First user's name.
            user2 (str): Second user's name.
        """
        # TODO: Implement adding friend connection
        pass

    def find_mutual_friends(self, user1, user2):
        """
        Finds mutual friends between two users.

        Args:
            user1 (str): First user's name.
            user2 (str): Second user's name.

        Returns:
            list: List of mutual friends' names.
        """
        # TODO: Implement finding mutual friends
        pass

    def suggest_connections(self, user):
        """
        Suggests potential connections for a user based on common interests.

        Args:
            user (str): User's name for whom connections are suggested.

        Returns:
            list: List of suggested connections' names.
        """
        # TODO: Implement suggesting connections
        pass

    def find_friends(self, user):
        """
        Finds friends for a given user.

        Args:
            user (str): User's name for whom to find friends.

        Returns:
            list: List of user's friends' names.
        """
        return self.network.get(user, [])