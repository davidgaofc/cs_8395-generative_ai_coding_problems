from problems.problem_54 import MathHelper

def test_is_prime():
    assert MathHelper.is_prime(2) == True
    assert MathHelper.is_prime(4) == False
    assert MathHelper.is_prime(17) == True
    assert MathHelper.is_prime(100) == False


def test_factorial():
    assert MathHelper.factorial(0) == 1
    assert MathHelper.factorial(1) == 1
    assert MathHelper.factorial(5) == 120
    assert MathHelper.factorial(10) == 3628800
