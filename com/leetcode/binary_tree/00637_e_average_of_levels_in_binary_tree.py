from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        r=[]
        q=Deque()
        q.append(root)
        while q:
            size=len(q)
            sum=0
            for _ in range(size):
                n=q.popleft()
                sum+=n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            r.append(sum/size)
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testAverageOfLevels(self):
        s = Solution()
        self.assertEqual(s.averageOfLevels(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), [3.00000,14.50000,11.00000])
        self.assertEqual(s.averageOfLevels(TreeNode(3,TreeNode(9,TreeNode(15),TreeNode(7)),TreeNode(20))), [3.00000,14.50000,11.00000])
        self.assertEqual(s.averageOfLevels(None), [])


if __name__ == '__main__':
    unittest.main()