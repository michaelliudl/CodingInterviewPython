from typing import List

class Solution:
    # Compare each element to it's top-left if exists
    # Follow up 1: load half of first row and half of second row and compare by 1 index offset. Keep last element of first row and first element of second row for second half comparison.
    # Follow up 2: load segments and compare per above
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True


import unittest

class TestSolution(unittest.TestCase):
    def testRotate(self):
        s = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if __name__ == '__main__':
    unittest.main()