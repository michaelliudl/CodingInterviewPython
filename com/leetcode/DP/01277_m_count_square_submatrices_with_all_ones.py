from typing import List

class Solution:

    # dp[i][j] = matrix[i][j] when i == 0 or j == 0
    # dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 when i > 0 and j > 0 and matrix[i][j] == 1
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            dp[row][0] = matrix[row][0]
        for col in range(cols):
            dp[0][col] = matrix[0][col]
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 1:
                    dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
        return sum([sum(dp[i]) for i in range(rows)])
        

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