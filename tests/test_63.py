from problems.problem_63 import WordProcessor

def test_count_words():
    processor = WordProcessor("Hello, world! This is a test.")
    assert processor.count_words() == 6



def test_capitalize_text():
    processor = WordProcessor("hello world")
    assert processor.capitalize_text() == "Hello World"


