from typing import List

class Solution:

    # dp[i][j] is number of permutations with i elements and exactly j inversed pairs
    def kInversePairs(self, n: int, k: int) -> int:
        if n<0 or k<0: return 0
        dp=[[0]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,k+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                if j>=i:
                    dp[i][j] = dp[i][j] - dp[i-1][j-i]
                dp[i][j]%=(10**9+7)
        return dp[n][k]


import unittest

class TestSolution(unittest.TestCase):
    def testKInversePairs(self):
        s = Solution()
        self.assertEqual(s.kInversePairs(n = 3, k = 0), 1)
        self.assertEqual(s.kInversePairs(n = 3, k = 1), 2)
        # self.assertEqual(s.kInversePairs(n = 4, k = 4), 3)
        


if __name__ == '__main__':
    unittest.main()