from typing import List

class Solution:

    # dp[i][j] is min edit distance between word1[:i-1] and word2[:j-1]
    # dp[i][j] = dp[i-1][j-1]       if word1[i-1]==word2[j-1] Do nothing
    # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j],              dp[i][j-1]) + 1         Choose min from result of previous 3 operations and add 1
    #                Replace       Delete 1 from word1      Delete 1 from word2
    # Equivalent to                Add 1 in word 2          Add 1 in word1
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0]=i
        for j in range(1,n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]

import unittest

class TestSolution(unittest.TestCase):
    def testMinDistance(self):
        s = Solution()
        self.assertEqual(s.minDistance(word1 = "horse", word2 = "ros"), 3)
        self.assertEqual(s.minDistance(word1 = "intention", word2 = "execution"), 5)
        


if __name__ == '__main__':
    unittest.main()