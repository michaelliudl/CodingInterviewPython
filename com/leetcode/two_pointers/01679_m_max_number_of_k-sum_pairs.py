from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if not nums or len(nums)<2 or k<=0: return 0
        nums.sort()
        ans=0
        low,high=0,len(nums)-1
        while low<high:
            cur=nums[low]+nums[high]
            if cur<k:
                low+=1
            elif cur>k:
                high-=1
            else:
                low+=1
                high-=1
                ans+=1
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()