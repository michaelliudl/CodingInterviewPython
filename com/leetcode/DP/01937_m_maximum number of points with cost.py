from typing import List

class Solution:

    # DP top-down, saving max points possible for each column in each row
    # At each row, use `leftToRight` and `rightToLeft` arrays to track max possible points for both directions
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        # DP on rows
        dp = [0] * n
        for i in range(m):
            # DP on columns for left -> right and right -> left
            leftToRight = [0] * n
            leftToRight[0] = dp[0]
            for j in range(1, n):
                leftToRight[j] = max(leftToRight[j - 1] - 1, dp[j])     # Only need to consider adjacent columns
            rightToLeft = [0] * n
            rightToLeft[-1] = dp[-1]
            for j in range(n - 2, -1, -1):
                rightToLeft[j] = max(rightToLeft[j + 1] - 1, dp[j])
            for j in range(n):
                dp[j] = max(leftToRight[j], rightToLeft[j]) + points[i][j]
        return max(dp)

import unittest

class TestSolution(unittest.TestCase):
    def testMaxPoints(self):
        s = Solution()
        self.assertEqual(s.maxPoints(points = [[1,2,3],[1,5,1],[3,1,1]]), 9)
        self.assertEqual(s.maxPoints(points = [[1,5],[2,3],[4,2]]), 11)
        

if __name__ == '__main__':
    unittest.main()