from problems.problem_60 import MatrixManipulator

def test_transpose():
    manipulator = MatrixManipulator()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert manipulator.transpose(matrix) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]



def test_rotate_clockwise():
    manipulator = MatrixManipulator()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert manipulator.rotate_clockwise(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

