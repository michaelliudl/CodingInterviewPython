from typing import List

class Solution:
    
    # Simulation
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # right, down, left, up
        res = []
        row, col = rStart, cStart
        step = 1
        i = 0
        while len(res) < (rows * cols):
            for _ in range(2):
                dRow, dCol = dirs[i]
                for _ in range(step):
                    if 0 <= row < rows and 0 <= col < cols:
                        res.append([row, col])
                    row += dRow
                    col += dCol
                i = (i + 1) % 4
            step += 1
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testGenerateMatrix(self):
        s = Solution()
        self.assertEqual(s.generateMatrix(0), [[]])
        self.assertEqual(s.generateMatrix(1), [[1]])
        self.assertEqual(s.generateMatrix(2), [[1,2],[4,3]])
        self.assertEqual(s.generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])


if __name__ == '__main__':
    unittest.main()