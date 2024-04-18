from typing import List
import math

class Solution:

    # Follow up of 2908, large constraint `3 <= nums.length <= 10 ** 5`
    # Find prefix and suffix of min elements
    def minimumSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        prefixMin = nums[:]
        for i in range(1, n):
            prefixMin[i] = min(prefixMin[i], prefixMin[i - 1])
        suffixMin = nums[:]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i], suffixMin[i + 1])
        result = math.inf
        for i in range(1, n - 1):
            if nums[i] > prefixMin[i] and nums[i] > suffixMin[i]:
                result = min(result, nums[i] + prefixMin[i] + suffixMin[i])
        return result if result != math.inf else -1

import unittest

class TestSolution(unittest.TestCase):
    def testNumMatrix(self):
        nm = NumMatrix(matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(nm.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(nm.sumRegion(1, 2, 2, 4), 12)


if __name__ == '__main__':
    unittest.main()