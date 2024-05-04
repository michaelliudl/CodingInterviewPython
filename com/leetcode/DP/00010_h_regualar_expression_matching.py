from typing import List

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True     # Empties match
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]     # s == '' matches p == '*'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]     # '.' matches any single character, just need to check if substrings before it also match
                elif p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = dp[i][j - 2]
                    elif s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j]
                elif s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]


import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()