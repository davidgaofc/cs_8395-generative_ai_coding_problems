class ArrayOperations:
    def __init__(self, rows, cols):
        """
        Represents an array for performing operations on a 2D array.

        Args:
            rows (int): The number of rows in the array.
            cols (int): The number of columns in the array.
        """
        self.rows = rows
        self.cols = cols
        self.array = [[0] * cols for _ in range(rows)]

    # TODO: Implement this function
    def set_value(self, row, col, value):
        """
        Sets the value of an element in the array.

        Args:
            row (int): The row index of the element.
            col (int): The column index of the element.
            value: The value to set.
        """
        pass

    # TODO: Implement this function
    def get_value(self, row, col):
        """
        Gets the value of an element in the array.

        Args:
            row (int): The row index of the element.
            col (int): The column index of the element.

        Returns:
            The value of the element.
        """
        pass

    # TODO: Implement this function
    def row_sum(self, row):
        """
        Calculates the sum of elements in a row.

        Args:
            row (int): The row index.

        Returns:
            The sum of elements in the row.
        """
        pass

    # TODO: Implement this function
    def col_sum(self, col):
        """
        Calculates the sum of elements in a column.

        Args:
            col (int): The column index.

        Returns:
            The sum of elements in the column.
        """
        pass