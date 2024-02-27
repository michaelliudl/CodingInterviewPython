from typing import Optional
from typing import List,Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:

    # Build graph from tree, then BFS from `target` node
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def buildGraph(node, parent):
            if not node: return
            if parent:
                if node not in graph:
                    graph[node] = []
                if parent not in graph:
                    graph[parent] = []
                graph[node].append(parent)
                graph[parent].append(node)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        if not root or not target: return []
        graph = {}
        buildGraph(root, parent=None)
        queue = Deque()
        queue.append(target)
        dist,ans,visited = 0,[],set()
        visited.add(target)
        while queue and dist <= k:
            curLen = len(queue)
            for _ in range(curLen):
                node = queue.popleft()
                if dist == k:
                    ans.append(node.val)
                elif node in graph:
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
            dist += 1
        return ans
        

import unittest

class TestSolution(unittest.TestCase):
    def testPostorderTraversal(self):
        s = Solution()
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))), [3,2,1])
        self.assertEqual(s.postorderTraversalIter(None), [])
        self.assertEqual(s.postorderTraversalIter(TreeNode(1,None,None)), [1])


if __name__ == '__main__':
    unittest.main()