from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # DFS and return distances to leaves in both left and right subtrees
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def dfs(node):
            nonlocal res
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            leftDists = dfs(node.left)
            rightDists = dfs(node.right)
            for ld in leftDists:
                for rd in rightDists:
                    if ld + rd <= distance:
                        res += 1
            return [dist + 1 for dist in (leftDists + rightDists)]

        res = 0
        dfs(root)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testDelNodes(self):
        s = Solution()
        self.assertEqual(s.delNodes(root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7))), 
                                    to_delete = [3,5]), 
                         [TreeNode(1,TreeNode(2,TreeNode(4))), TreeNode(6), TreeNode(7)])
        self.assertEqual(s.delNodes(root=TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4)),
                                    to_delete = [3]), 
                         [TreeNode(1,TreeNode(2),TreeNode(4))])


if __name__ == '__main__':
    unittest.main()