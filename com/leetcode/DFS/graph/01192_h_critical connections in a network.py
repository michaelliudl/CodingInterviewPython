from typing import List

class Solution:

    # DFS and use Tarjan's algo to find bridges
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def buildGraph():
            for u, v in connections:
                if u not in graph:
                    graph[u] = set()
                if v not in graph:
                    graph[v] = set()
                graph[u].add(v)
                graph[v].add(u)
        
        def dfs(node, parent, time):
            discoveryTime[node] = lowLink[node] = time
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    lowLink[node] = min(lowLink[node], discoveryTime[neighbor])
                else:
                    dfs(node=neighbor, parent=node, time=time + 1)
                    lowLink[node] = min(lowLink[node], lowLink[neighbor])
                    if lowLink[neighbor] > discoveryTime[node]:
                        bridges.append([node, neighbor])

        if n <= 0 or not connections:
            return []
        graph = {}
        buildGraph()

        bridges = []
        discoveryTime = [-1] * n
        lowLink = [-1] * n
        visited = set()
        for node in range(n):
            if node not in visited:
                dfs(node=node, parent=-1, time=0)
        return bridges

import unittest

class TestSolution(unittest.TestCase):
    def testCriticalConnections(self):
        s = Solution()
        self.assertEqual(s.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]), [[1,3]])
        self.assertEqual(s.criticalConnections(n = 2, connections = [[0,1]]), [[0,1]])

if __name__ == '__main__':
    unittest.main()