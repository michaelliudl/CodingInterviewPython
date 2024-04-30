from typing import List

class Solution:

    # DP forward by starting from each number and find next reachable number
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][4] + dp[i - 1][6]) % MOD
            dp[i][1] = (dp[i - 1][6] + dp[i - 1][8]) % MOD
            dp[i][2] = (dp[i - 1][7] + dp[i - 1][9]) % MOD
            dp[i][3] = (dp[i - 1][4] + dp[i - 1][8]) % MOD
            dp[i][4] = (dp[i - 1][0] + dp[i - 1][3] + dp[i - 1][9]) % MOD
            dp[i][6] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][7]) % MOD
            dp[i][7] = (dp[i - 1][2] + dp[i - 1][6]) % MOD
            dp[i][8] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
            dp[i][9] = (dp[i - 1][2] + dp[i - 1][4]) % MOD
        return sum(dp[-1]) % MOD


import unittest

class TestSolution(unittest.TestCase):
    def testLargestDivisibleSubset(self):
        s = Solution()
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,3]), [2,1])
        self.assertEqual(s.largestDivisibleSubset(nums = [1,2,4,8]), [8,4,2,1])
        


if __name__ == '__main__':
    unittest.main()