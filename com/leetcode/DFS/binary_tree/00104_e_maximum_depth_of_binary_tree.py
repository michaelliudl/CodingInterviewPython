from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.maxD(root,1,0)

    def maxD(self,root,d,md):
        if not root:
            return md
        if d>md:
            md=d
        return max(self.maxD(root.left, d+1, md), self.maxD(root.right, d+1, md))
        
    def maxDepthQ(self, root: Optional[TreeNode]) -> int:
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
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return d

import unittest

class TestSolution(unittest.TestCase):
    def testMaxDepth(self):
        s = Solution()
        
        self.assertEqual(s.maxDepthQ(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 3)
        self.assertEqual(s.maxDepthQ(TreeNode(1,None,TreeNode(2))), 2)


if __name__ == '__main__':
    unittest.main()