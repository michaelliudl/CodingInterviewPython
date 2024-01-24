from typing import List

class Solution:

    # dp[i][j] is min # of operations to make same between substring word1[:i] and word2[:j]
    # dp[i][j] = dp[i-1][j-1]                                                  if word1[i-1]==word2[j-1]
    # dp[i][j] = min(dp[i-1][j]+1,      dp[i][j-1]+1,       dp[i-1][j-1]+2)    if word1[i-1]<>word2[j-1]
    #                Delete from 1      Delete from 2       Delete from both
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
                    dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
        return dp[m][n]


    # Length diff of LCS with both
    def minDistanceLCS(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
        lcs=dp[m][n]
        return (m-lcs)+(n-lcs)



import unittest

class TestSolution(unittest.TestCase):
    def testMinDistance(self):
        s = Solution()
        self.assertEqual(s.minDistance(word1 = "sea", word2 = "eat"), 2)
        self.assertEqual(s.minDistance(word1 = "leetcode", word2 = "etco"), 4)
        


if __name__ == '__main__':
    unittest.main()