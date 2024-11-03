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

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Get sum of all values at each level
        def dfs(node, level):
            if not node:
                return
            if len(levelSums) == level:
                levelSums.append(0)
            levelSums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        def replace(node, level, curNode):
            nextLevel = level + 1
            nextLevelSum = 0
            if nextLevel < len(levelSums):
                nextLevelSum = levelSums[nextLevel]
            if node.left:
                nextLevelSum -= node.left.val
            if node.right:
                nextLevelSum -= node.right.val
            if node.left:
                curNode.left = TreeNode(nextLevelSum)
                replace(node.left, level + 1, curNode.left)
            if node.right:
                curNode.right = TreeNode(nextLevelSum)
                replace(node.right, level + 1, curNode.right)
            return curNode

        levelSums = []
        dfs(node=root, level=0)
        return replace(node=root, level=0, curNode=TreeNode(0))

    # TODO Fix BFS
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        childrenSum = {}
        queue = Deque()
        queue.append((root, None))
        while queue:
            curLen = len(queue)
            curChildrenSum = {}
            for _ in range(curLen):
                node, parent = queue.popleft()
                node.val = childrenSum[parent] if parent in childrenSum else 0
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
                if node.left or node.right:
                    
                    curChildrenSum[node] = node.left.val if node.left else 0
                    curChildrenSum[node] += node.right.val if node.right else 0
            childrenSum = curChildrenSum
        return root
    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrderIter(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None)))), [[3],[9,20],[15,7]])
        self.assertEqual(s.levelOrderIter(None), [])
        self.assertEqual(s.levelOrderIter(TreeNode(1,None,None)), [[1]])


if __name__ == '__main__':
    unittest.main()