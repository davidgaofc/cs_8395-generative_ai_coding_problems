from problems.problem_77 import MatrixOperations

def test_transpose():
    matrix = MatrixOperations([[1, 2, 3], [4, 5, 6]])
    matrix.transpose()
    assert matrix.matrix == [[1, 4], [2, 5], [3, 6]]

def test_sum_of_diagonals():
    matrix = MatrixOperations([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix.sum_of_diagonals() == 25

    matrix = MatrixOperations([[1, 2], [3, 4]])
    assert matrix.sum_of_diagonals() == 5