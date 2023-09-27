#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class TrieNode:
    def __init__(self):
        self.children = {}
        self.times = 0


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.curr_input = ""
        self.populate(sentences, times)

    def populate(self, sentences, times):
        for i in range(len(sentences)):
            self.add_sentence(sentences[i], times[i])

    def add_sentence(self, sentence, times):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.times += times

    def find_hot_sentences(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        def dfs(node, prefix, results):
            if node.times > 0:
                results.append((prefix, node.times))
            for char, child in node.children.items():
                dfs(child, prefix + char, results)

        results = []
        dfs(node, prefix, results)
        results.sort(key=lambda x: (-x[1], x[0]))
        return [result[0] for result in results][:3]

    def input(self, c):
        if c == "#":
            self.add_sentence(self.curr_input, 1)
            self.curr_input = ""
            return []
        else:
            self.curr_input += c
            return self.find_hot_sentences(self.curr_input)

    # Unimplemented functions for the user to complete

    def insert(self, sentence: str, times: int) -> None:
        # TODO: Implement the insertion of a sentence with its times
        pass

    def search(self, prefix: str):
        # TODO: Implement the search for hot sentences with a given prefix
        pass