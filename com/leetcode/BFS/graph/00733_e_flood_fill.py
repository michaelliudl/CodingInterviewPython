from typing import List,Deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and x<m and y>=0 and y<n

        if not image: return image
        m,n=len(image),len(image[0])
        if not valid(sr,sc): return image

        visited=[[False]*n for _ in range(m)]
        q=Deque()
        q.append((sr,sc))
        visited[sr][sc]=True
        oldColor=image[sr][sc]
        while q:
            x,y=q.popleft()
            image[x][y]=color
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if valid(nx,ny) and image[nx][ny]==oldColor and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny))
        return image

import unittest

class TestSolution(unittest.TestCase):
    def testNumEnclaves(self):
        s = Solution()
        self.assertEqual(s.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(s.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()