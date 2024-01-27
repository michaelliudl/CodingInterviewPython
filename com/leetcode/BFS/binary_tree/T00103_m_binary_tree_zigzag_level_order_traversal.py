from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()