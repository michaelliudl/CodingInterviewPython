from typing import Optional,List,Deque


"""
Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if not node:
            return node
        # Case 1, node has right child, find right child's most left child
        if node.right:
            child = node.right
            while child and child.left:
                child = child.left
            return child
        parent = node.parent
        if parent:
            # Case 2, node is left child of parent
            if node == parent.left:
                return parent
            else:
                # Case 3, node is right child of parent, keep going up until one parent is left child of its parent
                pp = node
                while pp.parent and pp == pp.parent.right:
                    pp = pp.parent
                return pp.parent

import unittest

class TestSolution(unittest.TestCase):
    def testInorderSuccessor(self):
        s = Solution()
        self.assertEqual(s.inorderSuccessor(TreeNode(1,TreeNode(1))), False)


if __name__ == '__main__':
    unittest.main()