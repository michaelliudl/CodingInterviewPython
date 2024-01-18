from typing import List,Deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dir=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(grid, x, y):
            return x>=0 and y>=0 and x<len(grid) and y<len(grid[0])

        def dfs(grid, x, y, visited, size):
            size+=1
            visited[x][y]=1
            for a,b in dir:
                x1,y1=x+a,y+b
                if valid(grid,x1,y1) and grid[x1][y1]==1 and not visited[x1][y1]:
                    size=dfs(grid, x1, y1, visited, size)
            return size

        if not grid:
            return 0
        r=0
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and not visited[i][j]:
                    size=dfs(grid, i, j, visited, size=0)
                    r=max(r,size)
        return r

        

import unittest

class TestSolution(unittest.TestCase):
    def testMaxAreaOfIsland(self):
        s = Solution()
        self.assertEqual(s.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]), 6)
        self.assertEqual(s.maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()