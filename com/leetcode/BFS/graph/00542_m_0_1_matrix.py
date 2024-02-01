from typing import List,Deque

class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and x<m and y>=0 and y<n
        
        if not mat: return mat
        m,n=len(mat),len(mat[0])
        dist=[[float('inf')]*n for _ in range(m)]   # distance array from inf
        
        q=Deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    dist[i][j]=0            # Set 0 cell's distance to 0
                    q.append((i,j))         # Enqueue all 0 cells
        
        while q:
            x,y=q.popleft()
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if valid(nx,ny) and dist[nx][ny] > dist[x][y]+1:        # Update ajacent 1 cell's dist to 1 and enqueue
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
        return dist

        


    # BFS from 1s, time out
    def updateMatrixFrom1s(self, mat: List[List[int]]) -> List[List[int]]:

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
    def testUpdateMatrix(self):
        s = Solution()
        self.assertEqual(s.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]), 
                         [[0,0,0],[0,1,0],[0,0,0]])
        self.assertEqual(s.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]), 
                         [[0,0,0],[0,1,0],[1,2,1]])
        


if __name__ == '__main__':
    unittest.main()