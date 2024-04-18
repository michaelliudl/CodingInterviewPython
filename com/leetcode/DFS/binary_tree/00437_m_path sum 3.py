from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Apply 113 Path Sum II logic to every node
    def pathSum1(self, root: TreeNode, targetSum: int) -> int:

        # DFS from each node as root and change target value on each recursion
        def dfs(node, target):
            nonlocal ret
            if not node:
                return
            if node.val == target:
                ret += 1
            dfs(node.left, target - node.val)
            dfs(node.right ,target - node.val)

        # `outerDfs` uses original `targetSum` on every node
        def outerDfs(node, targetSum):
            if not node:
                return
            dfs(node, targetSum)
            outerDfs(node.left, targetSum)
            outerDfs(node.right, targetSum)

        if not root:
            return 0
        ret = 0
        outerDfs(root, targetSum)
        return ret

    # Use return value on recusion
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        def dfs(root: TreeNode, target: int) -> int:
            if not root:
                return 0
            return (target == root.val) + \
                dfs(root.left, target - root.val) + \
                dfs(root.right, target - root.val)

        return dfs(root, targetSum) + \
            self.pathSum(root.left, targetSum) + \
            self.pathSum(root.right, targetSum)


import unittest

class TestSolution(unittest.TestCase):
    def testPathSum(self):
        s = Solution()
        self.assertEqual(s.pathSumStack(TreeNode(1,TreeNode(2)), 0), [])
        # self.assertEqual(s.pathSum(TreeNode(3,TreeNode(9,TreeNode(15),TreeNode(7)),TreeNode(20))), [3.00000,14.50000,11.00000])
        self.assertEqual(s.pathSumStack(None), [])


if __name__ == '__main__':
    unittest.main()