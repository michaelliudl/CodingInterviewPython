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

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node, key):
            if not node:
                return None
            if key<node.val:
                node.left=delete(node.left, key)
            elif key>node.val:
                node.right=delete(node.right, key)
            else:
                # Delete this node
                # 1. Delete leaf
                if not node.left and not node.right: 
                    return None
                # 2. Deleted node has child on one side
                elif node.left and not node.right:
                    return node.left
                elif not node.left and node.right:
                    return node.right
                else:
                # 3. Deleted node has child on both, two options
                # 3a. Promote node's right and move node's left to left most child of node's right
                    p=node.right
                    while p.left:
                        p=p.left
                    p.left=node.left
                    return node.right
                # 3b. Promote node's left and move node's right to right most child of node's left
                    # p=node.left
                    # while p.right:
                    #     p=p.right
                    # p.right=node.right
                    # return node.left
            return node

        if not root:
            return None
        newRoot=delete(root,key)
        return newRoot

    def deleteNodeIter(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        prev,cur,newRoot=None,root,root
        while cur:
            if key<cur.val:
                prev=cur
                cur=cur.left
            elif key>cur.val:
                prev=cur
                cur=cur.right
            else:
                if not cur.left and not cur.right:
                    if not prev:
                        newRoot=None # Delete single root node
                    elif cur.val<prev.val:
                        prev.left=None
                    else:
                        prev.right=None
                elif cur.left and not cur.right:
                    if not prev:
                        newRoot=cur.left # Delete root node, return new root
                    elif cur.val<prev.val:
                        prev.left=cur.left
                    else:
                        prev.right=cur.left
                elif not cur.left and cur.right:
                    if not prev:
                        newRoot=cur.right # Delete root node, return new root
                    elif cur.val<prev.val:
                        prev.left=cur.right
                    else:
                        prev.right=cur.right
                else:
                    p=cur.right # Promote right of deleted
                    while p.left:
                        p=p.left
                    p.left=cur.left
                    newCur=cur.right
                    # p=cur.left # Promote left of deleted
                    # while p.right:
                    #     p=p.right
                    # p.right=cur.right
                    # newCur=cur.left
                    if not prev:
                        newRoot=newCur
                    elif cur.val<prev.val:
                        prev.left=newCur
                    else:
                        prev.right=newCur
                break
                    
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