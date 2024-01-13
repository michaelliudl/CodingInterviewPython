from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val+=root2.val
        root1.left=self.mergeTrees(root1.left, root2.left)
        root1.right=self.mergeTrees(root1.right, root2.right)
        return root1

    def mergeTreesLevelOrder(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        q=Deque()
        q.append(root1)
        q.append(root2)
        while q:
            n1,n2=q.popleft(),q.popleft()
            n1.val+=n2.val
            if n1.left and n2.left:
                q.append(n1.left)
                q.append(n2.left)
            if n1.right and n2.right:
                q.append(n1.right)
                q.append(n2.right)
            if not n1.left and n2.left:
                n1.left=n2.left
            if not n1.right and n2.right:
                n1.right=n2.right
        return root1


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