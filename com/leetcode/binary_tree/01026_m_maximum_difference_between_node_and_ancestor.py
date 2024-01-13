from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def __eq__(self, __value: object) -> bool:
        return (isinstance(object,TreeNode) and self.val==object.val 
                and (self.left==object.left if self.left or object.left else True)
                and (self.right==object.right if self.right or object.right else True))

class Solution:

    def maxAncestorDiffDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, minV, maxV) -> int:
            if not node:
                return maxV-minV
            minV=min(minV,node.val)
            maxV=max(maxV,node.val)
            maxDiffLeft=dfs(node.left,minV,maxV)
            maxDiffRight=dfs(node.right,minV,maxV)
            return max(maxDiffLeft,maxDiffRight)
        
        return dfs(root, root.val, root.val)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.preOrder(root, [])
    
    def preOrder(self, node: TreeNode, st: list) -> int:
        if not node.left and not node.right:
            st.append(node.val)
            if len(st)==1:
                return st[0]
            maxDiff=max(st)-min(st)
            st.pop()
            return maxDiff
        st.append(node.val)
        maxLeft,maxRight=0,0
        if node.left:
            maxLeft=self.preOrder(node.left, st)
        if node.right:
            maxRight=self.preOrder(node.right, st)
        st.pop()
        return max(maxLeft, maxRight)
    
import unittest

class TestSolution(unittest.TestCase):
    def testMaxAncestorDiff(self):
        s = Solution()
        self.assertEqual(s.maxAncestorDiffDFS(TreeNode(8,TreeNode(3,TreeNode(1),TreeNode(6,TreeNode(4),TreeNode(7))),TreeNode(10,None,TreeNode(14,TreeNode(13))))), 7)
        self.assertEqual(s.maxAncestorDiffDFS(TreeNode(1,None,TreeNode(2,None,TreeNode(0,TreeNode(3))))), 3)

if __name__ == '__main__':
    unittest.main()