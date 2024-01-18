from typing import List,Deque

class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:

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