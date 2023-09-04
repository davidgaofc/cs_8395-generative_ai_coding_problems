from problems.problem_4 import clean_text, count_word_frequency, most_common_words

def test_clean_text():
    assert clean_text("Hello, World!") == "hello world"
    assert clean_text("Python is awesome!") == "python is awesome"
    assert clean_text("Testing the cleaning function.") == "testing the cleaning function"

def test_count_word_frequency():
    text = "Hello hello world World! This is a test."
    word_frequency = count_word_frequency(text)
    assert word_frequency == {'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'test': 1}

def test_most_common_words():
    text = "This is a test. Testing the most common words function."
    common_words = most_common_words(text, 3)
    assert common_words == [('this', 1), ('is', 1), ('a', 1)]