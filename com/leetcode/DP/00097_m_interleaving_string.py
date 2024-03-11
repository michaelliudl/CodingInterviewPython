from typing import List

class Solution:

    # Greedy moving pointers prefer to `s1` doesn't work

    # dp[i][j] is True is s1[:i-1] and s2[:j-1] constructs interleaving string for s3[:i+j-1]
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if (not s1 and s2 != s3) or (not s2 and s1 != s3):
            return False
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return False
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, len2 + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]) or (s3[i + j - 1] == s2[j - 1] and dp[i][j - 1])
        return dp[len1][len2]

        

import unittest

class TestSolution(unittest.TestCase):
    def testIsInterleave(self):
        s = Solution()
        self.assertEqual(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"), True)
        self.assertEqual(s.isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"), False)
        


if __name__ == '__main__':
    unittest.main()