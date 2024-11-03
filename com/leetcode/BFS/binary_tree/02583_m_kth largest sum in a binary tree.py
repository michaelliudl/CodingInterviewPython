from typing import Optional
from typing import List
from typing import Deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        queue = Deque()
        queue.append(root)
        while queue:
            curLen = len(queue)
            curSum = 0
            for _ in range(curLen):
                node = queue.popleft()
                curSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(heap) < k:
                heapq.heappush(heap, curSum)
            elif curSum > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, curSum)
        return -1 if len(heap) < k else heap[0]


    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()