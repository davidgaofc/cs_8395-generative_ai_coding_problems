from problems.problem_27 import Knapsack

def test_knapsack_dp():
    knapsack = Knapsack()

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    assert knapsack.knapsack_dp(weights, values, capacity) == 7

    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    assert knapsack.knapsack_dp(weights, values, capacity) == 220