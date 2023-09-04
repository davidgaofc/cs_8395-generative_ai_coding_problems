from problems.problem_76 import FibonacciSequence

def test_generate_sequence():
    sequence = FibonacciSequence(10)
    result = sequence.generate_sequence()
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_calculate_sum():
    sequence = FibonacciSequence(7)
    result = sequence.calculate_sum()
    assert result == 33

def test_calculate_average():
    sequence = FibonacciSequence(5)
    result = sequence.calculate_average()
    assert result == 2.4