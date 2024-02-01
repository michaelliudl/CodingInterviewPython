from typing import Optional
from typing import List
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            if not node: return
            inorder(node.left)
            if len(h)<k:
                heapq.heappush(h,-node.val)
            inorder(node.right)

        if not root: return -1
        h=[]
        inorder(root)
        return -heapq.heappop(h)


    def kthSmallestRecur(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal counter,r
            if not node or counter>k: return
            inorder(node.left)
            if counter==k:
                r=node.val 
            counter+=1
            inorder(node.right)
        
        if not root: return -1
        counter,r=1,None
        inorder(root)
        return r

import unittest

class TestSolution(unittest.TestCase):
    def testKthSmallest(self):
        s = Solution()
        self.assertEqual(s.kthSmallest(root = TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4)), k = 1), 1)
        self.assertEqual(s.kthSmallest(root = TreeNode(5,TreeNode(3,TreeNode(2,TreeNode(1)),TreeNode(4)),TreeNode(6)), k = 3), 3)


if __name__ == '__main__':
    unittest.main()