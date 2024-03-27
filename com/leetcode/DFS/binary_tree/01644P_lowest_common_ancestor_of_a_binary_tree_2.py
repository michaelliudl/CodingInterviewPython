from typing import List

'''
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Find LCA by usual, if LCA is `p` or `q`, try to find the other one in its subtree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(node, p, q):
            if not node or node == p or node == q:
                return node
            lcaLeft = lca(node.left, p, q)
            lcaRight = lca(node.right, p, q)
            if lcaLeft and lcaRight:
                return node
            elif lcaLeft:
                return lcaLeft
            else:
                return lcaRight
        
        def find(node, target):
            if not node or node == target:
                return node
            resultLeft = find(node.left, target)
            if resultLeft:
                return resultLeft
            return find(node.right, target)

        if not root or not p or not q:
            return None
        candidate = lca(root, p, q)
        if candidate == p:
            result = find(p, q)
            return candidate if result == q else None
        elif candidate == q:
            result = find(q, p)
            return candidate if result == p else None
        return candidate


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()