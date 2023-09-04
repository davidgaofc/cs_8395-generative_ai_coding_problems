from problems.problem_87 import DataProcessor

def test_filter_positive_numbers():
    processor = DataProcessor([5, -3, 10, 0, -8, 7])
    assert processor.filter_positive_numbers() == [5, 10, 7]
    assert processor.compute_average() == 2.1666666666666665
    assert processor.find_maximum() == 10

    processor = DataProcessor([-2, -5, -1])
    assert processor.filter_positive_numbers() == []
    assert processor.compute_average() == -2.6666666666666665
    assert processor.find_maximum() == -1

def test_compute_average():
    processor = DataProcessor([5, -3, 10, 0, -8, 7])
    assert processor.filter_positive_numbers() == [5, 10, 7]
    assert processor.compute_average() == 2.1666666666666665
    assert processor.find_maximum() == 10

    processor = DataProcessor([-2, -5, -1])
    assert processor.filter_positive_numbers() == []
    assert processor.compute_average() == -2.6666666666666665
    assert processor.find_maximum() == -1

def test_find_maximum():
    processor = DataProcessor([5, -3, 10, 0, -8, 7])
    assert processor.filter_positive_numbers() == [5, 10, 7]
    assert processor.compute_average() == 2.1666666666666665
    assert processor.find_maximum() == 10

    processor = DataProcessor([-2, -5, -1])
    assert processor.filter_positive_numbers() == []
    assert processor.compute_average() == -2.6666666666666665
    assert processor.find_maximum() == -1