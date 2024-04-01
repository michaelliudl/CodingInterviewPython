from typing import List

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
       pass
   def dimensions(self) -> list[]:
       pass

class Solution:

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        rowsWithOne = []
        for row in range(rows):
            if binaryMatrix.get(row, cols - 1) == 1:
                rowsWithOne.append(row)
        result = rows
        for row in rowsWithOne:
            low, high = 0, cols
            while low < high:
                mid = low + (high - low) // 2
                if binaryMatrix.get(row, mid) == 1:
                    high = mid
                else:
                    low = mid + 1
            result = min(result, low)
        return result if result < rows else -1

import unittest

class TestSolution(unittest.TestCase):
    def testMinEatingSpeed(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed(piles = [3,6,7,11], h = 8), 4)
        self.assertEqual(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5), 30)
        self.assertEqual(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6), 23)



if __name__ == '__main__':
    unittest.main()