from problems.problem_45 import Trie

def test_insert():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False

def test_search():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False

def test_startswith():
    trie = Trie()
    trie.insert("apple")
    assert trie.startswith("app") is True
    assert trie.startswith("banana") is False
