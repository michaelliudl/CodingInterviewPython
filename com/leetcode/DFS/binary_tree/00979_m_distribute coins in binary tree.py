from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # DFS, return number of nodes and total count of coins for each subtree
    # Increase number of operations by absolute value of diff between number of nodes and count of coins
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal res
            if not node:
                return (0, 0)
            leftNodes, leftCoins = dfs(node.left)
            rightNodes, rightCoins = dfs(node.right)
            res += (abs(leftNodes - leftCoins) + abs(rightNodes - rightCoins))
            return (1 + leftNodes + rightNodes, node.val + leftCoins + rightCoins)

        res = 0
        dfs(root)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testInvertTree(self):
        s = Solution()
        root=TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))
        s.invertTree(root)
        self.assertEqual(root, TreeNode(4,TreeNode(7,TreeNode(9),TreeNode(6)),TreeNode(2,TreeNode(3),TreeNode(1))))

        root=TreeNode(2,TreeNode(1),TreeNode(3))
        s.invertTree(root)
        self.assertEqual(root, TreeNode(2,TreeNode(3,TreeNode(1))))

if __name__ == '__main__':
    unittest.main()