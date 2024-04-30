from typing import List
import random

class Solution:

    # Count # of 1s per row and col.
    # For each grid[i][j] == 1, # of right triangles can be formed with i,j as corner == (# of ones on row[i] - 1) * (# of ones on col[j] - 1)
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        onesPerRow = [0] * m
        for i in range(m):
            onesPerRow[i] = grid[i].count(1)
        onesPerCol = [0] * n
        for j in range(n):
            ones = 0
            for i in range(m):
                ones += 1 if grid[i][j] == 1 else 0
            onesPerCol[j] = ones
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += (onesPerRow[i] - 1) * (onesPerCol[j] - 1)
        return res


import unittest

class TestSolution(unittest.TestCase):

    def testGameOfLife(self):
        s=Solution()
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        s.gameOfLife(board)
        self.assertEqual(board, [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])

        board = [[1,1],[1,0]]
        s.gameOfLife(board)
        self.assertEqual(board, [[1,1],[1,1]])

if __name__ == '__main__':
    unittest.main()