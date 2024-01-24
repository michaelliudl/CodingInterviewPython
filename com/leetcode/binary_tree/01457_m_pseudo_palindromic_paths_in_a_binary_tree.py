from typing import List,Optional

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def pPalin():
            odd=False
            for _,c in d.items():
                if c%2==1:
                    if odd:
                        return False
                    odd=True
            return True

        def recur(node):
            nonlocal r

            if node.val in d:
                d[node.val]+=1
            else:
                d[node.val]=1

            if not node.left and not node.right:
                if pPalin():
                    r+=1
            
            if node.left:
                recur(node.left)
            if node.right:
                recur(node.right)

            if node.val in d:
                d[node.val]-=1
                if d[node.val]==0:
                    del d[node.val]

        if not root:
            return 0
        d,r={},0
        recur(root)
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testPseudoPalindromicPaths(self):
        s = Solution()
        self.assertEqual(s.pseudoPalindromicPaths(TreeNode(2,TreeNode(3,TreeNode(3),TreeNode(1)),TreeNode(1,None,TreeNode(1)))), 2)
        self.assertEqual(s.pseudoPalindromicPaths(TreeNode(2,TreeNode(1,TreeNode(1),TreeNode(3,None,TreeNode(1))),TreeNode(1))), 1)
        


if __name__ == '__main__':
    unittest.main()