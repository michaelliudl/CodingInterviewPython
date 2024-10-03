from typing import List, DefaultDict

class TrieNode:

    def __init__(self):
        self.children = DefaultDict()
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def getScore(self, word):
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.count
        return score

class Solution:
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return [trie.getScore(word) for word in words]


import unittest

class TestSolution(unittest.TestCase):

    def testLongestCommonPrefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(arr1 = [32,33,35], arr2 = [10,12,32]), 2)
        self.assertEqual(s.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]), 3)
        self.assertEqual(s.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]), 0)


if __name__ == '__main__':
    unittest.main()
