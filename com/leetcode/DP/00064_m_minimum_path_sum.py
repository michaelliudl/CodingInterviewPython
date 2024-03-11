from typing import List

class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        for i in range(1, cols):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[rows - 1][cols - 1]

import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()