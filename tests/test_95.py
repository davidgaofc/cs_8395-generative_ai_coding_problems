from problems.problem_95 import DataAnalyzer

def test_mean():
    data = [3, 5, 7, 5, 2, 3, 7, 8, 5, 4]
    analyzer = DataAnalyzer(data)

    assert analyzer.mean() == 4.9

def test_median():
    data = [3, 5, 7, 5, 2, 3, 7, 8, 5, 4]
    analyzer = DataAnalyzer(data)

    assert analyzer.median() == 4.5


def test_mode():
    data = [3, 5, 7, 5, 2, 3, 7, 8, 5, 4]
    analyzer = DataAnalyzer(data)

    assert analyzer.mode() == [5]