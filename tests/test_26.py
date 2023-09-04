from problems.problem_26 import LongestCommonSubsequence

def test_longest_common_subsequence():
    lcs = LongestCommonSubsequence()
    assert lcs.longest_common_subsequence("abcde", "ace") == 3
    assert lcs.longest_common_subsequence("abc", "abc") == 3
    assert lcs.longest_common_subsequence("abc", "def") == 0
    assert lcs.longest_common_subsequence("abcde", "ace") == 3
    assert lcs.longest_common_subsequence("abcdef", "abdefc") == 4