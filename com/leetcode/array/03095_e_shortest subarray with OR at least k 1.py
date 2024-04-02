from typing import List
import math

class Solution:

    # Brute for small constraint size
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return -1
        result = math.inf
        for i in range(len(nums)):
            bitOr = nums[i]
            for j in range(i, len(nums)):
                bitOr |= nums[j]
                if bitOr >= k:
                    result = min(result, j - i + 1)
        return result if result < math.inf else -1


import unittest

class TestSolution(unittest.TestCase):
    def testMinimumSubarrayLength(self):
        s = Solution()
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2], k = 0), 1)
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2,3], k = 2), 1)
        self.assertEqual(s.minimumSubarrayLength(nums = [2,1,8], k = 10), 3)
        self.assertEqual(s.minimumSubarrayLength(nums = [16,1,2,20,32], k = 45), 2)

if __name__ == '__main__':
    unittest.main()