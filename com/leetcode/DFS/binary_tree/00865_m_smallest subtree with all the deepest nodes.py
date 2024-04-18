from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Postorder traversal to find LCA and respective depth, and always return deepest LCA
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def postorder(node):
            if not node:
                return (None, 0)
            lcaLeft, depLeft = postorder(node.left)
            lcaRight, depRight = postorder(node.right)
            if depLeft > depRight:
                return (lcaLeft, depLeft + 1)
            elif depLeft < depRight:
                return (lcaRight, depRight + 1)
            else:
                return (node, depLeft + 1)
        
        if not root:
            return root
        lca, _ = postorder(root)
        return lca

import unittest

class TestSolution(unittest.TestCase):
    def testRightSideView(self):
        s = Solution()
        self.assertEqual(s.rightSideView(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))), [1,3,4])
        self.assertEqual(s.rightSideView(TreeNode(1,None,TreeNode(3,))), [1,3])
        self.assertEqual(s.rightSideView(None), [])


if __name__ == '__main__':
    unittest.main()