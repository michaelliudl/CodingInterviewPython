from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return -1
        

import unittest

class TestSolution(unittest.TestCase):
    def testPostorderTraversal(self):
        s = Solution()
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))), [3,2,1])
        self.assertEqual(s.postorderTraversalIter(None), [])
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,None)), [1])


if __name__ == '__main__':
    unittest.main()