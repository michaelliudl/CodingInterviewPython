from typing import List
import heapq
import random

class Solution:

    # Convert to minutes, sort, find min diff between adjacent. Lastly compare with diff between first and last minutes.
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [(int(tp[:2]) * 60 + int(tp[3:])) for tp in timePoints]
        minutes.sort()
        res = 24 * 60
        for i in range(1, len(minutes)):
            res = min(res, (minutes[i] - minutes[i - 1]))
        res = min(res, (24 * 60 - minutes[-1] + minutes[0]))
        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testFindKthLargest(self):
        self.assertEqual(self.s.findKthLargestQuickSelect([3,2,1,5,6,4],2), 5)
        self.assertEqual(self.s.findKthLargestQuickSelect([3,2,3,1,2,4,5,5,6],4), 4)
        # self.s.partition([3,2,3,1,2,4,5,5,6], 0, 8)


if __name__ == '__main__':
    unittest.main()