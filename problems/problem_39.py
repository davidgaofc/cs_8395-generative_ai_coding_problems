#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class RestaurantRecommendationSystem:
    ratings = {}
    def __init__(self):
        """
        Initializes the restaurant recommendation system.
        """

        pass

    # TODO: Implement this function
    def add_rating(self, user_id, restaurant_id, rating):
        """
        Adds a user rating for a restaurant.

        Args:
            user_id (int): User ID.
            restaurant_id (int): Restaurant ID.
            rating (int): Rating score (1 to 5).
        """
        pass

    # TODO: Implement this function
    def get_recommendations(self, user_id, num_recommendations=5):
        """
        Generates restaurant recommendations for a user based on their ratings.

        Args:
            user_id (int): User ID.
            num_recommendations (int): Number of recommendations to generate.

        Returns:
            list of int: List of restaurant IDs recommended for the user.
        """
        pass