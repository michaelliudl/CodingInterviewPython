from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]
        # Sum down
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                self.prefixSum[row][col] = self.prefixSum[row - 1][col] + matrix[row - 1][col - 1]
        # Then sum right
        for col in range(1, cols + 1):
            for row in range(1, rows + 1):
                self.prefixSum[row][col] += self.prefixSum[row][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row2 + 1][col1] - self.prefixSum[row1][col2 + 1] + self.prefixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):
    def testNumMatrix(self):
        nm = NumMatrix(matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(nm.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(nm.sumRegion(1, 2, 2, 4), 12)


if __name__ == '__main__':
    unittest.main()