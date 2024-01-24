from typing import List

class Solution:

    # dp[i][j] is longest palindrome subsequence for substring between i and j inclusive
    # dp[i][j] = dp[i+1][j-1]+2 if s[i]==s[j] when traversing i backwards [n-1,0] and j forwards [i,n)
    # dp[i][j] = max(dp[i+1][j], dp[i][j-1]) if s[i]!=s[j] pick longer one after adding s[i] or s[j] to s[i+1,j-1]
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=1
                elif s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]


import unittest

class TestSolution(unittest.TestCase):
    def testLongestPalindromeSubseq(self):
        s = Solution()
        self.assertEqual(s.longestPalindromeSubseq(s = "bbbab"), 4)
        self.assertEqual(s.longestPalindromeSubseq(s = "cbbd"), 2)
        


if __name__ == '__main__':
    unittest.main()