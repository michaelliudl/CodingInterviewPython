from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # DFS and return null for a leaf with value matching target
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            return node
        
        return dfs(root)

import unittest

class TestSolution(unittest.TestCase):
    def testGetDirections(self):
        s = Solution()
        self.assertEqual(s.getDirections(root=TreeNode(5,None,TreeNode(3,TreeNode(4),TreeNode(7))), startValue = 4, destValue = 3), 'U')
        self.assertEqual(s.getDirections(root=TreeNode(5,TreeNode(1,TreeNode(3)),TreeNode(2,TreeNode(6),TreeNode(4))), startValue = 3, destValue = 6), 'UURL')
        self.assertEqual(s.getDirections(root=TreeNode(2,TreeNode(1)), startValue = 2, destValue = 1), 'L')
        self.assertEqual(s.getDirections(root=TreeNode(1,None,TreeNode(10,TreeNode(12,TreeNode(4),TreeNode(6)),TreeNode(13,None,TreeNode(15,None,TreeNode(2))))),
                                         startValue = 6, destValue = 15), 'UURR')


if __name__ == '__main__':
    unittest.main()