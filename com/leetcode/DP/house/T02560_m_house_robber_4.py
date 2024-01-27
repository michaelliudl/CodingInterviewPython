from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:


    # Backtrack, timeout
    def minCapability(self, nums: List[int], k: int) -> int:

        def backtrack(startIndex, path: list):
            nonlocal r
            if len(path)==k:
                r=min(r,max(path))
                return
            for i in range(startIndex,n):
                path.append(nums[i])
                backtrack(i+2, path)
                path.pop()

        if not nums or k<=0 or len(nums)<2*k-1:
            return 0
        n,r=len(nums),float('inf')
        backtrack(startIndex=0, path=[])
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testMinCapability(self):
        s = Solution()
        self.assertEqual(s.minCapability(nums = [2,3,5,9], k = 2), 5)
        self.assertEqual(s.minCapability(nums = [2,7,9,3,1], k = 2), 2)
        


if __name__ == '__main__':
    unittest.main()