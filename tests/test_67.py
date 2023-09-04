from problems.problem_67 import User

def test_follow():
    user1 = User("user1")
    user2 = User("user2")

    user1.follow(user2)
    assert user1.get_following() == {user2}
    assert user2.get_followers() == {user1}

    user1.unfollow(user2)
    assert user1.get_following() == set()
    assert user2.get_followers() == set()

def test_unfollow():
    user1 = User("user1")
    user2 = User("user2")

    user1.follow(user2)
    assert user1.get_following() == {user2}
    assert user2.get_followers() == {user1}

    user1.unfollow(user2)
    assert user1.get_following() == set()
    assert user2.get_followers() == set()



def test_get_followers():
    user1 = User("user1")
    user2 = User("user2")
    user3 = User("user3")

    user1.follow(user2)
    user1.follow(user3)
    user2.follow(user3)

    assert user1.get_following() == {user2, user3}
    assert user1.get_followers() == set()
    assert user2.get_following() == {user3}
    assert user2.get_followers() == {user1}
    assert user3.get_following() == set()
    assert user3.get_followers() == {user1, user2}

def test_get_following():
    user1 = User("user1")
    user2 = User("user2")
    user3 = User("user3")

    user1.follow(user2)
    user1.follow(user3)
    user2.follow(user3)

    assert user1.get_following() == {user2, user3}
    assert user1.get_followers() == set()
    assert user2.get_following() == {user3}
    assert user2.get_followers() == {user1}
    assert user3.get_following() == set()
    assert user3.get_followers() == {user1, user2}

