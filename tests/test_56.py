from problems.problem_56 import SentenceAnalyzer

def test_count_words():
    assert SentenceAnalyzer.count_words("Hello world") == 2
    assert SentenceAnalyzer.count_words("This is a test sentence") == 5
    assert SentenceAnalyzer.count_words("") == 0



def test_reverse_words():
    assert SentenceAnalyzer.reverse_words("Hello world") == "world Hello"
    assert SentenceAnalyzer.reverse_words("This is a test sentence") == "sentence test a is This"
    assert SentenceAnalyzer.reverse_words("") == ""

