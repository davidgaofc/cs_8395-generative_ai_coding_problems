from problems.problem_38 import MatrixMultiplier


def test_multiply():
    multiplier = MatrixMultiplier()

    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[7, 8],
         [9, 10],
         [11, 12]]

    result = multiplier.multiply(A, B)
    assert result == [[58, 64], [139, 154]]