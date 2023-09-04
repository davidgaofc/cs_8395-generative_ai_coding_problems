from problems.problem_47 import Room, Object, Player


def test_use():
    room = Room("Kitchen", "A room with a stove and sink.")
    key = Object("Key", "A shiny golden key.")
    player = Player("Alice")

    player.current_room = room
    room.add_object(key)
    player.take(key)

    # Test using an object
    player.use(key)
    assert key in player.inventory
    assert len(player.current_room.objects) == 1