from problems.problem_73 import TicTacToe

def test_make_move():
    game = TicTacToe()
    assert game.make_move(0, 0) is True
    assert game.make_move(1, 1) is True
    assert game.make_move(0, 1) is True
    assert game.make_move(1, 0) is True
    assert game.make_move(2, 2) is True
    assert game.make_move(0, 2) is True

    # Attempting to make a move on an already occupied spot
    assert game.make_move(2, 2) is False

def test_get_current_player():
    game = TicTacToe()
    assert game.get_current_player() == "X"
    game.make_move(0, 0)
    assert game.get_current_player() == "O"

def test_get_winner():
    game = TicTacToe()
    game.make_move(0, 0)
    game.make_move(1, 0)
    game.make_move(0, 1)
    game.make_move(1, 1)
    game.make_move(0, 2)
    assert game.get_winner() == "X"

def test_is_board_full():
    game = TicTacToe()
    assert game.is_board_full() is False
    game.make_move(0, 0)
    game.make_move(0, 1)
    game.make_move(0, 2)
    game.make_move(1, 0)
    game.make_move(1, 1)
    game.make_move(1, 2)
    game.make_move(2, 0)
    game.make_move(2, 1)
    game.make_move(2, 2)
    assert game.is_board_full() is True