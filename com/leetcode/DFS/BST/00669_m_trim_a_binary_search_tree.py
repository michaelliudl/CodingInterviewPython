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

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node, low, high) -> TreeNode:
            if not node:
                return None
            if node.val>high:
                return trim(node.left, low, high)
            if node.val<low:
                return trim(node.right, low, high)
            node.left=trim(node.left, low, high)
            node.right=trim(node.right, low, high)
            return node

        if not root:
            return None
        return trim(root, low, high)
        

    def trimBSTIter(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        #1. Find new root inside [low, high]
        newRoot=root
        while newRoot and (newRoot.val<low or newRoot.val>high):
            if newRoot.val<low:
                newRoot=newRoot.right
            else:
                newRoot=newRoot.left
        #2. Pick left >= low
        cur=newRoot
        while cur:
            while cur.left and cur.left.val<low:
                cur.left=cur.left.right
            cur=cur.left
        
        #3. Pick right <= high
        cur=newRoot
        while cur:
            while cur.right and cur.right.val>high:
                cur.right=cur.right.left
            cur=cur.right
        
        return newRoot

import unittest

class TestSolution(unittest.TestCase):
    def testInvertTree(self):
        s = Solution()
        root=TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))
        s.invertTree(root)
        self.assertEqual(root, TreeNode(4,TreeNode(7,TreeNode(9),TreeNode(6)),TreeNode(2,TreeNode(3),TreeNode(1))))

        root=TreeNode(2,TreeNode(1),TreeNode(3))
        s.invertTree(root)
        self.assertEqual(root, TreeNode(2,TreeNode(3,TreeNode(1))))

if __name__ == '__main__':
    unittest.main()