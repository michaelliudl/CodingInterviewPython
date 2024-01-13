from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        r=[]
        q=Deque()
        q.append(root)
        while q:
            size=len(q)
            r1=[]
            for _ in range(size):
                n=q.popleft()
                r1.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            r.append(r1)
        return list(reversed(r))

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrderBottom(self):
        s = Solution()
        self.assertEqual(s.levelOrderBottom(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), [[15,7],[9,20],[3]])
        self.assertEqual(s.levelOrderBottom(None), [])
        self.assertEqual(s.levelOrderBottom(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()