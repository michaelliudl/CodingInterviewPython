from typing import List
import math

class Solution:

    # Calculate total sum of all values' absolute
    # Find count of non positive numbers and smallest absolute value of numbers, if count of non positive is odd, minus double of the smallest absolute value
    # If count of non positive is even, they can all be converted to positive
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        totalSum = 0
        minAbs = math.inf   # Can flip smaller absolute positive to negative
        countNeg = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = matrix[i][j]
                totalSum += abs(num)
                minAbs = min(minAbs, abs(num))
                if num < 0:
                    countNeg += 1
        return totalSum - (countNeg & 1) * minAbs * 2

import unittest

class TestSolution(unittest.TestCase):
    def testMaxMatrixSum(self):
        s = Solution()
        self.assertEqual(s.maxMatrixSum(matrix = [[1,-1],[-1,1]]), 4)
        self.assertEqual(s.maxMatrixSum(matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]), 16)
        self.assertEqual(s.maxMatrixSum(matrix = [[-1,0,-1],[-2,1,3],[3,2,2]]), 15)
        self.assertEqual(s.maxMatrixSum(matrix = [[10000,10000,10000],[10000,10000,10000],[10000,10000,10000]]), 90000)
        self.assertEqual(s.maxMatrixSum(matrix = [[2,9,3],[5,4,-4],[1,7,1]]), 34)


if __name__ == '__main__':
    unittest.main()