from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def __eq__(self, __value: object) -> bool:
        return (isinstance(object,TreeNode) and self.val==object.val 
                and (self.left==object.left if self.left or object.left else True)
                and (self.right==object.right if self.right or object.right else True))

class Solution:

    ''' iterate all O(n), omitted '''

    ''' Check left/right height for full tree count 2**(k-1)-1, O(log(n)*log(n)) or O(k**2) '''
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh,rh=0,0
        lp,rp=root,root
        while lp or rp:
            if lp:
                lh+=1
                lp=lp.left
            if rp:
                rh+=1
                rp=rp.right
        if lh==rh:
            return 2**lh-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
import unittest

class TestSolution(unittest.TestCase):
    def testInvertTree(self):
        s = Solution()
        self.assertEqual(s.countNodes(TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6)))), 6)
        self.assertEqual(s.countNodes(TreeNode(1)), 1)
        self.assertEqual(s.countNodes(None), 0)

if __name__ == '__main__':
    unittest.main()