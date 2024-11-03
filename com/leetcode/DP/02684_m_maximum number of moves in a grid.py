from typing import List

class Solution:

    # dp[i][j] is maximum number of moves while starting from (i, j)
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        for j in range(cols - 2, -1, -1):
            for i in range(rows):
                if grid[i][j + 1] > grid[i][j]:
                    dp[i][j] = dp[i][j + 1] + 1
                if i > 0 and grid[i - 1][j + 1] > grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + 1)
                if i < rows - 1 and grid[i + 1][j + 1] > grid[i][j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + 1)
        return max(dp[i][0] for i in range(rows))
        

import unittest

class TestSolution(unittest.TestCase):
    def testCountSquares(self):
        s = Solution()
        self.assertEqual(s.countSquares(matrix =
                        [
                        [0,1,1,1],
                        [1,1,1,1],
                        [0,1,1,1]
                        ]), 15)
        self.assertEqual(s.countSquares(matrix = 
                        [
                        [1,0,1],
                        [1,1,0],
                        [1,1,0]
                        ]), 7)
        


if __name__ == '__main__':
    unittest.main()