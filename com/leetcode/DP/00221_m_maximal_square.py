from typing import List

class Solution:

    # dp[i][j] is largest side of square of '1's with i,j is bottom right co-ordinates
    # dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1, when matrix[i][j] == '1'
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        # Set dp array same size as matrix and init first row and column from matrix
        # Or set to rows + 1 and cols + 1 with all 0s
        dp = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            dp[row][0] = int(matrix[row][0])
        for col in range(cols):
            dp[0][col] = int(matrix[0][col])
        maxSide = max(dp[0])
        maxSide = max(maxSide, max([dp[row][0] for row in range(rows)]))
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == '1':
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
                    maxSide = max(maxSide, dp[row][col])
        return maxSide * maxSide

    # Brute
    def maximalSquareBrute(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        maxSquare = 0
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    maxSquare = 1
                    break
        if maxSquare == 0:
            return 0
        limit = min(rows, cols)
        for side in range(limit, 1, -1):
            for row in range(rows - side + 1):
                for col in range(cols - side + 1):
                    square = True
                    for i in range(row, row + side):
                        for j in range(col, col + side):
                            if matrix[i][j] == '0':
                                square = False
                                break
                        if not square:
                            break
                    if square:
                        return side * side
        return maxSquare



import unittest

class TestSolution(unittest.TestCase):
    def testMaximalSquare(self):
        s = Solution()
        self.assertEqual(s.maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 4)
        self.assertEqual(s.maximalSquare(matrix = [["0","1"],["1","0"]]), 1)
        self.assertEqual(s.maximalSquare(matrix = [["0"]]), 0)
        


if __name__ == '__main__':
    unittest.main()