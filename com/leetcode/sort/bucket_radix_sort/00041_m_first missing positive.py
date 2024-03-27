from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        n = len(nums)
        # Bucket sort into correct slots
        # nums[i]           = i + 1
        # nums[i] - 1       = i
        # nums[nums[i] - 1] = nums[i]
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i, num in enumerate(nums):
            if num != (i + 1):
                return i + 1
        return n + 1

import unittest

class TestSolution(unittest.TestCase):
    def testFirstMissingPositive(self):
        s = Solution()
        self.assertEqual(s.firstMissingPositive(nums = [1,1]), 2)
        self.assertEqual(s.firstMissingPositive(nums = [-5]), 1)
        self.assertEqual(s.firstMissingPositive(nums = [1,2,0]), 3)
        self.assertEqual(s.firstMissingPositive(nums = [3,4,-1,1]), 2)
        self.assertEqual(s.firstMissingPositive(nums = [7,8,9,11,12]), 1)

if __name__ == '__main__':
    unittest.main()