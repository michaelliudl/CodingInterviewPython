from typing import Optional,List,Deque

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    '''
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.
    '''

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        def inorder(node):
            if not node:
                return None
            if node.val <= p.val:
                return inorder(node.right)
            else:
                return inorder(node.left) or node
        
        if not root or not p:
            return None
        return inorder(root)

import unittest

class TestSolution(unittest.TestCase):
    def testIsValidBST(self):
        s = Solution()
                
        self.assertEqual(s.isValidBST(TreeNode(1,TreeNode(1))), False)


if __name__ == '__main__':
    unittest.main()