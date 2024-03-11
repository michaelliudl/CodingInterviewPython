from typing import List

class Solution:

    # dp[i][j] is min sum of deletion to make s1[:i-1] == s2[:j-1]
    # dp[i][j] = dp[i-1][j-1]   when s1[i-1] == s2[j-1]
    # dp[i][j] = min((dp[i-1][j] + s1[i - 1]), (dp[i][j-1] + s2[j-1]))
    # First row and column should be initialized to prefix sum of s2 and s1
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1 and not s2:
            return 0
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for i in range(1, len2 + 1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min((dp[i-1][j] + ord(s1[i-1])), (dp[i][j-1] + ord(s2[j-1])))
        return dp[len1][len2]


import unittest

class TestSolution(unittest.TestCase):
    def testMinimumDeleteSum(self):
        s = Solution()
        self.assertEqual(s.minimumDeleteSum(s1 = "sea", s2 = "eat"), 231)
        self.assertEqual(s.minimumDeleteSum(s1 = "delete", s2 = "leet"), 403)
        


if __name__ == '__main__':
    unittest.main()