from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def isValidBSTIter(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        prev,cur=None,root
        st=[]
        while cur or st:
            if cur:
                st.append(cur)
                cur=cur.left
            else:
                cur=st.pop()
                if prev and prev.val>=cur.val:
                    return False
                prev=cur
                cur=cur.right
        return True



    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node: TreeNode, pre: TreeNode) -> (bool, TreeNode):
            if not node:
                return (True, pre)
            (validLeft, pre)=inorder(node.left, pre)
            if pre and pre.val>=node.val:
                return (False, pre)
            pre=node
            (validRight, pre)=inorder(node.right, pre)
            return (validLeft and validRight, pre)

        if not root:
            return True
        (valid, _) = inorder(root, pre=None)
        return valid
        
        
    def isValidBSTUseList(self, root: Optional[TreeNode]) -> bool:
        def inorder(node: TreeNode, r: list):
            if not node:
                return
            inorder(node.left, r)
            r.append(node.val)
            inorder(node.right, r)

        if not root:
            return False
        r=[]
        inorder(root, r)
        for i in range(len(r)-1):
            if r[i]>=r[i+1]:
                return False
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testIsValidBST(self):
        s = Solution()
                
        self.assertEqual(s.isValidBST(TreeNode(1,TreeNode(1))), False)


if __name__ == '__main__':
    unittest.main()