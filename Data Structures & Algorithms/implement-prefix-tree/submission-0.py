class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for each in word:
            if each not in curr.children:
                curr.children[each] = TrieNode()
            curr = curr.children[each]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for each in word:
            if each not in curr.children:
                return False
            curr = curr.children[each]
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for each in prefix:
            if each not in curr.children:
                return False
            curr = curr.children[each]
        return True