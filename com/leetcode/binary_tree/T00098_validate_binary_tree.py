from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return (self.isValid(root.left, rv=root.val, lessThan=True) 
                and self.isValid(root.right, rv=root.val, lessThan=False))
        
    def isValid(self, node:TreeNode, rv: int, lessThan: bool) -> bool:
        if not node:
            return True
        return (node.val<rv if lessThan else node.val>rv
                and self.isValid(node.left, rv=node.val, lessThan=True) 
                and self.isValid(node.right, rv=node.val, lessThan=False))

import unittest

class TestSolution(unittest.TestCase):
    def testIsValidBST(self):
        s = Solution()
        self.assertEqual(s.isValidBST(TreeNode(2,TreeNode(1,None,None),TreeNode(3,None,None))), True)
        self.assertEqual(s.isValidBST(TreeNode(5,TreeNode(1,None,None),TreeNode(4,TreeNode(3,None,None),TreeNode(6,None,None)))), False)


if __name__ == '__main__':
    unittest.main()