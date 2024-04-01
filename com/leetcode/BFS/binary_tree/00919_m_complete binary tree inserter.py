from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.lowestCompleteLevel = []
        self.lowestLevel = []
        self.level = 0

        queue = Deque()
        queue.append(root)
        while queue:
            curLen = len(queue)
            if curLen == 2 ** self.level:
                self.lowestCompleteLevel = list(queue)
                for _ in range(curLen):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            else:
                self.lowestLevel = list(queue)
                break
            self.level += 1

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        insertIndex = len(self.lowestLevel)
        parent = self.lowestCompleteLevel[insertIndex // 2]
        if insertIndex % 2 == 0:
            parent.left = node
        else:
            parent.right = node
        self.lowestLevel.append(node)
        if len(self.lowestLevel) == 2 ** self.level:
            self.level += 1
            self.lowestCompleteLevel = self.lowestLevel
            self.lowestLevel = []
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

class Solution:
    pass
    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()