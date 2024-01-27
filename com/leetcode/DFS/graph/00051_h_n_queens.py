from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n<=0:
            return []
        r=[]
        self.backtrack(n, y=0, r=r, matrix=[[0]*n for _ in range(n)])
        return [[''.join(['Q' if s2 else '.' for s2 in s1]) for s1 in s] for s in r]

    def valid(self, n, matrix, x, y):
        for j in range(0, y):
            if matrix[j][x]:
                return False
        i,j=x-1,y-1
        while i>=0 and j>=0:
            if matrix[j][i]:
                return False
            i-=1
            j-=1
        i,j=x+1,y-1
        while i<n and j>=0:
            if matrix[j][i]:
                return False
            i+=1
            j-=1
        return True
    
    def backtrack(self, n, y, r, matrix):
        if sum(sum(matrix[i]) for i in range(n))==n:
            r.append([row[:] for row in matrix])
            return
        for x in range(n):
            if self.valid(n, matrix, x, y):
                matrix[y][x]=1
                self.backtrack(n, y+1, r, matrix)
                matrix[y][x]=0


import unittest

class TestSolution(unittest.TestCase):
    def testSolveNQueens(self):
        s = Solution()

        self.assertEqual(s.valid(4, [[1,0,0,0],[0,0,0,1]], 1, 2), True)

        self.assertEqual(s.solveNQueens(n = 4), [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
        # self.assertEqual(s.solveNQueens(n = 1), [["Q"]])
        


if __name__ == '__main__':
    unittest.main()