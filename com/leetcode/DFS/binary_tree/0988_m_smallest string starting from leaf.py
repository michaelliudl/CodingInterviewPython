from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(node, path):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right:
                path.append(node.val)
                if not res or list(reversed(path)) < res:
                    res = list(reversed(path))
                path.pop()
                return
            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        if not root:
            return ''
        res = []
        dfs(root, path = [])
        return ''.join(chr(elem + ord('a')) for elem in res)

import unittest

class TestSolution(unittest.TestCase):
    def testDelNodes(self):
        s = Solution()
        # self.assertEqual(s.delNodes(root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7))), 
        #                             to_delete = [3,5]), 
        #                  [TreeNode(1,TreeNode(2,TreeNode(4))), TreeNode(6), TreeNode(7)])
        self.assertEqual(s.delNodes(root=TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4)),
                                    to_delete = [3]), 
                         [TreeNode(1,TreeNode(2),TreeNode(4))])


if __name__ == '__main__':
    unittest.main()