from typing import List

class Solution:

    # dp[m-1][n-1] = dp[m-2][n-1] + dp[m-1][n-2]
    def uniquePaths(self, m: int, n: int) -> int:
        if m<=1 or n<=1:
            return 1
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePathsOneDArray(self, m: int, n: int) -> int:
        if m<=1 or n<=1:
            return 1
        dp=[1]*n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j]+=dp[j-1]
        return dp[n-1]


import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()