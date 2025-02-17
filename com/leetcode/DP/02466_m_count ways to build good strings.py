from typing import List
import math, functools

class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        kMode = 10 ** 9 + 7
        dp = [0] * (high + 1)   # dp[i] # of ways to build good strings with length i
        dp[0] = 1
        res = 0
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % kMode
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % kMode
            if i >= low:
                res = (res + dp[i]) % kMode
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testMinimumOperations(self):
        s = Solution()
        self.assertEqual(s.minimumOperations(grid = [[1,0,2],[1,0,2]]), 0)
        self.assertEqual(s.minimumOperations(grid = [[1,1,1],[0,0,0]]), 3)
        self.assertEqual(s.minimumOperations(grid = [[1],[2],[3]]), 2)


if __name__ == '__main__':
    unittest.main()