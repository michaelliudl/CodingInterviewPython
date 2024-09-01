from typing import List
import functools, math

class Solution:

    # Greedy math solution, result is sum of all primary factors of `n`
    def minSteps(self, n: int) -> int:
        res = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                n //= factor
                res += factor
            factor += 1
        return res

    # DP Bottom-up
    def minStepsBottomUp(self, n: int) -> int:
        if n <= 1:
            return 0
        # dp[i] is min number of steps to get `i` number of `A`s
        # Init with `i` which is most basic steps with 1 copy and i - 1 pastes
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i // 2, 2, -1):      # Loop in reverse to minimize pastes
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)    # Paste dp[j] number of `A`s (i // j) times
                    break
        return dp[n]

    # DP top-down, choose between copy current count or paste last count
    def minStepsTopDown(self, n: int) -> int:

        @functools.cache
        def dp(copy, paste):
            if copy == n:
                return 0
            if copy > n:
                return math.inf
            # Paste
            resPaste = 1 + dp(copy + paste, paste)
            # Copy & Paste
            resCopyPaste = 2 + dp(copy + copy, copy)
            return min(resPaste, resCopyPaste)

        if n <= 1:
            return 0
        return 1 + dp(copy=1, paste=1)

import unittest

class TestSolution(unittest.TestCase):
    def testMinSteps(self):
        s = Solution()
        self.assertEqual(s.minSteps(n = 3), 3)
        self.assertEqual(s.minSteps(n = 1), 0)
        

if __name__ == '__main__':
    unittest.main()