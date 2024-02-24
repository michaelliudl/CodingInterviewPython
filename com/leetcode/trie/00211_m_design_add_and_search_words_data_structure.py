from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
    
    def search(self, word):
        def dfs(node, start):
            nonlocal found, result
            if found:
                return
            if start == len(word):
                if node and node.word:
                    found = True
                    result = node.word
                return
            if word[start] == '.':
                for _,child in node.children.items():
                    if not found:
                        dfs(child, start=start+1)
            elif word[start] in node.children:
                dfs(node.children[word[start]], start=start+1)
            
        found = False
        result = None
        dfs(self.root, start=0)
        return result

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        if not word: return
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        if not word: return False
        result=self.trie.search(word)
        return result is not None

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testWordDictionary(self):
        wd = WordDictionary()
        wd.addWord('bad')
        wd.addWord('dad')
        wd.addWord('mad')
        self.assertEqual(wd.search('pad'), False)
        self.assertEqual(wd.search('bad'), True)
        self.assertEqual(wd.search('.ad'), True)
        self.assertEqual(wd.search('b..'), True)
        

if __name__ == '__main__':
    unittest.main()