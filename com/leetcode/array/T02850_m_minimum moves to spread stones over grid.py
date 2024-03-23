from typing import List
import random

class Solution:

    def minimumMoves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        numZeros = 0
        for row in range(rows):
            for col in range(cols):
                numZeros += 1 if grid[row][col] == 0 else 0
        if numZeros == 0:
            return 0
        result = float('inf')
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    for rowA in range(rows):
                        for colA in range(cols):
                            if grid[rowA][colA] > 1:
                                grid[rowA][colA] -= 1
                                grid[row][col] += 1
                                result = min(result, abs(row - rowA) + abs(col - colA) + self.minimumMoves(grid))
                                grid[rowA][colA] += 1
                                grid[row][col] -= 1
        return result

import unittest

class TestSolution(unittest.TestCase):

    def testMinimumMoves(self):
        s=Solution()
        self.assertEqual(s.minimumMoves(grid = [[1,1,0],[1,1,1],[1,2,1]]), 3)
        self.assertEqual(s.minimumMoves(grid = [[1,3,0],[1,0,0],[1,0,3]]), 4)
        self.assertEqual(s.minimumMoves(grid = [[0,0,9],[0,0,0],[0,0,0]]), 18)

if __name__ == '__main__':
    unittest.main()