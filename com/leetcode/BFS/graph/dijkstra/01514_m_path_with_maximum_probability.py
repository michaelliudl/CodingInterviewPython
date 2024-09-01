from typing import List
import heapq

class Solution:

    # Dijkstra to track max probability
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for index, [u, v] in enumerate(edges):
            prob = succProb[index]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        heap = [(-1, start_node)]
        visited = [False] * n
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob
            if node == end_node:
                return prob
            visited[node] = True
            for neighbor, neighborProb in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(heap, (-(prob * neighborProb), neighbor))
        return 0

import unittest

class TestSolution(unittest.TestCase):
    def testMaxProbability(self):
        s = Solution()
        self.assertEqual(s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2), 0.25)
        self.assertEqual(s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2), 0.3)
        self.assertEqual(s.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2), 0)


if __name__ == '__main__':
    unittest.main()