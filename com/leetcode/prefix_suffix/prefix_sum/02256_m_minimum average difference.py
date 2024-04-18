from typing import List
import math

class Solution:

    def minimumAverageDifference(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):   # Prefix sum
            nums[i] += nums[i - 1]
        result = -1
        minAvgDiff = math.inf
        n = len(nums)
        for i in range(n):
            avg1 = nums[i] // (i + 1)   # Index 0 includes num at 0
            avg2 = 0 if i == n - 1 else (nums[-1] - nums[i]) // (n - 1 - i)     # Index (n-1)'s right is empty
            avgDiff = abs(avg1 - avg2)
            if avgDiff < minAvgDiff:
                minAvgDiff = avgDiff
                result = i
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testMatrixBlockSum(self):
        s = Solution()
        self.assertEqual(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1), 
                         [[12,21,16],[27,45,33],[24,39,28]])
        self.assertEqual(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2), 
                         [[45,45,45],[45,45,45],[45,45,45]])


if __name__ == '__main__':
    unittest.main()