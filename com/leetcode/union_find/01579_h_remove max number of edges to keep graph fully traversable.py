from typing import List

class UnionFind:

    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
    
    def _find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        parentU = self._find(u)
        parentV = self._find(v)
        if parentU == parentV:
            return False
        if self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = parentV
        elif self.rank[parentU] > self.rank[parentV]:
            self.parent[parentV] = parentU
        else:
            self.parent[parentU] = parentV
            self.rank[parentV] += 1
        self.count -= 1
        return True
    
    def isConnected(self):
        return self.count == 1

class Solution:
    # Use 2 UnionFind instance to track connectivity for each type
    # When counting connectivity, prefer edge type that works for both
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        graph1 = UnionFind(n)
        graph2 = UnionFind(n)
        numEdgesNeeded = 0

        for type, u, v in edges:
            if type == 3:       # Greedily process type 3 (connectivity for both) first
                res1 = graph1.union(u, v)
                res2 = graph2.union(u, v)
                if res1 or res2:
                    numEdgesNeeded += 1
        for type, u, v in edges:
            if type == 1:
                if graph1.union(u, v):
                    numEdgesNeeded += 1
            else:
                if graph2.union(u, v):
                    numEdgesNeeded += 1
        
        if graph1.isConnected() and graph2.isConnected():
            return len(edges) - numEdgesNeeded
        return -1

import unittest

class TestSolution(unittest.TestCase):
    def testMaxNumEdgesToRemove(self):
        s = Solution()
        self.assertEqual(s.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]), 2)
        self.assertEqual(s.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]), 0)
        self.assertEqual(s.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]), -1)


if __name__ == '__main__':
    unittest.main()