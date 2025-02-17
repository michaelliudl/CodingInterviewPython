from typing import List

class Solution:

    # Count `1`s first, then iterate through the string and count `0`s on left side
    def maxScore(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
        zeroes = 0
        res = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeroes += 1
            else:
                ones -= 1
            res = max(res, zeroes + ones)
        return res
        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()