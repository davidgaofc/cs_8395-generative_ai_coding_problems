#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class User:
    """
    A class representing a user in a social media application.
    """

    def __init__(self, username):
        """
        Initializes a user with the given username.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.followers = set()
        self.following = set()

    def follow(self, other_user):
        """
        Makes the user follow another user.

        Args:
            other_user (User): The user to be followed.
        """
        # TODO: Implement the logic to follow another user
        pass

    def unfollow(self, other_user):
        """
        Makes the user unfollow another user.

        Args:
            other_user (User): The user to be unfollowed.
        """
        # TODO: Implement the logic to unfollow another user
        pass

    def get_followers(self):
        """
        Returns a set of followers of the user.

        Returns:
            set: A set of User objects representing followers.
        """
        # TODO: Implement the logic to get followers
        pass

    def get_following(self):
        """
        Returns a set of users that the user is following.

        Returns:
            set: A set of User objects representing following users.
        """
        # TODO: Implement the logic to get following users
        pass