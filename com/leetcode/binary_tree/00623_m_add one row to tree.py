from typing import Optional,List,Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if depth <= 1:
            node = TreeNode(val, left = root)
            return node
        queue = Deque()
        queue.append(root)
        curDep = 1
        insertBelow = list(queue)
        while queue and curDep < depth - 1:
            curLen = len(queue)
            for _ in range(curLen):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                insertBelow = list(queue)
            curDep += 1
        for node in insertBelow:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, left = None, right = node.right)
        return root


import unittest

class TestSolution(unittest.TestCase):
    def testRightSideView(self):
        s = Solution()
        self.assertEqual(s.rightSideView(TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))), [1,3,4])
        self.assertEqual(s.rightSideView(TreeNode(1,None,TreeNode(3,))), [1,3])
        self.assertEqual(s.rightSideView(None), [])


if __name__ == '__main__':
    unittest.main()