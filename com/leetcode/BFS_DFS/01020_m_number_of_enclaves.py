from typing import List,Deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        dir=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(grid, x, y):
            m,n=len(grid),len(grid[0])
            return x>=0 and y>=0 and x<m and y<n

        def dfs(grid, x, y):
            grid[x][y]=0
            for a,b in dir:
                x1,y1=x+a,y+b
                if valid(grid, x1, y1) and grid[x1][y1]==1:
                    dfs(grid, x1, y1)

        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            if grid[i][0]==1:
                dfs(grid, i, 0)
            if grid[i][n-1]==1:
                dfs(grid, i, n-1)
        for i in range(1, n-1):
            if grid[0][i]==1:
                dfs(grid, 0, i)
            if grid[m-1][i]==1:
                dfs(grid, m-1, i)
        return sum([sum(row) for row in grid])

        

import unittest

class TestSolution(unittest.TestCase):
    def testNumEnclaves(self):
        s = Solution()
        self.assertEqual(s.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(s.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()