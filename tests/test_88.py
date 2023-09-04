from problems.problem_88 import MatrixOperations

def test_transpose():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    operations = MatrixOperations(matrix)

    assert operations.transpose() == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
def test_calculate_determinant():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    operations = MatrixOperations(matrix)
    assert operations.calculate_determinant() == 0  # Replace with the actual determinant value
def test_multiply_by_scalar():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    operations = MatrixOperations(matrix)
    assert operations.multiply_by_scalar(2) == [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]
    ]