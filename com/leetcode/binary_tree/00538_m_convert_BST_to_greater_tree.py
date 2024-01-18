from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def convert(node, prev) -> TreeNode:
            if not node:
                return prev
            prev=convert(node.right, prev)
            node.val+=prev.val if prev else 0
            prev=node
            prev=convert(node.left, prev)
            return prev

        if not root:
            return None
        convert(root, prev=None)
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