from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        m,n = len(matrix), len(matrix[0])
        rows, cols = 0, 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows |= 1 << i
                    cols |= 1 << j
        for i in range(256):            # Constraint, m,n <= 200
            mask = 1<<i
            if rows & mask == mask:
                for j in range(n):
                    matrix[i][j] = 0
            if cols & mask == mask:
                for j in range(m):
                    matrix[j][i] = 0


import unittest

class TestSolution(unittest.TestCase):
    def testSetZeroes(self):
        s = Solution()
        matrix = matrix = [[1,1,1],[1,0,1],[1,1,1]]
        s.setZeroes(matrix)
        self.assertEqual(matrix, [[1,0,1],[0,0,0],[1,0,1]])
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        s.setZeroes(matrix)
        self.assertEqual(matrix, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])

if __name__ == '__main__':
    unittest.main()