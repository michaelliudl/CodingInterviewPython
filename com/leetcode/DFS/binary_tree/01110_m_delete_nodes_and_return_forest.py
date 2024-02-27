from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def dfs(target, node, parent, left):
            if not node:
                return False
            if node.val == target:
                if node.left:
                    forest.add(node.left)
                if node.right:
                    forest.add(node.right)
                if parent:
                    if left:
                        parent.left = None
                    else:
                        parent.right = None
                if node in forest:
                    forest.remove(node)
                return True
            delLeft = dfs(target, node.left, node, left=True)
            if delLeft:
                return True
            return dfs(target, node.right, node, left=False)

        if not root or not to_delete: return [root]
        forest = {root}
        for toDel in to_delete:
            for subRoot in forest:
                deleted = dfs(target=toDel, node=subRoot, parent=None, left=None)
                if deleted: break
        return list(forest)

import unittest

class TestSolution(unittest.TestCase):
    def testDelNodes(self):
        s = Solution()
        # self.assertEqual(s.delNodes(root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7))), 
        #                             to_delete = [3,5]), 
        #                  [TreeNode(1,TreeNode(2,TreeNode(4))), TreeNode(6), TreeNode(7)])
        self.assertEqual(s.delNodes(root=TreeNode(1,TreeNode(2,None,TreeNode(3)),TreeNode(4)),
                                    to_delete = [3]), 
                         [TreeNode(1,TreeNode(2),TreeNode(4))])


if __name__ == '__main__':
    unittest.main()