from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    # Same as # 865
    # DFS to find LCA and respective height (calculated bottom up), and always return LCA and larger height
    # If same height from left and right, return current node
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return (None, 0)
            lcaLeft, heightLeft = dfs(node.left)
            lcaRight, heightRight = dfs(node.right)
            if heightLeft == heightRight:
                return (node, heightLeft + 1)
            elif heightLeft > heightRight:
                return (lcaLeft, heightLeft + 1)
            else:
                return (lcaRight, heightRight + 1)

        if not root:
            return root
        lca, _ = dfs(root)
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