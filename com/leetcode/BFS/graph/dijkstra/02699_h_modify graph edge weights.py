from typing import List
import heapq

class Solution:

    # Dijkstra to find first modified edge that make shortest distance equals to `target`
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        def dijkstra():
            dists = [MAX] * n
            heap = [(0, source)]
            dists[source] = 0
            while heap:
                dist, node = heapq.heappop(heap)
                if dist < target:
                    for neighbor, weight in graph[node]:
                        if dist + weight < dists[neighbor]:
                            dists[neighbor] = dist + weight
                            heapq.heappush(heap, (dists[neighbor], neighbor))
            return dists[destination]

        MAX = 2 * 10 ** 9
        graph = [[] for _ in range(n)]
        for u, v, weight in edges:
            if weight > 0:              # First check graph w/o -1 weight edges
                graph[u].append((v, weight))
                graph[v].append((u, weight))
        dist = dijkstra()
        if dist < target:       # Not possible to make shortest path equals target
            return []
        m = len(edges)
        if dist == target:      # Shortest path w/o considering -1 edges equals target, change all -1 to MAX
            for i in range(m):
                if edges[i][2] == -1:
                    edges[i][2] = MAX
            return edges
        
        for i in range(m):
            edge = edges[i]
            u, v, weight = edge
            if weight == -1:        # Try -1 edges, change its weight to 1 and add to graph
                edge[2] = 1
                graph[u].append((v, 1))
                graph[v].append((u, 1))
                dist = dijkstra()   # Another round Dijkstra on updated graph
                if dist <= target:  # If < target, change this edge to the diff and all remaining -1s to MAX
                    edge[2] = 1 + (target - dist)
                    for j in range(i + 1, m):
                        if edges[j][2] == -1:
                            edges[j][2] = MAX
                    return edges
        # Changed all -1s to 1s, can't make shortest distance equal to target
        return []

import unittest

class TestSolution(unittest.TestCase):
    def testModifiedGraphEdges(self):
        s = Solution()
        self.assertEqual(s.modifiedGraphEdges(n = 5, edges = [[3,0,1],[2,1,-1],[2,3,6],[4,2,6],[1,3,2],[2,0,7],[0,4,10],[0,1,6]], source = 1, destination = 4, target = 14), 
                         [])
        self.assertEqual(s.modifiedGraphEdges(n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5), 
                         [[4,1,1],[2,0,1],[0,3,1],[4,3,3]])
        self.assertEqual(s.modifiedGraphEdges(n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6), 
                         [])
        self.assertEqual(s.modifiedGraphEdges(n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6), 
                         [[1,0,4],[1,2,3],[2,3,5],[0,3,1]])


if __name__ == '__main__':
    unittest.main()