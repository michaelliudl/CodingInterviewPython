from typing import List

class Solution:

    # dp[i][j] is # of substrings of t ending at (j-1) that are subsequences in substring of s ending at (i-1)
    # Only backtrack i index of s, since subsequence needs to contain all characters of substring of t
    # dp[i][j] = dp[i-1][j-1] + dp[i-1][j]      If s[i-1]==t[j-1], consider subsequence of s that ends at (i-1) and previous ones
    # dp[i][j] = dp[i-1][j]                     If s[i-1]<>t[j-1], only consider previous subsequences of s
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]

            


import unittest

class TestSolution(unittest.TestCase):
    def testNumDistinct(self):
        s = Solution()
        self.assertEqual(s.numDistinct(s = "rabbbit", t = "rabbit"), 3)
        self.assertEqual(s.numDistinct(s = "babgbag", t = "bag"), 5)
        


if __name__ == '__main__':
    unittest.main()