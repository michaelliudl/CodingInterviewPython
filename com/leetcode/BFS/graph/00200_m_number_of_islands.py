from typing import List,Deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(grid, x, y):
            return x>=0 and x<len(grid) and y>=0 and y<len(grid[0])
        
        def dfsRecur(grid, startX, startY, visited):
            visited[startX][startY]=1
            for a,b in directions:
                x1,y1=startX+a,startY+b
                if valid(grid,x1,y1) and grid[x1][y1]=='1' and not visited[x1][y1]:
                    dfsRecur(grid, x1, y1, visited)
        
        def dfs(grid, startX, startY, visited):
            st=[]
            st.append((startX,startY))
            visited[startX][startY]=1
            while st:
                x,y=st.pop()
                for a,b in directions:
                    x1,y1=x+a,y+b
                    if valid(grid,x1,y1) and grid[x1][y1]=='1' and not visited[x1][y1]:
                        st.append((x1,y1))
                        visited[x1][y1]=1

        def bfs(grid, startX, startY, visited):
            q=Deque()
            q.append((startX,startY))
            visited[startX][startY]=1
            while q:
                x,y=q.popleft()
                for a,b in directions:
                    x1,y1=(x+a,y+b)
                    if valid(grid,x1,y1) and grid[x1][y1]=='1' and not visited[x1][y1]:
                        q.append((x1,y1))
                        visited[x1][y1]=1

        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for _ in range(m)]
        r=0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':
                    # bfs(grid, i, j, visited)
                    # dfs(grid, i, j, visited)
                    dfsRecur(grid, i, j, visited)
                    r+=1
        return r
        

import unittest

class TestSolution(unittest.TestCase):
    def testNumIslands(self):
        s = Solution()
        self.assertEqual(s.numIslands(grid = [
                        ["1","1","1","1","0"],
                        ["1","1","0","1","0"],
                        ["1","1","0","0","0"],
                        ["0","0","0","0","0"]
                        ]), 1)
        self.assertEqual(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
                        ]), 3)
        


if __name__ == '__main__':
    unittest.main()