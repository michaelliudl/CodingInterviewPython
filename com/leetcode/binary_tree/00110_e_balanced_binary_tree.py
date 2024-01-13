from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def isBalancedHeightDiff(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            lh=dfs(node.left)
            if lh<0:
                return -1
            rh=dfs(node.right)
            if rh<0:
                return -1
            return -1 if abs(lh-rh)>1 else max(lh,rh)+1

        if not root:
            return True
        return dfs(root)>-1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode, h: int) -> (bool,int):
            if not node.left and not node.right:
                return (True,h)
            rl=dfs(node.left, h+1) if node.left else (True,h)
            rr=dfs(node.right, h+1) if node.right else (True,h)
            return ((rl[0] and rr[0] and abs(rl[1]-rr[1])<=1), max(rl[1],rr[1]))

        if not root:
            return True
        r=dfs(root, 1)
        return r[0]


import unittest

class TestSolution(unittest.TestCase):
    def testIsBalanced(self):
        s = Solution()
        
        self.assertEqual(s.isBalanced(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), True)
        self.assertEqual(s.isBalanced(TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))), False)
        self.assertEqual(s.isBalanced(None), True)


if __name__ == '__main__':
    unittest.main()