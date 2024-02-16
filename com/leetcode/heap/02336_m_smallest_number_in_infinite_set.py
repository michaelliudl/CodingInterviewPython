from typing import List
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i+1 for i in range(2**10)]

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        return 0

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):
    def testKClosest(self):
        s = Solution()
        self.assertEqual(sorted(s.kClosest(points = [[1,3],[-2,2]], k = 1)), sorted([[-2,2]]))
        self.assertEqual(sorted(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)), sorted([[3,3],[-2,4]]))



if __name__ == '__main__':
    unittest.main()