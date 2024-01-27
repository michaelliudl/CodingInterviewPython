from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        n=root
        while n:
            if val==n.val:
                return n
            elif val<n.val:
                n=n.left
            elif val>n.val:
                n=n.right
        return None

import unittest

class TestSolution(unittest.TestCase):
    def testIsValidBST(self):
        s = Solution()
                
        self.assertEqual(s.isValidBST(TreeNode(1,TreeNode(1))), False)


if __name__ == '__main__':
    unittest.main()