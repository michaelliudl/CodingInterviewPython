from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def postorder(node):
            nonlocal r
            if not node: return 0
            lDepth=postorder(node.left)
            rDepth=postorder(node.right)
            curDiameter=lDepth+rDepth
            r=max(r,curDiameter)
            return max(lDepth,rDepth)+1

        if not root:
            return -1
        r=0
        postorder(root)
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testDiameterOfBinaryTree(self):
        s = Solution()
        self.assertEqual(s.diameterOfBinaryTree(TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))), 3)
        self.assertEqual(s.diameterOfBinaryTree(TreeNode(1,TreeNode(2),None)), 1)
        self.assertEqual(s.diameterOfBinaryTree(TreeNode(2,TreeNode(5,TreeNode(3,TreeNode(1),TreeNode(4))),None)), 3)


if __name__ == '__main__':
    unittest.main()