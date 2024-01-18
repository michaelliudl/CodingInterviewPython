from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        prev,cur=None,root
        st=[]
        while cur or st:
            if cur:
                st.append(cur)
                cur=cur.right
            else:
                cur=st.pop()
                cur.val+=prev.val if prev else 0
                prev=cur
                cur=cur.left
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