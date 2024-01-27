from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass
        



import unittest

class TestSolution(unittest.TestCase):
    def testLastStoneWeight(self):
        s = Solution()
        self.assertEqual(s.lastStoneWeight(stones = [2,7,4,1,8,1]), 1)
        self.assertEqual(s.lastStoneWeight(stones=[1]), 1)



if __name__ == '__main__':
    unittest.main()