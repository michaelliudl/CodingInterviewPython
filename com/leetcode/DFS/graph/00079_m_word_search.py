from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and y>=0 and x<m and y<n
        
        def dfs(x,y,start):
            nonlocal found
            if found: return
            if start==k-1:
                found=True
                return
            visited[x][y]=True
            for dx,dy in dirs:
                a,b=x+dx,y+dy
                if valid(a,b) and not visited[a][b] and board[a][b]==word[start+1]:
                    dfs(a,b,start+1)
                    if found: break
            if not found:
                visited[x][y]=False

        if not board or not word: return False
        m,n,k=len(board),len(board[0]),len(word)
        visited=[[0]*n for _ in range(m)]
        found=False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    dfs(x=i, y=j, start=0)
        return found
        

import unittest

class TestSolution(unittest.TestCase):
    def testExist(self):
        s = Solution()
        self.assertEqual(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"), True)
        self.assertEqual(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"), True)
        self.assertEqual(s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"), False)


if __name__ == '__main__':
    unittest.main()