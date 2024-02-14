from typing import List,Deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    # A graph can form at most 1 or 2 MHTs
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        def buildGraph():
            for node1, node2 in edges:
                if node1 in graph:
                    graph[node1].append(node2)
                else:
                    graph[node1] = [node2]
                if node2 in graph:
                    graph[node2].append(node1)
                else:
                    graph[node2] = [node1]

        if n<=1 or not edges: return [0]
        graph = {}
        buildGraph()

        # Find leaves
        leaves = [node for node, neighbors in graph.items() if len(neighbors) == 1]

        # Iteratively remove leaf nodes until node count is 1 or 2
        nodeCount = n
        while nodeCount > 2:
            nodeCount -= len(leaves)
            nextLeaves = []
            for leaf in leaves:
                nextLeaf = graph[leaf].pop()
                graph[nextLeaf].remove(leaf)
                if len(graph[nextLeaf]) == 1:
                    nextLeaves.append(nextLeaf)
            leaves = nextLeaves
        return leaves

import unittest

class TestSolution(unittest.TestCase):
    def testFindMinHeightTrees(self):
        s = Solution()
        self.assertEqual(s.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]), [1])
        self.assertEqual(s.findMinHeightTrees(n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]), [3,4])
        


if __name__ == '__main__':
    unittest.main()