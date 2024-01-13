from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.minD(root,1)

    def minD(self,root,d):
        if not root.left and not root.right:
            return d
        if not root.left:
            return self.minD(root.right, d+1)
        elif not root.right:
            return self.minD(root.left, d+1)
        else:
            return min(self.minD(root.left, d+1), self.minD(root.right, d+1))
        
    def minDepthQ(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d=0
        q=Deque()
        q.append(root)
        while q:
            d+=1
            size=len(q)
            for _ in range(size):
                n=q.popleft()
                if not n.left and not n.right:
                    return d
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return d


import unittest

class TestSolution(unittest.TestCase):
    def testMinDepth(self):
        s = Solution()
        
        self.assertEqual(s.minDepthQ(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 2)
        self.assertEqual(s.minDepthQ(TreeNode(2,None,TreeNode(3,None,TreeNode(4,None,TreeNode(5,None,(TreeNode(6))))))), 5)


if __name__ == '__main__':
    unittest.main()