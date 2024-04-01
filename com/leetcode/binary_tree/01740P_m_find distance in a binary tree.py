from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

'''
Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.
'''

class Solution:

    # Find LCA first, then find depths of all three. distance = depth of p + depth of q - 2 * (depth of LCAs)
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        def lca(node, p, q):
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            lcaLeft = lca(node.left, p, q)
            lcaRight = lca(node.right, p, q)
            if lcaLeft and lcaRight:
                return node
            elif lcaLeft:
                return lcaLeft
            else:
                return lcaRight
        
        def getDepth(node, target, depth):
            if not node:
                return -1
            if node.val == target:
                return depth
            leftDepth = getDepth(node.left, target, depth + 1)
            if leftDepth > 0:
                return leftDepth
            return getDepth(node.right, target, depth + 1)

        if not root or p == q:
            return 0
        lcaNode = lca(root, p, q)
        lcaDepth = getDepth(root, lcaNode.val, depth = 0)
        pDepth = getDepth(root, p, depth = 0)
        qDepth = getDepth(root, q, depth = 0)
        result = pDepth + qDepth - 2 * lcaDepth
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testRightSideView(self):
        s = Solution()
        self.assertEqual(s.rightSideView(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))), [1,3,4])
        self.assertEqual(s.rightSideView(TreeNode(1,None,TreeNode(3,))), [1,3])
        self.assertEqual(s.rightSideView(None), [])


if __name__ == '__main__':
    unittest.main()