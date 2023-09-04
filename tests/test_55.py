from problems.problem_55 import PalindromeChecker

def test_is_palindrome():
    assert PalindromeChecker.is_palindrome("radar") == True
    assert PalindromeChecker.is_palindrome("hello") == False
    assert PalindromeChecker.is_palindrome("level") == True
    assert PalindromeChecker.is_palindrome("algorithm") == False