from typing import Optional
from typing import List
import functools

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Tree node values are unique. DFS to find height of each node.
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        @functools.cache
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def dfs(node, depth, maxHeight):
            if not node:
                return
            valueToHeight[node.val] = maxHeight
            dfs(node.left, depth + 1, max(maxHeight, depth + height(node.right)))
            dfs(node.right, depth + 1, max(maxHeight, depth + height(node.left)))

        valueToHeight = {}
        dfs(node=root, depth=0, maxHeight=0)
        return [valueToHeight[query] for query in queries]

import unittest

class TestSolution(unittest.TestCase):
    def testPostorderTraversal(self):
        s = Solution()
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))), [3,2,1])
        self.assertEqual(s.postorderTraversalIter(None), [])
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,None)), [1])


if __name__ == '__main__':
    unittest.main()