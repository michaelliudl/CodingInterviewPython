from typing import List,Deque

class Solution:

    # Split each cell into 3x3 smaller cells, mark diagonal if originally had a slash
    # Run DFS from empty smaller cells and count "Number of islands"
    def regionsBySlashes(self, grid: List[str]) -> int:

        def dfs(row, col):
            if row < 0 or row >= newDim or col < 0 or col >= newDim:
                return
            if splitGrid[row][col] != 0:
                return
            splitGrid[row][col] = 1     # Mark visited
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        n = len(grid)
        # Expand to (3 * n) size grid
        newDim = 3 * n
        splitGrid = [[0] * newDim for _ in range(newDim)]
        for row in range(n):
            for col in range(n):
                splitRow, splitCol = row * 3, col * 3
                if grid[row][col] == '/':
                    splitGrid[splitRow][splitCol + 2] = 1
                    splitGrid[splitRow + 1][splitCol + 1] = 1
                    splitGrid[splitRow + 2][splitCol] = 1
                elif grid[row][col] == '\\':
                    splitGrid[splitRow][splitCol] = 1
                    splitGrid[splitRow + 1][splitCol + 1] = 1
                    splitGrid[splitRow + 2][splitCol + 2] = 1
        # Run DFS on expanded grid
        res = 0
        for row in range(newDim):
            for col in range(newDim):
                if splitGrid[row][col] == 0:
                    dfs(row, col)
                    res += 1
        return res

        

import unittest

class TestSolution(unittest.TestCase):
    def testRegionsBySlashes(self):
        s = Solution()
        self.assertEqual(s.regionsBySlashes(grid = [" /","/ "]), 2)
        self.assertEqual(s.regionsBySlashes(grid = [" /","  "]), 1)
        self.assertEqual(s.regionsBySlashes(grid = ["/\\","\\/"]), 5)


if __name__ == '__main__':
    unittest.main()