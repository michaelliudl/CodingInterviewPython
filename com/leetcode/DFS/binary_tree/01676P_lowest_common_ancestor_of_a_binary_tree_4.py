from typing import List

'''
Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

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

        if not root or not nodes:
            return root
        result = nodes[0]
        for i in range(1, len(nodes)):
            result = lca(root, result, nodes[i])
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()