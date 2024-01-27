from typing import List

class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testFindRedundantConnection(self):
        s = Solution()
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[1,3],[2,3]]), [2,3])
        self.assertEqual(s.findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]), [1,4])
        # self.assertEqual(s.findRedundantConnection([0,0,0]), [[0,0,0]])


if __name__ == '__main__':
    unittest.main()