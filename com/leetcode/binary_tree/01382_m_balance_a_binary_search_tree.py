from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def balanceBST(self, root: TreeNode) -> TreeNode:

        def balance(low, high):
            if low>high:
                return None
            mid=low+(high-low)//2
            root=TreeNode(treeList[mid], balance(low,mid-1), balance(mid+1,high))
            return root

        def isBST(node):
            if not node: return (True,0)
            bLeft,hLeft=isBST(node.left)
            bRight,hRight=isBST(node.right)
            bNode=bLeft and bRight and (abs(hLeft-hRight)<=1)
            return (bNode,max(hLeft,hRight)+1)

        def inorder(node):
            if not node: return
            inorder(node.left)
            treeList.append(node.val)
            inorder(node.right)

        if not root: return root
        b,_=isBST(root)
        if b: return root
        treeList=[]
        inorder(root)
        newRoot = balance(0, len(treeList)-1)
        return newRoot

import unittest

class TestSolution(unittest.TestCase):
    def testBalanceBST(self):
        s = Solution()
        s.balanceBST(TreeNode(1,None,TreeNode(2,None,TreeNode(3,None,TreeNode(4)))))
        s.balanceBST(TreeNode(2,TreeNode(1),TreeNode(3)))

if __name__ == '__main__':
    unittest.main()