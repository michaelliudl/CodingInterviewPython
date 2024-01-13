from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not root or not p or not q:
            return None
        pl,ql=list(),list()
        self.findPath(root,p,pl),self.findPath(root,q,ql)
        

    def findPath(self, root: 'TreeNode', t: 'TreeNode', r: List) -> None:
        if root.val==t.val:
            r.append(root)
            return
        r.append(root)
        self.findPath(root.left,t,r)


import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()