from typing import List

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums)==1: return True
        cover=0                                 # Look for position that can cover whole array
        for i in range(len(nums)):
            if i>cover: return False            # False if loop outside cover range
            cover=max(cover, (i+nums[i]))       # cover is index + value
            if cover>=len(nums)-1: return True
        return False


import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()