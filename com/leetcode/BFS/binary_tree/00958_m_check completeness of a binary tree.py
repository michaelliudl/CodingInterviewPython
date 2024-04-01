from typing import List,Deque,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # BFS and add empty children to queue until queue head is empty
    # Verify no solid node after empty node in queue
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = Deque()
        queue.append(root)
        while queue[0]:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
        while queue and not queue[0]:
            queue.popleft()
        return not queue
    
    # DFS get total nodes count, then another DFS check if any valid node's index (in flatten array) is larger than `count`
    def isCompleteTreeDFS(self, root: Optional[TreeNode]) -> bool:

        def getCount(node):
            if not node:
                return 0
            return 1 + getCount(node.left) + getCount(node.right)

        def isComplete(node, index):
            if not node:        # Same base case as root == null
                return True
            if index >= total:  # index out of bound in flatten array
                return False
            return isComplete(node.left, index * 2 + 1) and isComplete(node.right, index * 2 + 2)

        if not root:
            return True
        total = getCount(root)
        complete = isComplete(root, index = 0)
        return complete

import unittest

class TestSolution(unittest.TestCase):
    def testUpdateMatrix(self):
        s = Solution()
        self.assertEqual(s.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]), 
                         [[0,0,0],[0,1,0],[0,0,0]])
        self.assertEqual(s.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]), 
                         [[0,0,0],[0,1,0],[1,2,1]])
        


if __name__ == '__main__':
    unittest.main()