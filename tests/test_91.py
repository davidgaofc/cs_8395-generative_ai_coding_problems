from problems.problem_91 import GridNavigator

def test_get_current_position():
    navigator = GridNavigator(5, 5)

    assert navigator.get_current_position() == (0, 0)

    navigator.move_right()
    assert navigator.get_current_position() == (0, 1)

    navigator.move_down()
    navigator.move_down()
    assert navigator.get_current_position() == (2, 1)

    navigator.move_left()
    navigator.move_up()
    assert navigator.get_current_position() == (1, 0)

    navigator.move_left()
    assert navigator.get_current_position() == (1, 0)

def test_move_up():
    navigator = GridNavigator(5, 5)

    assert navigator.get_current_position() == (0, 0)

    navigator.move_right()
    assert navigator.get_current_position() == (0, 1)

    navigator.move_down()
    navigator.move_down()
    assert navigator.get_current_position() == (2, 1)

    navigator.move_left()
    navigator.move_up()
    assert navigator.get_current_position() == (1, 0)

    navigator.move_left()
    assert navigator.get_current_position() == (1, 0)
def test_move_down():
    navigator = GridNavigator(5, 5)

    assert navigator.get_current_position() == (0, 0)

    navigator.move_right()
    assert navigator.get_current_position() == (0, 1)

    navigator.move_down()
    navigator.move_down()
    assert navigator.get_current_position() == (2, 1)

    navigator.move_left()
    navigator.move_up()
    assert navigator.get_current_position() == (1, 0)

    navigator.move_left()
    assert navigator.get_current_position() == (1, 0)
def test_move_left():
    navigator = GridNavigator(5, 5)

    assert navigator.get_current_position() == (0, 0)

    navigator.move_right()
    assert navigator.get_current_position() == (0, 1)

    navigator.move_down()
    navigator.move_down()
    assert navigator.get_current_position() == (2, 1)

    navigator.move_left()
    navigator.move_up()
    assert navigator.get_current_position() == (1, 0)

    navigator.move_left()
    assert navigator.get_current_position() == (1, 0)
def test_move_right():
    navigator = GridNavigator(5, 5)

    assert navigator.get_current_position() == (0, 0)

    navigator.move_right()
    assert navigator.get_current_position() == (0, 1)

    navigator.move_down()
    navigator.move_down()
    assert navigator.get_current_position() == (2, 1)

    navigator.move_left()
    navigator.move_up()
    assert navigator.get_current_position() == (1, 0)

    navigator.move_left()
    assert navigator.get_current_position() == (1, 0)