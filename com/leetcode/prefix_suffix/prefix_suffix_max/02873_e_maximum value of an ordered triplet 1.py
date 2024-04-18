from typing import List
import math

class Solution:
    # Brute force for small constraint `3 <= nums.length <= 100` O(n**2)
    def maximumTripletValue(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        n = len(nums)
        for j in range(1, n - 1):
            left = [nums[i] for i in range(j) if nums[i] > nums[j]]
            if left:
                result = max(result, (max(left) - nums[j]) * max(nums[j + 1:]))
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testNumMatrix(self):
        nm = NumMatrix(matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(nm.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(nm.sumRegion(1, 2, 2, 4), 12)


if __name__ == '__main__':
    unittest.main()