from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def preorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        st=[]
        p=root
        while p or st:
            if p:
                r.append(p.val)
                st.append(p)
                p=p.left
            else:
                p=st.pop().right
        return r



    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        self.traverse(root,r)
        return r
    
    def traverse(self, root: TreeNode, r: List):
        if not root:
            return
        r.append(root.val)
        self.traverse(root.left,r)
        self.traverse(root.right,r)

import unittest

class TestSolution(unittest.TestCase):
    def testPreorderTraversal(self):
        s = Solution()
        self.assertEqual(s.preorderTraversalIter(TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))), [1,2,3])
        self.assertEqual(s.preorderTraversalIter(None), [])
        self.assertEqual(s.preorderTraversalIter(TreeNode(1,None,None)), [1])


if __name__ == '__main__':
    unittest.main()