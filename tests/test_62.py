from problems.problem_62 import StringAnalyzer

def test_longest_palindrome_substring():
    analyzer = StringAnalyzer()
    assert analyzer.longest_palindrome_substring("babad") == "bab"
    assert analyzer.longest_palindrome_substring("cbbd") == "bb"


def test_is_anagram():
    analyzer = StringAnalyzer()
    assert analyzer.is_anagram("listen", "silent")
    assert not analyzer.is_anagram("hello", "world")
