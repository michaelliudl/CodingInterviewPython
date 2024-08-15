from typing import List

class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def valid(row, col):
            nums = set()
            total = -1
            for i in range(row, row + 3):
                rowSum = 0
                for j in range(col, col + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    if grid[i][j] in nums:
                        return False
                    nums.add(grid[i][j])
                    rowSum += grid[i][j]
                if total == -1:
                    total = rowSum
                elif rowSum != total:
                    return False
            for j in range(col, col + 3):
                colSum = 0
                for i in range(row, row + 3):
                    colSum += grid[i][j]
                if colSum != total:
                    return False
            diagonal = counterDiagonal = 0
            for i in range(3):
                diagonal += grid[row + i][col + i]
                counterDiagonal += grid[row + i][col + 2 - i]
            return diagonal == total and counterDiagonal == total

        res = 0
        m, n = len(grid), len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                res += 1 if valid(row, col) else 0
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testNumMagicSquaresInside(self):
        s = Solution()
        self.assertEqual(s.numMagicSquaresInside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]), 1)
        self.assertEqual(s.numMagicSquaresInside(grid = [[8]]), 0)
        self.assertEqual(s.numMagicSquaresInside(grid = [[5,5,5],[5,5,5],[5,5,5]]), 0)
        self.assertEqual(s.numMagicSquaresInside(grid = [[10,3,5],[1,6,11],[7,9,2]]), 0)

if __name__ == '__main__':
    unittest.main()