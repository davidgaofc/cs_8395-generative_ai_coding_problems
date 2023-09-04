from problems.problem_52 import UniqueWordsCounter

def test_count_unique_words():
    text = "This is a test. This is only a test."
    counter = UniqueWordsCounter(text)
    unique_word_count = counter.count_unique_words()

    assert unique_word_count == 6