from typing import Optional
from typing import List, Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Difference with 314?
    # BFS to get each node's row and column and cache in map
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        map = {}
        queue = Deque()
        queue.append((root, 0, 0))
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                node, row, col = queue.popleft()
                if col not in map:
                    map[col] = {}
                if row not in map[col]:
                    map[col][row] = []
                map[col][row].append(node.val)
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
        columns = sorted(map.keys())
        result = []
        for col in columns:
            values = []
            rows = sorted(map[col].keys())
            for row in rows:
                values.extend(sorted(map[col][row]))
            result.append(values)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testVerticalTraversal(self):
        s = Solution()
        self.assertEqual(s.verticalTraversal(TreeNode(3,TreeNode(1,TreeNode(0),TreeNode(2)),TreeNode(4,TreeNode(2)))), 
                         [[0],[1],[3,2,2],[4]])
        self.assertEqual(s.verticalTraversal(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 
                         [[9],[3,15],[20],[7]])
        self.assertEqual(s.verticalTraversal(TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))), 
                         [[4],[2],[1,5,6],[3],[7]])
        self.assertEqual(s.verticalTraversal(TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(6)),TreeNode(3,TreeNode(5),TreeNode(7)))), 
                         [[4],[2],[1,5,6],[3],[7]])


if __name__ == '__main__':
    unittest.main()