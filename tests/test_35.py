from problems.problem_35 import SetOperations

def test_union():
    set1 = SetOperations([1, 2, 3, 4, 5])
    set2 = SetOperations([3, 4, 5, 6, 7])
    result = set1.union(set2)
    assert result.elements == [1, 2, 3, 4, 5, 6, 7]

def test_intersection():
    set1 = SetOperations([1, 2, 3, 4, 5])
    set2 = SetOperations([3, 4, 5, 6, 7])
    result = set1.intersection(set2)
    assert result.elements == [3, 4, 5]

def test_difference():
    set1 = SetOperations([1, 2, 3, 4, 5])
    set2 = SetOperations([3, 4, 5, 6, 7])
    result = set1.difference(set2)
    assert result.elements == [1, 2]