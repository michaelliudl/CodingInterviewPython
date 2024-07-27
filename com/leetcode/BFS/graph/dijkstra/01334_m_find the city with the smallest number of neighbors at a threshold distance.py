from typing import List
import heapq

class Solution:

    # Dijkstra to find reachable nodes within distance threshold from each node, due to non-negative edge weight
    def findTheCityDijkstra(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def dijkstra(node):
            heap = [(0, node)]
            visited = set()
            while heap:
                dist, cur = heapq.heappop(heap)
                if cur in visited:
                    continue
                visited.add(cur)
                for neighbor, nextDist in graph[cur]:
                    if neighbor in visited:
                        continue
                    neighborDist = dist + nextDist
                    if neighborDist <= distanceThreshold:
                        heapq.heappush(heap, (neighborDist, neighbor))
            return len(visited) - 1     # `visited` includes source

        graph = [[] for _ in range(n)]
        for u, v, dist in edges:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        res, minReachable = -1, n
        for node in range(n):
            reachable = dijkstra(node)
            if reachable <= minReachable:   # Get larger node if equal min distance
                res = node
                minReachable = reachable
        return res

    # Floyd-Warshall to find shortest distance between nodes
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def floydWarshall():
            graph = [[distanceThreshold + 1] * n for _ in range(n)]     # Initialize as threshold + 1
            for i in range(n):
                graph[i][i] = 0
            for u, v, weight in edges:
                graph[u][v] = weight
                graph[v][u] = weight
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        graph[i][j] = min(graph[i][j], (graph[i][k] + graph[k][j]))
            return graph

        graph = floydWarshall()
        res, minCount = -1, n
        for i in range(n):
            curCount = sum(graph[i][j] <= distanceThreshold for j in range(n))
            if curCount <= minCount:
                res = i
                minCount = curCount
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testFindTheCity(self):
        s = Solution()
        self.assertEqual(s.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4), 3)
        self.assertEqual(s.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2), 0)


if __name__ == '__main__':
    unittest.main()