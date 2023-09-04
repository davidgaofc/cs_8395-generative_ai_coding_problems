class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Implement this function
        pass

    def search(self, word: str) -> bool:
        # Implement this function
        pass

    def startswith(self, prefix: str) -> bool:
        # Implement this function
        pass