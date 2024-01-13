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

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.inv(root)
        return root

    def inv(self, root):
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.inv(root.left)
        self.inv(root.right)

    def invertTreeStack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        st=[root]
        while st:
            n=st.pop()
            if n.left:
                st.append(n.left)
            if n.right:
                st.append(n.right)
            n.left,n.right=n.right,n.left
        return root
    
    def invertTreeQueue(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q=Deque()
        q.append(root)
        while q:
            size=len(q)
            for _ in range(size):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                n.left,n.right=n.right,n.left
        return root

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