from typing import List, DefaultDict

class TrieNode:

    def __init__(self):
        self.children = DefaultDict()

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
    
    def search(self, word):
        prefixLen = 0
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefixLen += 1
        return prefixLen

class Solution:
    
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        trie = Trie()
        for num1 in arr1:
            trie.insert(str(num1))
        for num2 in arr2:
            res = max(res, trie.search(str(num2)))
        return res


import unittest

class TestSolution(unittest.TestCase):

    def testLongestCommonPrefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(arr1 = [32,33,35], arr2 = [10,12,32]), 2)
        self.assertEqual(s.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]), 3)
        self.assertEqual(s.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]), 0)


if __name__ == '__main__':
    unittest.main()
