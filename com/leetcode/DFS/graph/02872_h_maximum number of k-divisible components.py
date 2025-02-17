from typing import List, DefaultDict

class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        def dfs(node, prev):
            nonlocal res
            treeSum = values[node]
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                treeSum += dfs(neighbor, node)
            if treeSum % k == 0:
                res += 1
            return treeSum

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = 0
        dfs(node=0, prev=-1)
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testMaximalPathQuality(self):
        s = Solution()
        self.assertEqual(s.maximalPathQuality(values = [95], edges = [], maxTime = 83), 95)
        self.assertEqual(s.maximalPathQuality(values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49), 75)
        self.assertEqual(s.maximalPathQuality(values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30), 25)
        self.assertEqual(s.maximalPathQuality(values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50), 7)

if __name__ == '__main__':
    unittest.main()