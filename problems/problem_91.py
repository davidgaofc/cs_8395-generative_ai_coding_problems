#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class GridNavigator:
    """
    A class for navigating a grid of cells.
    """

    def __init__(self, rows, cols):
        """
        Initializes the GridNavigator with the specified number of rows and columns.

        Args:
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]

    def move_up(self):
        """
        Moves the navigator one cell up (if possible).
        """
        pass

    def move_down(self):
        """
        Moves the navigator one cell down (if possible).
        """
        pass

    def move_left(self):
        """
        Moves the navigator one cell left (if possible).
        """
        pass

    def move_right(self):
        """
        Moves the navigator one cell right (if possible).
        """
        pass

    def get_current_position(self):
        """
        Retrieves the current position of the navigator.

        Returns:
            Tuple containing the row and column of the current position.
        """
        pass