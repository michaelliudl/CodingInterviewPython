from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def inorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        st=[]
        p=root
        while p or st:
            if p:
                st.append(p)
                p=p.left
            else:
                t=st.pop()
                r.append(t.val)
                p=t.right
        return r



    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        self.traverse(root,r)
        return r
    
    def traverse(self, root: TreeNode, r: List):
        if not root:
            return
        self.traverse(root.left,r)
        r.append(root.val)
        self.traverse(root.right,r)

import unittest

class TestSolution(unittest.TestCase):
    def testInorderTraversal(self):
        s = Solution()
        self.assertEqual(s.inorderTraversalIter(TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))), [1,3,2])
        self.assertEqual(s.inorderTraversalIter(None), [])
        self.assertEqual(s.inorderTraversalIter(TreeNode(1,None,None)), [1])


if __name__ == '__main__':
    unittest.main()