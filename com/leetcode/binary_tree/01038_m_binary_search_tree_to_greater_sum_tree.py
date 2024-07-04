from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    # Use stack to track right children
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        prev, cur = None, root
        stack = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += prev.val if prev else 0
                prev = cur
                cur = cur.left
        return root
    
    # Recursion
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def recur(node):
            nonlocal prev
            if not node:
                return
            recur(node.right)
            node.val += prev
            prev = node.val
            recur(node.left)

        prev = 0
        recur(root)
        return root

import unittest

class TestSolution(unittest.TestCase):
    def testIsBalanced(self):
        s = Solution()
        
        self.assertEqual(s.isBalanced(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), True)
        self.assertEqual(s.isBalanced(TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))), False)
        self.assertEqual(s.isBalanced(None), True)


if __name__ == '__main__':
    unittest.main()