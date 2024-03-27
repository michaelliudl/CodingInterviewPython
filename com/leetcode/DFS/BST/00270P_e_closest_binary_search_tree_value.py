from typing import Optional,List,Deque

'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.
'''

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return 0
        node = root
        result = -1
        diff = float('inf')
        while node:
            if target == node.val:
                return node.val
            curDiff = abs(node.val - target)
            if curDiff < diff or (curDiff == diff and node.val < result):
                result = node.val
                diff = abs(node.val - target)
            if target < node.val:
                node = node.left
            else:
                node = node.right
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testClosestValue(self):
        s = Solution()
        
        self.assertEqual(s.closestValue(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(5)), target = 3.714286), 4)
        self.assertEqual(s.closestValue(TreeNode(1), target = 4.428571), 1)
        self.assertEqual(s.closestValue(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(5)), target = 3.5), 3)
        self.assertEqual(s.closestValue(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(5)), target = 4.5), 4)


if __name__ == '__main__':
    unittest.main()