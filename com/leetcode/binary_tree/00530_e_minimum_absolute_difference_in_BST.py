from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        prev,cur=None,root
        st=[]
        minD=float('inf')
        while cur or st:
            if cur:
                st.append(cur)
                cur=cur.left
            else:
                cur=st.pop()
                if prev and (cur.val-prev.val < minD):
                    minD=cur.val-prev.val
                prev=cur
                cur=cur.right
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