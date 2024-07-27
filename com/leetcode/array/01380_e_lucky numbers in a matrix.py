from typing import List

class Solution:
    
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        rowMins = [min(row) for row in matrix]
        colMaxes = [0] * n
        for j in range(n):
            for i in range(m):
                colMaxes[j] = max(colMaxes[j], matrix[i][j])
        res = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == rowMins[i] and matrix[i][j] == colMaxes[j]:
                    res.append(matrix[i][j])
        return res

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