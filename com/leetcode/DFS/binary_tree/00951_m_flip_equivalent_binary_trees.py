from typing import Optional
from typing import List,Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1:
            return not root2
        if not root2:
            return not root1
        if root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
                or
                (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
                )

    # DFS, all paths should match
    def flipEquivUsingPath(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def inorder(node, paths, path):
            if not node.left and not node.right:
                path.append(node.val)
                paths.append(path[:])
                path.pop()
                return
            path.append(node.val)
            if node.left:
                inorder(node.left, paths, path)
            if node.right:
                inorder(node.right, paths, path)
            path.pop()

        if not root1 and not root2: return True
        if not root1 or not root2: return False
        paths1,paths2 = [],[]
        inorder(root1, paths1, path=[])
        inorder(root2, paths2, path=[])
        # Convert sublist to tuple for set. Order is retained.
        return set(tuple(path) for path in paths1) == set(tuple(path) for path in paths2)
        

import unittest

class TestSolution(unittest.TestCase):
    def testFlipEquiv(self):
        s = Solution()
        self.assertEqual(s.flipEquiv(root1=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(7),TreeNode(8))),TreeNode(3,TreeNode(6))),
                                     root2=TreeNode(1,TreeNode(3,None,TreeNode(6)),TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(8),TreeNode(7))))),
                                     True)
        self.assertEqual(s.flipEquiv(None, TreeNode(1,None,None)), False)
        self.assertEqual(s.flipEquiv(None, None), True)


if __name__ == '__main__':
    unittest.main()