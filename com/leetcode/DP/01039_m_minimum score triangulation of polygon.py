from typing import List,Deque
import math

class Solution:

    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for j in range(2, n):
            for i in range(j - 2, -1, -1):
                dp[i][j] = math.inf
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + values[i] * values[k] * values[j] + dp[k][j])
        return dp[0][n - 1]

import unittest

class TestSolution(unittest.TestCase):
    def testFindPaths(self):
        s = Solution()
        self.assertEqual(s.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0), 6)
        self.assertEqual(s.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1), 12)
        


if __name__ == '__main__':
    unittest.main()