from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Optimal
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, path):
            nonlocal result
            if not node:
                return
            if not node.left and not node.right:
                result += path * 10 + node.val
                return
            dfs(node.left, path * 10 + node.val)
            dfs(node.right, path * 10 + node.val)

        if not root:
            return 0
        result = 0
        dfs(root, path = 0)
        return result

    def sumNumbers1(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal r
            if not node.left and not node.right:
                path.append(node.val)
                multiplier=1
                for i in range(len(path)-1,-1,-1):
                    r+=path[i]*multiplier
                    multiplier*=10
                path.pop()
                return
            path.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            path.pop()

        if not root: return 0
        r,path=0,[]
        dfs(root)
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testSumNumbers(self):
        s = Solution()
        self.assertEqual(s.sumNumbers(TreeNode(1,TreeNode(2),TreeNode(3))), 25)
        self.assertEqual(s.sumNumbers(TreeNode(4,TreeNode(9,TreeNode(5),TreeNode(1)),TreeNode(0))), 1026)


if __name__ == '__main__':
    unittest.main()