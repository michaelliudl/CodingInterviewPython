from typing import List
import math

class Solution:

    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = math.inf
        for i in range(4):
            res = min(res, (nums[n - 4 + i] - nums[i]))
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()