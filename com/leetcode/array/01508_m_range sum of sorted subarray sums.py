from typing import List
import random

class Solution:

    # Brute
    def rangeSumBrute(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subSums = []
        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum = (curSum + nums[j]) % MOD
                subSums.append(curSum)
        subSums.sort()
        res = 0
        for i in range(left - 1, right):    # `left` and `right` are 1-based
            res = (res + subSums[i]) % MOD
        return res

import unittest

class TestSolution(unittest.TestCase):

    def testMinimumMoves(self):
        s=Solution()
        self.assertEqual(s.minimumMoves(grid = [[1,1,0],[1,1,1],[1,2,1]]), 3)
        self.assertEqual(s.minimumMoves(grid = [[1,3,0],[1,0,0],[1,0,3]]), 4)
        self.assertEqual(s.minimumMoves(grid = [[0,0,9],[0,0,0],[0,0,0]]), 18)

if __name__ == '__main__':
    unittest.main()