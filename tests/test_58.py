from problems.problem_58 import WordCounter

def test_count_words():
    assert WordCounter.count_words("Hello world") == 2
    assert WordCounter.count_words("This is a test.") == 4
    assert WordCounter.count_words("") == 0


def test_most_common_words():
    text = "This is a test. This is only a test."
    result = WordCounter.most_common_words(text, 2)
    expected_result = [("this", 2), ("is", 2)]
    assert result == expected_result