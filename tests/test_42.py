from problems.problem_42 import MagicSquareChecker


def test_is_magic_square():
    magic_square_checker = MagicSquareChecker()

    magic_matrix = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    assert magic_square_checker.is_magic_square(magic_matrix) == True

    non_magic_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert magic_square_checker.is_magic_square(non_magic_matrix) == False
