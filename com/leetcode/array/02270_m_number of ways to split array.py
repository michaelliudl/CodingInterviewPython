from typing import List

class Solution:
    
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum = 0
        rightsum = sum(nums)
        res = 0
        for i in range(len(nums) - 1):
            leftSum += nums[i]
            rightsum -= nums[i]
            if leftSum >= rightsum:
                res += 1
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