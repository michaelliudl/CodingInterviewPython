from typing import Optional,List,Deque
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        queue = Deque()
        queue.append(root)
        while queue:
            size = len(queue)
            large = -math.inf
            for _ in range(size):
                node = queue.popleft()
                large = max(large, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(large)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testLargestValues(self):
        s = Solution()
        self.assertEqual(s.largestValues(TreeNode(1,TreeNode(3,TreeNode(5),TreeNode(3)),TreeNode(2,None,TreeNode(9)))), [1,3,9])
        self.assertEqual(s.largestValues(TreeNode(1,TreeNode(2),TreeNode(3))), [1,3])
        self.assertEqual(s.largestValues(None), [])


if __name__ == '__main__':
    unittest.main()