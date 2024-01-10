from typing import List,Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False
        leaf1,leaf2=[],[]
        self.travLeaf(root1,leaf1)
        self.travLeaf(root2,leaf2)
        return leaf1==leaf2
        
    def travLeaf(self, node, leaves):
        if not node.left and not node.right:
            leaves.append(node.val)
        if node.left:
            self.travLeaf(node.left,leaves)
        if node.right:
            self.travLeaf(node.right,leaves)
        

import unittest

class TestSolution(unittest.TestCase):
    def testLeafSimilar(self):
        s = Solution()
        self.assertEqual(s.leafSimilar(
            TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(9),TreeNode(8))),
            TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(7)),TreeNode(1,TreeNode(4),TreeNode(2,TreeNode(9),TreeNode(8))))
        ), True)
        self.assertEqual(s.leafSimilar(
            TreeNode(1,TreeNode(2),TreeNode(3)),
            TreeNode(1,TreeNode(3),TreeNode(2))
        ), False)


if __name__ == '__main__':
    unittest.main()