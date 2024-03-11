from typing import List, Deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def bfs(row, col):
            queue = Deque()
            queue.append((row, col))
            grid[row][col] = 1
            while queue:
                curRow, curCol = queue.popleft()
                for dRow, dCol in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nRow, nCol = curRow + dRow, curCol + dCol
                    if 0 <= nRow < rows and 0 <= nCol < cols and grid[nRow][nCol] == 0:
                        grid[nRow][nCol] = 1
                        queue.append((nRow, nCol))

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        for col in range(cols):
            if grid[0][col] == 0:
                bfs(0, col)
            if grid[rows - 1][col] == 0:
                bfs(rows - 1, col)
        for row in range(rows):
            if grid[row][0] == 0:
                bfs(row, 0)
            if grid[row][cols - 1] == 0:
                bfs(row, cols - 1)
        ans = 0
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if grid[row][col] == 0:
                    ans += 1
                    bfs(row, col)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()