from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node: TreeNode, prev: TreeNode, diff: int) -> (TreeNode, int):
            if not node:
                return (prev, diff)
            (prev, diff)=inorder(node.left, prev, diff)
            if prev and (node.val-prev.val)<diff:
                diff=node.val-prev.val
            prev=node
            (prev, diff)=inorder(node.right, prev, diff)
            return (prev, diff)
        
        if not root or (not root.left and not root.right):
            return 0
        (_, minD)=inorder(root, prev=None, diff=float('inf'))
        return minD





import unittest

class TestSolution(unittest.TestCase):
    def testBinaryTreePaths(self):
        s = Solution()
        
        self.assertEqual(s.binaryTreePaths(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))), ["1->2->5","1->3"])
        self.assertEqual(s.binaryTreePaths(TreeNode(1)), ["1"])

        self.assertEqual(s.binaryTreePathsRecurString(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))), ["1->2->5","1->3"])
        self.assertEqual(s.binaryTreePathsRecurString(TreeNode(1)), ["1"])

        self.assertEqual(s.binaryTreePathsStack(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))), ["1->2->5","1->3"])
        self.assertEqual(s.binaryTreePathsStack(TreeNode(1)), ["1"])


if __name__ == '__main__':
    unittest.main()