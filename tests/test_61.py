from problems.problem_61 import StringAnalyzer

def test_count_vowels():
    analyzer = StringAnalyzer()
    assert analyzer.count_vowels("Hello, World!") == 3
    assert analyzer.count_vowels("Python is awesome!") == 6


def test_reverse_words():
    analyzer = StringAnalyzer()
    assert analyzer.reverse_words("Hello, World!") == "World! Hello,"
    assert analyzer.reverse_words("Python is awesome!") == "awesome! is Python"
