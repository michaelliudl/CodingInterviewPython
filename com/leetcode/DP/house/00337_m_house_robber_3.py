from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Use recursion stack as DP array. Postorder the tree.
    # Each recursion returns result whether or not to include current node: (node + grandchildren) or (children)
    def rob(self, root: Optional[TreeNode]) -> int:
        def postorder(node) -> (int, int):      # Tuple 0 is node + grandchildren, tuple 1 is children
            if not node: 
                return (0,0)
            (lChild, lGrandChildren) = postorder(node.left)
            (rChild, rGrandChildren) = postorder(node.right)
            curNode = node.val + lGrandChildren + rGrandChildren    # Current node + grand children
            curChildren = max(lChild, lGrandChildren) + max(rChild, rGrandChildren)     # Choose max from child or grandchilden
            return (curNode, curChildren)

        if not root:
            return 0
        (rootNode, rootChildren) = postorder(root)
        return max(rootNode, rootChildren)

    # Brute force with memoization
    def robMemo(self, root: Optional[TreeNode]) -> int:

        def postorder(node) -> int:
            if not node:
                return 0
            if node in cache:
                return cache[node]
            
            rChild = 0
            rChild += postorder(node.left)
            rChild += postorder(node.right)
            
            rNode = node.val
            rNode += postorder(node.left.left) if node.left else 0
            rNode += postorder(node.left.right) if node.left else 0
            rNode += postorder(node.right.left) if node.right else 0
            rNode += postorder(node.right.right) if node.right else 0

            r=max(rNode, rChild)
            cache[node]=r
            return r

        if not root:
            return 0
        cache={}
        return postorder(root)


import unittest

class TestSolution(unittest.TestCase):
    def testRob(self):
        s = Solution()
        self.assertEqual(s.rob(TreeNode(3,TreeNode(2,None,TreeNode(3)),TreeNode(3,None,TreeNode(1)))), 7)
        self.assertEqual(s.rob(TreeNode(3,TreeNode(4,TreeNode(1),TreeNode(3)),TreeNode(5,None,TreeNode(1)))), 9)
        self.assertEqual(s.rob(TreeNode(4,TreeNode(1,TreeNode(2,TreeNode(3))))), 7)
        


if __name__ == '__main__':
    unittest.main()