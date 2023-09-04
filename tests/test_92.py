from problems.problem_92 import PerfectNumbers

def test_find_perfect_numbers():
    perfect_numbers = PerfectNumbers(10000)

    assert perfect_numbers.is_perfect(6) is True
    assert perfect_numbers.is_perfect(28) is True
    assert perfect_numbers.is_perfect(496) is True
    assert perfect_numbers.is_perfect(8128) is True
    assert perfect_numbers.is_perfect(12) is False
    assert perfect_numbers.is_perfect(30) is False

    assert perfect_numbers.find_perfect_numbers() == [6, 28, 496, 8128]

def test_is_perfect():
    perfect_numbers = PerfectNumbers(10000)

    assert perfect_numbers.is_perfect(6) is True
    assert perfect_numbers.is_perfect(28) is True
    assert perfect_numbers.is_perfect(496) is True
    assert perfect_numbers.is_perfect(8128) is True
    assert perfect_numbers.is_perfect(12) is False
    assert perfect_numbers.is_perfect(30) is False

    assert perfect_numbers.find_perfect_numbers() == [6, 28, 496, 8128]