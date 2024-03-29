from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def recur(node):
            nonlocal ans
            if not node:
                return 0
            leftUpValue = max(recur(node.left), 0)          # Return 0 for subtree if result is negative
            rightUpValue = max(recur(node.right), 0)
            ans = max(ans, (node.val + leftUpValue + rightUpValue))
            return node.val + max(leftUpValue, rightUpValue)

        if not root:
            return -1
        ans = -float('inf')
        recur(root)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testPostorderTraversal(self):
        s = Solution()
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))), [3,2,1])
        self.assertEqual(s.postorderTraversalIter(None), [])
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,None)), [1])


if __name__ == '__main__':
    unittest.main()