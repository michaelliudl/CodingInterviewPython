from typing import Optional,List,Deque

'''
Given the root of a binary tree and a leaf node, reroot the tree so that the leaf is the new root.

You can reroot the tree with the following steps for each node cur on the path starting from the leaf up to the root​​​ excluding the root:

If cur has a left child, then that child becomes cur's right child.
cur's original parent becomes cur's left child. Note that in this process the original parent's pointer to cur becomes null, making it have at most one child.
Return the new root of the rerooted tree.

Note: Ensure that your solution sets the Node.parent pointers correctly after rerooting or you will receive "Wrong Answer".


'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:

    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        if not root or not leaf:
            return None
        cur = leaf
        prevParent = None
        while cur:
            if cur != root and cur.left:    # Don't switch left/right for root
                cur.right = cur.left
            parent = cur.parent
            if parent:
                if cur == parent.left:      # Set parent left/right link based on cur to avoid loop
                    parent.left = None
                if cur == parent.right:
                    parent.right = None
            if cur != root:                 # Don't change left to parent for root
                cur.left = parent
            cur.parent = prevParent
            prevParent = cur
            cur = parent
        return leaf

import unittest

class TestSolution(unittest.TestCase):

    def testFlipBinaryTree(self):

        def buildTree():
            node3 = Node(3)
            node5 = Node(5)
            node5.parent = node3
            node1 = Node(1)
            node1.parent = node3
            node3.left = node5
            node3.right = node1

            node6 = Node(6)
            node2 = Node(2)
            node6.parent = node5
            node2.parent = node5
            node5.left = node6
            node5.right = node2

            node7 = Node(7)
            node4 = Node(4)
            node7.parent = node2
            node4.parent = node2
            node2.left = node7
            node2.right = node4

            node0 = Node(0)
            node8 = Node(8)
            node0.parent = node1
            node8.parent = node1
            node1.left = node0
            node1.right = node8

            return node3, node0

        s = Solution()
        root, leaf = buildTree()
        newRoot = s.flipBinaryTree(root, leaf)
        self.assertEqual(newRoot, leaf)

    # def testFlipBinaryTree1(self):

    #     def buildTree():
    #         node3 = Node(3)
    #         node5 = Node(5)
    #         node5.parent = node3
    #         node1 = Node(1)
    #         node1.parent = node3
    #         node3.left = node5
    #         node3.right = node1

    #         node6 = Node(6)
    #         node2 = Node(2)
    #         node6.parent = node5
    #         node2.parent = node5
    #         node5.left = node6
    #         node5.right = node2

    #         node7 = Node(7)
    #         node4 = Node(4)
    #         node7.parent = node2
    #         node4.parent = node2
    #         node2.left = node7
    #         node2.right = node4

    #         node0 = Node(0)
    #         node8 = Node(8)
    #         node0.parent = node1
    #         node8.parent = node1
    #         node1.left = node0
    #         node1.right = node8

    #         return node3, node7

    #     s = Solution()
    #     root, leaf = buildTree()
    #     newRoot = s.flipBinaryTree(root, leaf)
    #     self.assertEqual(newRoot, leaf)


if __name__ == '__main__':
    unittest.main()