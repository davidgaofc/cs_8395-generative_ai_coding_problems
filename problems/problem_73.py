class TicTacToe:
    """
    A class that represents a simple game of Tic-Tac-Toe.
    """

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, row, col):
        """
        Makes a move on the Tic-Tac-Toe board.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            bool: True if the move was valid and successful, False otherwise.
        """
        pass

    def get_current_player(self):
        """
        Returns the symbol of the current player (either 'X' or 'O').

        Returns:
            str: The symbol of the current player.
        """
        pass

    def get_winner(self):
        """
        Checks if there's a winner and returns the winner's symbol.

        Returns:
            str: The symbol of the winner ('X', 'O'), or None if no winner.
        """
        pass

    def is_board_full(self):
        """
        Checks if the Tic-Tac-Toe board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        pass