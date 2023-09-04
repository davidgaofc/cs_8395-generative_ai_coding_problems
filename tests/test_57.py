from problems.problem_57 import NumberConverter

def test_decimal_to_binary():
    assert NumberConverter.decimal_to_binary(10) == "1010"
    assert NumberConverter.decimal_to_binary(15) == "1111"
    assert NumberConverter.decimal_to_binary(0) == "0"



def test_binary_to_decimal():
    assert NumberConverter.binary_to_decimal("1010") == 10
    assert NumberConverter.binary_to_decimal("1111") == 15
    assert NumberConverter.binary_to_decimal("0") == 0

