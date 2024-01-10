from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def postorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        st=[]
        p=root
        lastVisited=None
        while p or st:
            if p:
                st.append(p)
                p=p.left
            elif st[-1].right and st[-1].right!=lastVisited:
                p=st[-1].right
            else:
                lastVisited=st.pop()
                r.append(lastVisited.val)
        return r
            



    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        self.traverse(root,r)
        return r
    
    def traverse(self, root: TreeNode, r: List):
        if not root:
            return
        self.traverse(root.left,r)
        self.traverse(root.right,r)
        r.append(root.val)

import unittest

class TestSolution(unittest.TestCase):
    def testPostorderTraversal(self):
        s = Solution()
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))), [3,2,1])
        self.assertEqual(s.postorderTraversalIter(None), [])
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,None)), [1])


if __name__ == '__main__':
    unittest.main()