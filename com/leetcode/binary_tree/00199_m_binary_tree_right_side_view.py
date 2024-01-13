from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        q=Deque()
        q.append(root)
        while q:
            r.append(q[-1].val)
            size=len(q)
            for _ in range(size):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testRightSideView(self):
        s = Solution()
        self.assertEqual(s.rightSideView(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))), [1,3,4])
        self.assertEqual(s.rightSideView(TreeNode(1,None,TreeNode(3,))), [1,3])
        self.assertEqual(s.rightSideView(None), [])


if __name__ == '__main__':
    unittest.main()