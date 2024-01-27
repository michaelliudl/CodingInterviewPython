from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass

import unittest

class TestSolution(unittest.TestCase):
    def testKClosest(self):
        s = Solution()
        self.assertEqual(sorted(s.kClosest(points = [[1,3],[-2,2]], k = 1)), sorted([[-2,2]]))
        self.assertEqual(sorted(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)), sorted([[3,3],[-2,4]]))



if __name__ == '__main__':
    unittest.main()