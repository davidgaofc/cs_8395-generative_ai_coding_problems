from problems.problem_30 import MemoizedPalindromeSubstrings

def test_palindrome_substrings():
    solution = MemoizedPalindromeSubstrings()

    assert solution.palindrome_substrings("abcbad") == ["bcb", "bcb"]
    assert solution.palindrome_substrings("racecar") == ["racecar", "aceca", "cec"]
    assert solution.palindrome_substrings("programming") == []