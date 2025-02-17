from typing import Optional
from typing import List
from typing import Deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # DFS recursion and swap values on odd levels 
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(left, right, isOdd):
            if not left:
                return
            if isOdd:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, not isOdd)
            dfs(left.right, right.left, not isOdd)
        
        dfs(root.left, root.right, True)
        return root
    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()