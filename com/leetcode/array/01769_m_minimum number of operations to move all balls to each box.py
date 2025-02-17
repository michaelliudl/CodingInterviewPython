from typing import List

class Solution:
    
    # Accumulate number of operations by counting number of 1s forwards and backwards
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        countOfOnes = moves = 0
        for i in range(len(boxes)):
            res[i] += moves
            countOfOnes += 1 if boxes[i] == '1' else 0
            moves += countOfOnes
        countOfOnes = moves = 0
        for i in range(len(boxes) - 1, -1, -1):
            res[i] += moves
            countOfOnes += 1 if boxes[i] == '1' else 0
            moves += countOfOnes
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testNumMatrix(self):
        nm = NumMatrix(matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(nm.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(nm.sumRegion(1, 2, 2, 4), 12)


if __name__ == '__main__':
    unittest.main()