from typing import List

class Solution:

    # dp[i][j] is length of LCS for text 1 ended at i-1 and text 2 ended at j-1
    # dp[i][j] = (dp[i-1][j-1] + 1) if text1[i-1]==text2[j-1] else max(dp[i-1][j], dp[i][j-1])
    def longestCommonSubsequenceTwoD(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m,n,longest=len(text1),len(text2),0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                longest=max(longest, dp[i][j])
        return longest
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m,n,longest=len(text1),len(text2),0
        dp=[0]*(n+1)
        for i in range(1,m+1):
            prev=dp[0]                  # Store previous LCS length
            for j in range(1,n+1):
                cur=dp[j]               # Store current LCS length
                if text1[i-1]==text2[j-1]:
                    dp[j]=prev+1        # When same, add from prev
                else:
                    dp[j]=max(dp[j], dp[j-1])
                prev=cur
                longest=max(longest, dp[j])
        return longest


import unittest

class TestSolution(unittest.TestCase):
    def testLongestCommonSubsequence(self):
        s = Solution()
        self.assertEqual(s.longestCommonSubsequence(text1 = "abcde", text2 = "ace"), 3)
        self.assertEqual(s.longestCommonSubsequence(text1 = "abc", text2 = "abc"), 3)
        self.assertEqual(s.longestCommonSubsequence(text1 = "abc", text2 = "def"), 0)
        self.assertEqual(s.longestCommonSubsequence(text1 = "hofubmnylkra", text2 = "pqhgxgdofcvmr"), 5)
        self.assertEqual(s.longestCommonSubsequence(text1 = "abcba", text2 = "abcbcba"), 5)


if __name__ == '__main__':
    unittest.main()