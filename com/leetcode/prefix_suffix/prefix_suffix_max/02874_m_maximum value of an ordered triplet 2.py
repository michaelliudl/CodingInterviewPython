from typing import List
import math

class Solution:

    # Follow up of 2873, large constraint `3 <= nums.length <= 10 ** 5`
    # Find prefix and suffix of max elements
    def minimumSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        prefixMax = nums[:]
        for i in range(1, n):
            prefixMax[i] = max(nums[i], prefixMax[i - 1])
        suffixMax = nums[:]
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(nums[i], suffixMax[i + 1])
        ret = 0
        for j in range(1, n - 1):
            if prefixMax[j] > nums[j]:      # Only consider prefix value larger than current
                ret = max(ret, (prefixMax[j] - nums[j]) * suffixMax[j + 1])     # Take suffix max value from `current + 1`
        return ret

import unittest

class TestSolution(unittest.TestCase):
    def testNumMatrix(self):
        nm = NumMatrix(matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(nm.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(nm.sumRegion(1, 2, 2, 4), 12)


if __name__ == '__main__':
    unittest.main()