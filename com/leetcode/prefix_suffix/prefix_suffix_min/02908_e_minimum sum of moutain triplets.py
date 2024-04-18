from typing import List
import math

class Solution:
    # Brute force for small constraint `3 <= nums.length <= 50` O(n**2)
    def minimumSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        result = math.inf
        for i in range(1, n - 1):
            left = [num for num in nums[:i] if num < nums[i]]
            right = [num for num in nums[i + 1:] if num < nums[i]]
            if left and right:
                result = min(result, nums[i] + min(left) + min(right))
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