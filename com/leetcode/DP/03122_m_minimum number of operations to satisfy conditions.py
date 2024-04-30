from typing import List
import math, functools

class Solution:

    def minimumOperations(self, grid: List[List[int]]) -> int:

        @functools.lru_cache(None)
        def dp(cur, prev):
            # Return min # of operations to update and satisfy conditions,
            # when (cur - 1) column is filled with `prev`
            if cur == n:
                return 0
            res = math.inf
            for candidate in range(10):
                if cur == 0 or candidate != prev:
                    # Total rows `m` - # of exiting `candidate` on `cur` column + dp(next column, candidate)
                    res = min(res, m - counts[cur][candidate] + dp(cur + 1, candidate))
            return res

        m, n = len(grid), len(grid[0])
        counts = [[0] * 10 for _ in range(n)]   # Get current count of each number on each column
        for i in range(m):
            for j in range(n):
                counts[j][grid[i][j]] += 1
        return dp(cur = 0, prev = 0)


import unittest

class TestSolution(unittest.TestCase):
    def testMinimumOperations(self):
        s = Solution()
        self.assertEqual(s.minimumOperations(grid = [[1,0,2],[1,0,2]]), 0)
        self.assertEqual(s.minimumOperations(grid = [[1,1,1],[0,0,0]]), 3)
        self.assertEqual(s.minimumOperations(grid = [[1],[2],[3]]), 2)


if __name__ == '__main__':
    unittest.main()