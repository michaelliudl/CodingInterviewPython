from typing import List

class TrieNode:

    def __init__(self):
        self.children={}
        self.endFlag=False

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if not c in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
        node.endFlag=True

    def search(self, word: str) -> bool:
        endNode=self._find(word)
        return endNode is not None and endNode.endFlag

    def startsWith(self, prefix: str) -> bool:
        endNode=self._find(prefix)
        return endNode is not None

    def _find(self, word):
        node=self.root
        for c in word:
            if not node.children or not c in node.children:
                return None
            node=node.children[c]
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    # def testTrie(self):
    #     trie = Trie()
    #     trie.insert('apple')
    #     s=trie.search('apple')
    #     self.assertEqual(s, True)
    #     s=trie.search('app')
    #     self.assertEqual(s, False)
    #     s=trie.startsWith('app')
    #     self.assertEqual(s, True)
    #     trie.insert('app')
    #     s=trie.search('app')
    #     self.assertEqual(s, True)

    # def testTrie_1(self):
    #     trie = Trie()
    #     trie.insert('hotdog')
    #     s=trie.startsWith('dog')
    #     self.assertEqual(s, False)

    def testTrie_2(self):
        trie = Trie()
        trie.insert('app')
        trie.insert('apple')
        trie.insert('beer')
        trie.insert('add')
        trie.insert('jam')
        trie.insert('rental')
        s=trie.search('apps')
        self.assertEqual(s, False)
        s=trie.search('app')
        self.assertEqual(s, True)


if __name__ == '__main__':
    unittest.main()