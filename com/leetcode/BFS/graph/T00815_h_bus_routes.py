from typing import List,Deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        pass


        

import unittest

class TestSolution(unittest.TestCase):
    def testLadderLength(self):
        s = Solution()
        self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]), 0)
        


if __name__ == '__main__':
    unittest.main()