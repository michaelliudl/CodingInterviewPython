from typing import List,Deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        dir=[(1,0),(0,1),(-1,0),(0,-1)]

        def valid(x, y):
            return x>=0 and y>=0 and x<m and y<n
        
        def dfs(x, y, reach):
            reach[x][y]=1
            for a,b in dir:
                x1,y1=x+a,y+b
                if valid(x1,y1) and not reach[x1][y1] and heights[x1][y1]>=heights[x][y]:
                    dfs(x1,y1,reach)
        
        if not heights:
            return [[]]
        m,n=len(heights),len(heights[0])
        pacReach=[[0]*n for _ in range(m)]
        atlReach=[[0]*n for _ in range(m)]
        for i in range(m):
            dfs(i, 0, pacReach)
            dfs(i, n-1, atlReach)
        for i in range(n):
            dfs(0, i, pacReach)
            dfs(m-1, i, atlReach)
        r=[]
        for i in range(m):
            for j in range(n):
                if pacReach[i][j] and atlReach[i][j]:
                    r.append([i,j])
        return r



    def pacificAtlanticBrute(self, heights: List[List[int]]) -> List[List[int]]:

        dir=[(1,0),(0,1),(-1,0),(0,-1)]

        def valid(x, y):
            return x>=0 and y>=0 and x<m and y<n

        def pacific(x,y):
            return x==0 or y==0

        def atlantic(x,y):
            return x==m-1 or y==n-1

        def bfs(grid, start, r):
            q=Deque()
            q.append(start)
            pac,atl=False,False
            visited={}
            while q:
                x,y=q.popleft()
                visited[(x,y)]=1
                pac=pacific(x,y) if not pac else pac
                atl=atlantic(x,y) if not atl else atl
                if pac and atl:
                    r.append(start)
                    return
                for a,b in dir:
                    x1,y1=x+a,y+b
                    if valid(x1,y1) and grid[x1][y1]<=grid[x][y] and not (x1,y1) in visited:
                        q.append([x1,y1])

        if not heights:
            return [[]]
        
        m,n=len(heights),len(heights[0])
        r=[]
        for i in range(m):
            for j in range(n):
                bfs(grid=heights, start=[i, j], r=r)
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testPacificAtlantic(self):
        s = Solution()
        self.assertEqual(s.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]), [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
        self.assertEqual(s.pacificAtlantic(heights = [[1]]), [[0,0]])


if __name__ == '__main__':
    unittest.main()