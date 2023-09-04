from problems.problem_37 import ArrayOperations

def test_product_of_pairs():
    array = [2, 3, 4]
    operations = ArrayOperations(array)
    assert operations.product_of_pairs() == 72

def test_odd_count():
    array = [5, 10, 2, 7, 3]
    operations = ArrayOperations(array)
    assert operations.odd_count() == 3

def test_unique_elements():
    array = [1, 2, 3, 1, 2, 3, 4]
    operations = ArrayOperations(array)
    assert operations.unique_elements() == [1, 2, 3, 4]