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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot):
            return False
        return self.sub(root, subRoot, False)

    def sub(self, root, subRoot, found):
        if found:
            return True
        if not root:
            return False
        if root.val==subRoot.val:
            isSame=self.same(root,subRoot)
            if isSame:
                found=True
                return True
        return self.sub(root.left, subRoot, found) or self.sub(root.right, subRoot, found)
        
    def same(self, r1, r2):
        if not r1 and not r2:
            return True
        if (r1 and not r2) or (not r1 and r2):
            return False
        return r1.val==r2.val and self.same(r1.left,r2.left) and self.same(r1.right,r2.right)
    
import unittest

class TestSolution(unittest.TestCase):
    def testIsSubtree(self):
        s = Solution()
        self.assertEqual(s.isSubtree(
            root=TreeNode(3,TreeNode(4,TreeNode(1),TreeNode(2,TreeNode(0))),TreeNode(5)),
            subRoot=TreeNode(4,TreeNode(1),TreeNode(2))
        ), False)

if __name__ == '__main__':
    unittest.main()