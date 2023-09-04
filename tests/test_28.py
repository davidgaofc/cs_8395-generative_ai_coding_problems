from problems.problem_28 import PalindromeRearrangement

def test_can_form_palindrome():
    palindrome_check = PalindromeRearrangement()

    assert palindrome_check.can_form_palindrome("aab") == True
    assert palindrome_check.can_form_palindrome("abc") == False
    assert palindrome_check.can_form_palindrome("racecar") == True
    assert palindrome_check.can_form_palindrome("hello") == False
    assert palindrome_check.can_form_palindrome("level") == True