from problems.problem_24 import MaxSubarraySum

def test_max_subarray_bruteforce():
    max_sum = MaxSubarraySum()
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_sum.max_subarray_bruteforce(arr)
    assert result == 6

def test_max_subarray_divide_conquer():
    max_sum = MaxSubarraySum()
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_sum.max_subarray_divide_conquer(arr)
    assert result == 6