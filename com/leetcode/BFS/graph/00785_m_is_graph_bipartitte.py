from typing import List,Deque,Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def dfs(node, isA):
            if (node in setA and isA) or (node in setB and not isA):
                return
            if isA:
                setA.add(node)
            else:
                setB.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, isA=(not isA))

        if not graph:
            return False
        n = len(graph)
        setA, setB = set(), set()
        for i in range(n):
            if i not in setA and i not in setB:
                dfs(i, isA=True)
        for i in range(n):
            if i in setA and i in setB:
                return False
        return True


import unittest

class TestSolution(unittest.TestCase):
    def testIsBipartite(self):
        s = Solution()
        self.assertEqual(s.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]), False)
        self.assertEqual(s.isBipartite(graph = [[1],[0,3],[3],[1,2]]), True)
        self.assertEqual(s.isBipartite(graph = [[1,3],[0,2],[1,3],[0,2]]), True)
        self.assertEqual(s.isBipartite(graph = [[3],[2,4],[1],[0,4],[1,3]]), True)
        


if __name__ == '__main__':
    unittest.main()