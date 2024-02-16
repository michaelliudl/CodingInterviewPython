from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        if len(nums) <= k: return k
        ans,slow,counter = 0,0,k
        for i in range(len(nums)):
            if nums[i] == 0:
                counter -= 1
            while counter < 0:
                if nums[slow] == 0:
                    counter +=1
                slow+=1
            ans = max(ans, (i-slow+1))
        return ans



import unittest

class TestSolution(unittest.TestCase):
    def testLongestOnes(self):
        s = Solution()
        self.assertEqual(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2), 6)
        self.assertEqual(s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3), 10)


if __name__ == '__main__':
    unittest.main()