from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum):
            if not root.left and not root.right:
                return root.val==targetSum
            fl=dfs(root.left, targetSum-root.val) if root.left else False
            if fl:
                return True
            fr=dfs(root.right, targetSum-root.val) if root.right else False
            if fr:
                return True
            return False

        if not root:
            return False
        return dfs(root, targetSum)
    
    def hasPathSumStack(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        st=[]
        st.append((root,targetSum))
        while st:
            (node,target)=st.pop()
            if not node.left and not node.right:
                if target==node.val:
                    return True
            if node.left:
                st.append((node.left, target-node.val))
            if node.right:
                st.append((node.right, target-node.val))
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testAverageOfLevels(self):
        s = Solution()
        self.assertEqual(s.averageOfLevels(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), [3.00000,14.50000,11.00000])
        self.assertEqual(s.averageOfLevels(TreeNode(3,TreeNode(9,TreeNode(15),TreeNode(7)),TreeNode(20))), [3.00000,14.50000,11.00000])
        self.assertEqual(s.averageOfLevels(None), [])


if __name__ == '__main__':
    unittest.main()