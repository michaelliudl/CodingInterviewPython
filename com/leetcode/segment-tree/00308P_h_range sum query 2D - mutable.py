from typing import List

'''
Given a 2D matrix matrix, handle multiple queries of the following types:

Update the value of a cell in matrix.
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
'''

# Prefix sum passes.
# More efficient to use segment tree / Fenwick tree TODO
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m, n = len(self.matrix), len(self.matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = self.prefix[i][j - 1] + matrix[i - 1][j - 1]
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                self.prefix[i][j] += self.prefix[i - 1][j]

    def update(self, row: int, col: int, val: int) -> None:
        oldVal = self.matrix[row][col]
        diff = val - oldVal
        self.matrix[row][col] = val
        m, n = len(self.matrix), len(self.matrix[0])
        for i in range(row + 1, m + 1):
            for j in range(col + 1, n + 1):
                self.prefix[i][j] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] + self.prefix[row1][col1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):
    def testNumMatrix(self):
        nm = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        nm.update(3, 2, 2)
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 10)
        


if __name__ == '__main__':
    unittest.main()