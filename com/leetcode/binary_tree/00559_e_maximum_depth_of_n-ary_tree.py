from typing import Optional,List,Deque

class Node:

    def __init__(self, val=0, children=None):
        self.val=val
        self.children=children
        

class Solution:

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        dep=0
        q=Deque()
        q.append(root)
        while q:
            dep+=1
            size=len(q)
            for _ in range(size):
                n=q.popleft()
                if n.children:
                    for c in n.children:
                        q.append(c)
        return dep

import unittest

class TestSolution(unittest.TestCase):
    def testMaxDepth(self):
        s = Solution()
        
        self.assertEqual(s.maxDepthQ(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 3)
        self.assertEqual(s.maxDepthQ(TreeNode(1,None,TreeNode(2))), 2)


if __name__ == '__main__':
    unittest.main()