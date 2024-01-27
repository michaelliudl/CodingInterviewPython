from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    ''' Down from root, first node with value in [p.v,q.v] is LCA in BST '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, minV, maxV):
            if not node:
                return node
            if node.val>=minV and node.val <=maxV:
                return node
            lcaLeft=lca(node.left, minV, maxV)
            if lcaLeft:
                return lcaLeft
            return lca(node.right, minV, maxV)

        if not root or not p or not q:
            return None
        return lca(root, p.val if p.val<q.val else q.val, p.val if p.val>q.val else q.val)

    def lowestCommonAncestorIter(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        minV=p.val if p.val<q.val else q.val
        maxV=p.val if p.val>q.val else q.val
        st=[root]
        while st:
            node=st.pop()
            if node.val>=minV and node.val<=maxV:
                return node
            if node.val>maxV and node.left:
                st.append(node.left)
            if node.val<minV and node.right:
                st.append(node.right)
        return None


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()