from typing import List,Deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        pass


        

import unittest

class TestSolution(unittest.TestCase):
    def testLadderLength(self):
        s = Solution()
        self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]), 0)
        


if __name__ == '__main__':
    unittest.main()