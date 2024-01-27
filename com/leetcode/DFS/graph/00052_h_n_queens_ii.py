from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n<=0:
            return []
        r=[]
        self.backtrack(n, y=0, r=r, matrix=[[0]*n for _ in range(n)])
        return len(r)

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
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()