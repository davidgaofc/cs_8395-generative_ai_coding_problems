from problems.problem_49 import WordFrequencyCounter


def test_add_word():
    counter = WordFrequencyCounter()
    counter.add_word("apple")
    counter.add_word("banana")
    counter.add_word("apple")

    assert counter.get_word_count("apple") == 2
    assert counter.get_word_count("banana") == 1

    print("test_add_word() passed!")


def test_remove_word():
    counter = WordFrequencyCounter()
    counter.add_word("apple")
    counter.add_word("banana")
    counter.remove_word("apple")

    assert counter.get_word_count("apple") == 0
    assert counter.get_word_count("banana") == 1



def test_get_word_count():
    counter = WordFrequencyCounter()
    counter.add_word("apple")
    counter.add_word("banana")
    counter.add_word("apple")

    assert counter.get_word_count("apple") == 2
    assert counter.get_word_count("banana") == 1
    assert counter.get_word_count("orange") == 0



def test_get_most_common_words():
    counter = WordFrequencyCounter()
    counter.add_word("apple")
    counter.add_word("banana")
    counter.add_word("apple")
    counter.add_word("banana")
    counter.add_word("cherry")

    most_common = counter.get_most_common_words(2)
    assert most_common == [("apple", 2), ("banana", 2)]

    most_common = counter.get_most_common_words(1)
    assert most_common == [("apple", 2)]
