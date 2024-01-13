from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recur(nums, start, end):
            if start>end:
                return None
            maxI,maxV=-float('inf'), -float('inf')
            for i in range(start, end+1):
                if nums[i]>maxV:
                    maxI,maxV=i,nums[i]
            return TreeNode(maxV, recur(nums, start, maxI-1), recur(nums, maxI+1, end))

        if not nums:
            return None
        return recur(nums, 0, len(nums)-1)

import unittest

class TestSolution(unittest.TestCase):
    def testConstructMaximumBinaryTree(self):
        s = Solution()
        self.assertEqual(s.constructMaximumBinaryTree(nums = [3,2,1,6,0,5]), 
                         TreeNode(6,TreeNode(3,None,TreeNode(2,None(TreeNode(1)))), TreeNode(5,TreeNode(0))))


if __name__ == '__main__':
    unittest.main()