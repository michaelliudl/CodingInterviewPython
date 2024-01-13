from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r=[]
        q=Deque()
        q.append(root)
        while q:
            size=len(q)
            large=-float('inf')
            for _ in range(size):
                n=q.popleft()
                if n.val>large:
                    large=n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            r.append(large)
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testLargestValues(self):
        s = Solution()
        self.assertEqual(s.largestValues(TreeNode(1,TreeNode(3,TreeNode(5),TreeNode(3)),TreeNode(2,None,TreeNode(9)))), [1,3,9])
        self.assertEqual(s.largestValues(TreeNode(1,TreeNode(2),TreeNode(3))), [1,3])
        self.assertEqual(s.largestValues(None), [])


if __name__ == '__main__':
    unittest.main()