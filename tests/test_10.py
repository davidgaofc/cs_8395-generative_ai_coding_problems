import numpy as np
from problems.problem_10 import MatrixOperations

def test_matrix_addition():
    matrix_ops = MatrixOperations()

    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    result = matrix_ops.matrix_addition(matrix1, matrix2)
    expected = np.array([[6, 8], [10, 12]])
    assert np.array_equal(result, expected)

def test_matrix_multiplication():
    matrix_ops = MatrixOperations()

    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    result = matrix_ops.matrix_multiplication(matrix1, matrix2)
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(result, expected)

def test_matrix_transpose():
    matrix_ops = MatrixOperations()

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    result = matrix_ops.matrix_transpose(matrix)
    expected = np.array([[1, 4], [2, 5], [3, 6]])
    assert np.array_equal(result, expected)