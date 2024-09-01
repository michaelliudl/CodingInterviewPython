from typing import List
import functools

class Solution:

    # DP bottom-up, dp[i][j] is minimum number of turns to print s[i..j]
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for j in range(n):
            for i in range(j, -1, -1):
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] - (1 if s[k] == s[j] else 0))
        return dp[0][n - 1]

    # DP top-down
    def strangePrinterTopDown(self, s: str) -> int:

        @functools.cache
        def dp(low, high):
            if low > high:
                return 0
            res = dp(low + 1, high) + 1
            for mid in range(low + 1, high + 1):
                if s[mid] == s[low]:
                    res = min(res, dp(low, mid - 1) + dp(mid + 1, high))
            return res

        n = len(s)
        return dp(low=0, high=(n - 1))

import unittest

class TestSolution(unittest.TestCase):
    def testStrangePrinter(self):
        s = Solution()
        self.assertEqual(s.strangePrinter(s = "aaabbb"), 2)
        self.assertEqual(s.strangePrinter(s = "aba"), 2)
        # self.assertEqual(s.strangePrinter(s = "LEETCODE"), 92)


if __name__ == '__main__':
    unittest.main()