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

    def insertIntoBSTIter(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur=root
        while cur:
            if val<cur.val:
                if not cur.left:
                    cur.left=TreeNode(val)
                    break
                else:
                    cur=cur.left
            else:
                if not cur.right:
                    cur.right=TreeNode(val)
                    break
                else:
                    cur=cur.right
        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node, val):
            if val<node.val:
                if not node.left:
                    node.left=TreeNode(val)
                    return
                else:
                    insert(node.left, val)
            else:
                if not node.right:
                    node.right=TreeNode(val)
                    return
                else:
                    insert(node.right, val)

        if not root:
            return TreeNode(val)
        insert(root,val)
        return root

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