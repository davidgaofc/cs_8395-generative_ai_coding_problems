from problems.problem_39 import RestaurantRecommendationSystem

def test_add_rating():
    rec_system = RestaurantRecommendationSystem()
    rec_system.add_rating(user_id=1, restaurant_id=101, rating=4)
    rec_system.add_rating(user_id=2, restaurant_id=101, rating=3)
    rec_system.add_rating(user_id=3, restaurant_id=102, rating=5)

    assert rec_system.ratings == {
        (1, 101): 4,
        (2, 101): 3,
        (3, 102): 5
    }

def test_get_recommendations():
    rec_system = RestaurantRecommendationSystem()
    rec_system.add_rating(user_id=1, restaurant_id=101, rating=4)
    rec_system.add_rating(user_id=1, restaurant_id=102, rating=5)
    rec_system.add_rating(user_id=2, restaurant_id=101, rating=3)
    rec_system.add_rating(user_id=2, restaurant_id=103, rating=4)
    rec_system.add_rating(user_id=3, restaurant_id=102, rating=5)
    rec_system.add_rating(user_id=3, restaurant_id=103, rating=2)

    recommendations = rec_system.get_recommendations(user_id=1)
    assert recommendations == [102]

    recommendations = rec_system.get_recommendations(user_id=2)
    assert recommendations == [102, 103]

    recommendations = rec_system.get_recommendations(user_id=3)
    assert recommendations == [103, 101]