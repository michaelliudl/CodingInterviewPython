from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None:
            return 0
        r,sum,slow,fast=len(nums)+1,0,0,0
        while fast<len(nums):
            sum+=nums[fast]
            while sum>=target:
                r=min(r,(fast-slow+1))
                sum-=nums[slow]
                slow+=1
            fast+=1
        return 0 if r>len(nums) else r

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testMinSubArrayLen(self):
        self.assertEqual(self.s.minSubArrayLen(7, [2,3,1,2,4,3]), 2)
        self.assertEqual(self.s.minSubArrayLen(4, [1,4,4]), 1)
        self.assertEqual(self.s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0)

if __name__ == '__main__':
    unittest.main()