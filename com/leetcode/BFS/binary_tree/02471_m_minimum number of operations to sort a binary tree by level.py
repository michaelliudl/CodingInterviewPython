from typing import Optional
from typing import List
from typing import Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # BFS then sort values with index on each level. Then count number of operations to sort the indexes.
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = Deque()
        queue.append(root)
        res = 0
        while queue:
            curLen = len(queue)
            values = []
            for i in range(curLen):
                node = queue.popleft()
                values.append((node.val, i))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.sort()
            indexes = [i for _, i in values]
            for i in range(len(indexes)):
                while indexes[i] != i:
                    j = indexes[i]
                    indexes[i] = indexes[j]
                    indexes[j] = j
                    res += 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()