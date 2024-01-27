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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.sym(root.left, root.right)

    def sym(self, left, right):
        if not left and not right:
            return True
        if left and right:
            return left.val==right.val and self.sym(left.left, right.right) and self.sym(left.right, right.left)
        return False

    def isSymmetricQueue(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q=Deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            if len(q) < 2 or len(q)%2==1:
                return False
            l,r=q.popleft(),q.popleft()
            if not l and not r:
                continue
            if not l or not r or l.val!=r.val:
                return False
            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)
        return True
    
    def isSymmetricStack(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        st=[]
        st.append(root.left)
        st.append(root.right)
        while st:
            r,l=st.pop(),st.pop()
            if not l and not r:
                continue
            if not l or not r or l.val!=r.val:
                return False
            st.append(l.left)
            st.append(r.right)
            st.append(l.right)
            st.append(r.left)
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testInvertTree(self):
        s = Solution()
        root=TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))
        s.invertTree(root)
        self.assertEqual(root, TreeNode(4,TreeNode(7,TreeNode(9),TreeNode(6)),TreeNode(2,TreeNode(3),TreeNode(1))))

        root=TreeNode(2,TreeNode(1),TreeNode(3))
        s.invertTree(root)
        self.assertEqual(root, TreeNode(2,TreeNode(3,TreeNode(1))))

if __name__ == '__main__':
    unittest.main()