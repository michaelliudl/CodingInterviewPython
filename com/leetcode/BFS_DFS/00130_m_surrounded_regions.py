from typing import List,Deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir=[(-1,0),(1,0),(0,-1),(0,1)]
        A,X,O='A','X','O'

        def valid(board, x, y):
            m,n=len(board),len(board[0])
            return x>=0 and y>=0 and x<m and y<n
        
        def dfs(board, x, y):
            board[x][y]=A
            for a,b in dir:
                x1,y1=x+a,y+b
                if valid(board, x1, y1) and board[x1][y1]==O:
                    dfs(board, x1, y1)


        if not board:
            return
        m,n=len(board),len(board[0])
        for i in range(m):
            if board[i][0]==O:
                dfs(board, i, 0)
            if board[i][n-1]==O:
                dfs(board, i, n-1)
        for i in range(1,n-1):
            if board[0][i]==O:
                dfs(board, 0, i)
            if board[m-1][i]==O:
                dfs(board, m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j]==O:
                    board[i][j]=X
                if board[i][j]==A:
                    board[i][j]=O
                



        

import unittest

class TestSolution(unittest.TestCase):
    def testNumEnclaves(self):
        s = Solution()
        self.assertEqual(s.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(s.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()