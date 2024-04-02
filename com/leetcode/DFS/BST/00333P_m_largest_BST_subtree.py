from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        
'''
Given the root of a binary tree, find the largest 
subtree
, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.
'''
class Solution:

    # Recurse and return if subtree rooted at `node` is BST, # of nodes, min/max value in the subtree
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def recur(node):
            # Leaf node
            if not node.left and not node.right:
                return (True, 1, node.val, node.val)
            # Default to empty subtree
            isLeftBST, leftCount, leftMin, leftMax = True, 0, node.val, node.val
            if node.left:
                isLeftBST, leftCount, leftMin, leftMax = recur(node.left)
            isRightBST, rightCount, rightMin, rightMax = True, 0, node.val, node.val
            if node.right:
                isRightBST, rightCount, rightMin, rightMax = recur(node.right)
            # Both left and right subtrees are BST, and node value > left max if left subtree exists,
            # and node value < right min if right subtree exists
            if isLeftBST and isRightBST and ((node.left and node.val > leftMax) or (not node.left)) \
                and ((node.right and node.val < rightMin) or (not node.right)):
                return True, 1 + leftCount + rightCount, leftMin, rightMax
            return False, max(leftCount, rightCount), leftMin, rightMax

        if not root:
            return 0
        _, result, _, _ = recur(root)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testLargestBSTSubtree(self):
        s = Solution()
        self.assertEqual(s.largestBSTSubtree(TreeNode(4,TreeNode(2,TreeNode(2,TreeNode(2,TreeNode(1))),TreeNode(3)),TreeNode(7,TreeNode(5)))), 2)
        self.assertEqual(s.largestBSTSubtree(TreeNode(10,TreeNode(5,TreeNode(1),TreeNode(8)),TreeNode(15,None,TreeNode(7)))), 3)


if __name__ == '__main__':
    unittest.main()