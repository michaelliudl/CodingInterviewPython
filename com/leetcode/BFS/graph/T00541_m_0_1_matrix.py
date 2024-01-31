from typing import List,Deque

class Solution:

    # BFS from 1s, time out
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and x<m and y>=0 and y<n
        
        def bfs(i,j):
            q=Deque()
            q.append((i,j))
            visited={}
            visited[(i,j)]=True
            dist=0
            while q:
                curLen=len(q)
                for _ in range(curLen):
                    x,y=q.popleft()
                    if mat[x][y]==0:
                        return dist
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if valid(nx,ny) and not (nx,ny) in visited:
                            visited[(nx,ny)]=True
                            q.append((nx,ny))
                dist+=1
            return dist

        if not mat: return mat
        m,n=len(mat),len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    dist=bfs(i,j)
                    mat[i][j]=dist
        return mat

import unittest

class TestSolution(unittest.TestCase):
    def testNumEnclaves(self):
        s = Solution()
        self.assertEqual(s.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(s.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()