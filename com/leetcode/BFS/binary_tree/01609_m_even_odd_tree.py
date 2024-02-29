from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        level = 0
        queue = Deque()
        queue.append(root)
        while queue:
            curLen = len(queue)
            prevVal = None
            for _ in range(curLen):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or (prevVal and node.val <= prevVal):
                        return False
                else:
                    if node.val % 2 == 1 or (prevVal and node.val >= prevVal):
                        return False
                prevVal = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True


    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()