from typing import List, DefaultDict

class Solution:

    # Result is 0 if input has 0 or more than 1 islands
    # When input has 1 island, result is 1 if it has a side of width 1, otherwise result is 2 for cutting one corner
    def minDays(self, grid: List[List[int]]) -> int:

        def dfs(i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == 0 or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i - 1, j, visited)
            dfs(i + 1, j, visited)
            dfs(i, j - 1, visited)
            dfs(i, j + 1, visited)

        def isDisconnected():
            count = 0
            visited = set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        count += 1
                        if count > 1:
                            return True
                        dfs(i, j, visited)
            return count != 1   # Graph is considered disconnected if it has 0 or more than 1 islands

        m, n = len(grid), len(grid[0])
        # Already disconnected
        if isDisconnected():
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Flip one cell and check if it's disconnected
                    grid[i][j] = 0
                    if isDisconnected():
                        return 1
                    # Revert flipping
                    grid[i][j] = 1
        return 2

import unittest

class TestSolution(unittest.TestCase):
    def testMinDays(self):
        s = Solution()
        self.assertEqual(s.minDays(grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]), 1)
        self.assertEqual(s.minDays(grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]), 2)
        self.assertEqual(s.minDays(grid = [[1,1]]), 2)
        
if __name__ == '__main__':
    unittest.main()