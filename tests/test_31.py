from problems.problem_31 import ArrayOperations

def test_set_value():
    arr = ArrayOperations(3, 4)
    arr.set_value(1, 2, 7)
    assert arr.get_value(1, 2) == 7

def test_get_value():
    arr = ArrayOperations(3, 4)
    arr.set_value(1, 2, 7)
    assert arr.get_value(1, 2) == 7

def test_row_sum():
    arr = ArrayOperations(3, 4)
    arr.set_value(1, 0, 5)
    arr.set_value(1, 1, 6)
    arr.set_value(1, 2, 7)
    arr.set_value(1, 3, 8)
    assert arr.row_sum(1) == 26

def test_col_sum():
    arr = ArrayOperations(3, 4)
    arr.set_value(0, 3, 4)
    arr.set_value(1, 3, 8)
    arr.set_value(2, 3, 12)
    assert arr.col_sum(3) == 24