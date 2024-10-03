from typing import List
import random

class Solution:

    # Find max value in the array in one pass
    def longestSubarray(self, nums: List[int]) -> int:
        res = curMax = lenOfCurMax = 0
        for num in nums:
            if num > curMax:
                curMax = num
                lenOfCurMax = 1
                res = 0
            elif num == curMax:
                lenOfCurMax += 1
            else:
                lenOfCurMax = 0
            res = max(res, lenOfCurMax)
        return res

    # Result of AND of a smaller number and a bigger number is always smaller than the bigger number
    # 1. If n < curMax, n & curMax < curMax
    # 2. If n == curMax, n & curMax == curMax
    # 3. If n > curMax, n & curMax < curMax
    # This is equivalent to find longest subarray with consecutive maximum value in the array
    def longestSubarrayUsingMax(self, nums: List[int]) -> int:
        maxValue = max(nums)
        res = countOfMax = 0
        for num in nums:
            if num == maxValue:
                countOfMax += 1
            else:
                countOfMax = 0
            res = max(res, countOfMax)
        return res

import unittest

class TestSolution(unittest.TestCase):

    def testGameOfLife(self):
        s=Solution()
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        s.gameOfLife(board)
        self.assertEqual(board, [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])

        board = [[1,1],[1,0]]
        s.gameOfLife(board)
        self.assertEqual(board, [[1,1],[1,1]])

if __name__ == '__main__':
    unittest.main()