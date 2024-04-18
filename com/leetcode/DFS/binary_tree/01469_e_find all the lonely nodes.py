from typing import Optional,List,Deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node, lone):
            if not node:
                return
            if lone:
                ret.append(node.val)
            if node.left and node.right:
                dfs(node.left, lone = False)
                dfs(node.right, lone = False)
            elif node.left:
                dfs(node.left, lone = True)
            elif node.right:
                dfs(node.right, lone = True)

        ret = []
        dfs(root, lone = False)
        return ret

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