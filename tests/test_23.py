import numpy as np
from problems.problem_23 import StatisticalAnalyzer

def test_calculate_mean():
    analyzer = StatisticalAnalyzer()
    data = [12, 15, 18, 21, 24]
    mean = analyzer.calculate_mean(data)
    assert np.isclose(mean, 18)

def test_calculate_standard_deviation():
    analyzer = StatisticalAnalyzer()
    data = [10, 12, 14, 16, 18]
    std_dev = analyzer.calculate_standard_deviation(data)
    assert np.isclose(std_dev, 2.8284271247461903)

def test_perform_t_test():
    analyzer = StatisticalAnalyzer()
    data1 = [22, 25, 28, 31, 34]
    data2 = [18, 22, 26, 30, 34]
    t_stat, p_value = analyzer.perform_t_test(data1, data2)
    assert np.isclose(t_stat, 1.3174657760732198)
    assert np.isclose(p_value, 0.22778132792363872)