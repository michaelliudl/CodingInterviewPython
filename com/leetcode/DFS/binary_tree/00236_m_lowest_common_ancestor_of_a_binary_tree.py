from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(node, p, q):
            if not node or node == p or node == q:
                return node
            lcaLeft = lca(node.left, p, q)
            lcaRight = lca(node.right, p, q)
            if lcaLeft and lcaRight:
                return node
            elif lcaLeft:
                return lcaLeft
            else:
                return lcaRight

        if not root or not p or not q:
            return None
        return lca(root, p, q)
    
    
    def lowestCommonAncestorStack(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        st,pPath,qPath,visited=[root],[],[],[]
        while st:
            node=st[-1]
            if not pPath and node.val==p.val:
                pPath=st[:]
            if not qPath and node.val==q.val:
                qPath=st[:]
            if pPath and qPath:
                break
            visited.append(node)
            if node.left and not node.left in visited:
                st.append(node.left)
            elif node.right and not node.right in visited:
                st.append(node.right)
            else:
                st.pop()
        i,j,same=0,0,None
        while i<len(pPath) and j<len(qPath):
            if pPath[i].val==qPath[j].val:
                same=pPath[i]
                i+=1
                j+=1
            else:
                break
        return same




import unittest

class TestSolution(unittest.TestCase):

    def testLowestCommonAncestor(self):
        s = Solution()
        root=TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8)))
        self.assertEqual(s.lowestCommonAncestor(root, TreeNode(3), TreeNode(5)).val, 3)
        self.assertEqual(s.lowestCommonAncestor(root, TreeNode(6), TreeNode(2)).val, 5)
        self.assertEqual(s.lowestCommonAncestor(root, TreeNode(4), TreeNode(7)).val, 2)
        self.assertEqual(s.lowestCommonAncestor(root, TreeNode(6), TreeNode(0)).val, 3)
        self.assertEqual(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(1)).val, 3)


if __name__ == '__main__':
    unittest.main()