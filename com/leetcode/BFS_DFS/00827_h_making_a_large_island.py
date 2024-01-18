from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        dir=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and y>=0 and x<m and y<n

        def dfs(x, y, visited, newIsland, size):
            visited[x][y]=1
            grid[x][y]=newIsland
            size+=1
            for a,b in dir:
                x1,y1=x+a,b+y
                if valid(x1,y1) and grid[x1][y1]==1 and not visited[x1][y1]:
                    size=dfs(x1,y1,visited, newIsland, size)
            return size

        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for i in range(m)]
        islands={}
        newIsland=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    newIsland+=1
                    size=dfs(i, j, visited, newIsland, size=0)
                    islands[newIsland]=size
        maxSize=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    size=1
                    adj=[]
                    for a,b in dir:
                        x1,y1=i+a,j+b
                        if valid(x1,y1) and grid[x1][y1]>1 and not grid[x1][y1] in adj:
                            adj.append(grid[x1][y1])
                            size+=islands[grid[x1][y1]]
                    maxSize=max(maxSize, size)
        return maxSize if maxSize>0 else islands[2]


import unittest

class TestSolution(unittest.TestCase):
    def testLargestIsland(self):
        s = Solution()
        self.assertEqual(s.largestIsland(grid = [[1,0],[0,1]]), 3)
        self.assertEqual(s.largestIsland(grid = [[1,1],[1,0]]), 4)
        self.assertEqual(s.largestIsland(grid = [[1,1],[1,1]]), 4)
        self.assertEqual(s.largestIsland(grid = [[0,0,0,0,0,0,0],
                                                 [0,1,1,1,1,0,0],
                                                 [0,1,0,0,1,0,0],
                                                 [1,0,1,0,1,0,0],
                                                 [0,1,0,0,1,0,0],
                                                 [0,1,0,0,1,0,0],
                                                 [0,1,1,1,1,0,0]]), 18)



if __name__ == '__main__':
    unittest.main()