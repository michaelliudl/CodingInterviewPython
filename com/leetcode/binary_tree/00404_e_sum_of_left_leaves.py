from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, sum, isLeft) -> int:
            if not node.left and not node.right:
                if isLeft:
                    sum+=node.val
                return sum
            leftSum,rightSum=0,0
            if node.left:
                leftSum=dfs(node.left, sum, isLeft=True)
            if node.right:
                rightSum=dfs(node.right, sum, isLeft=False)
            return leftSum+rightSum

        if not root:
            return 0
        return dfs(root, sum=0, isLeft=False)

    def sumOfLeftLeavesStack(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sum=0
        st=[]
        st.append((root, False))
        while st:
            node,isLeft=st.pop()
            if not node.left and not node.right:
                if isLeft:
                    sum+=node.val
            if node.left:
                st.append((node.left, True))
            if node.right:
                st.append((node.right, False))
        return sum

import unittest

class TestSolution(unittest.TestCase):
    def testSumOfLeftLeaves(self):
        s = Solution()
        
        self.assertEqual(s.sumOfLeftLeaves(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 24)
        self.assertEqual(s.sumOfLeftLeaves(TreeNode(1)), 0)

        self.assertEqual(s.sumOfLeftLeavesStack(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 24)
        self.assertEqual(s.sumOfLeftLeavesStack(TreeNode(1)), 0)

if __name__ == '__main__':
    unittest.main()