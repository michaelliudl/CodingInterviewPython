from typing import List,Deque

class Solution:

    # DFS simplified code
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def dfs(x, y):
            nonlocal res
            if x < 0 or x >= m or y < 0 or y >= n:
                res += 1
                return
            if grid[x][y] == 0:
                res += 1
                return
            if grid[x][y] == 2:
                return
            grid[x][y] = 2
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return res
    
    # Scan each cell, if value = 1, assume it contributes 4 to perimeter, then minus 1 per each direct neighbor 1s
    def islandPerimeterScanCells(self, grid: List[List[int]]) -> int:

        d=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and y>=0 and x<m and y<n

        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        p=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    p+=4
                    for a,b in d:
                        x,y=i+a,j+b
                        if valid(x,y) and grid[x][y]==1:
                            p-=1
        return p

    def islandPerimeterDFS(self, grid: List[List[int]]) -> int:

        d=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and y>=0 and x<m and y<n
        
        def dfs(x,y,p):
            visited[x][y]=1
            p+=4
            for a,b in d:
                x1,y1=x+a,y+b
                if valid(x1,y1) and grid[x1][y1]==1:
                    p-=1
                    if not visited[x1][y1]:
                        p=dfs(x1,y1,p)
            return p

        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for i in range(m)]
        p=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    p+=dfs(i,j,p=0)
                    # break
        return p



        

import unittest

class TestSolution(unittest.TestCase):
    def testIslandPerimeter(self):
        s = Solution()
        self.assertEqual(s.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]), 16)
        self.assertEqual(s.islandPerimeter(grid = [[1]]), 4)
        self.assertEqual(s.islandPerimeter(grid = [[1,0]]), 4)
        


if __name__ == '__main__':
    unittest.main()