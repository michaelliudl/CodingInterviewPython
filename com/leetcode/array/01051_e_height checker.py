from typing import List

class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        hs = sorted(heights)
        return sum(1 if heights[i] != hs[i] else 0 for i in range(len(heights)))

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()