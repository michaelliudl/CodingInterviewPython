from typing import List,Deque,Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and x<m and y>=0 and y<n
        
        def enqueueNeighbor(q,x,y):
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if valid(nx,ny) and grid[nx][ny]==1:
                    grid[nx][ny]=-1
                    q.append((nx,ny))
        
        def bfsOneRound(q):
            curLen=len(q)
            for _ in range(curLen):
                x,y=q.popleft()
                enqueueNeighbor(q,x,y)

        def bfs(starts):
            nonlocal maxRounds
            queues=[]
            for x,y in starts:
                q=Deque()
                enqueueNeighbor(q,x,y)
                queues.append(q)
            while True:
                end=True
                for q in queues:
                    if q:
                        end=False
                        bfsOneRound(q)
                if not end:
                    maxRounds+=1
                else:
                    break

        if not grid: return -1
        m,n=len(grid),len(grid[0])
        maxRounds=0
        starts=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    starts.append((i,j))
        bfs(starts)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return maxRounds
        

import unittest

class TestSolution(unittest.TestCase):
    def testOrangesRotting(self):
        s = Solution()
        self.assertEqual(s.orangesRotting(grid = [[0]]), 0)
        self.assertEqual(s.orangesRotting(grid = [[0,2]]), 0)
        self.assertEqual(s.orangesRotting(grid = [[2,1,1],[1,1,1],[0,1,2]]), 2)
        self.assertEqual(s.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]), 4)
        self.assertEqual(s.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]), -1)
        


if __name__ == '__main__':
    unittest.main()