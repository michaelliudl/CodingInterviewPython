from typing import List, Deque

class Solution:

    # BFS after adding each edge
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def bfs(start):
            queue = Deque()
            queue.append(start)
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if shortestDist[node] + 1 < shortestDist[neighbor]: # Similiarly update shortest distance of nodes
                        shortestDist[neighbor] = shortestDist[node] + 1
                        queue.append(neighbor)

        graph = [[i + 1] for i in range(n - 1)]
        graph.append([])    # Placeholder for node `n - 1`
        shortestDist = [i for i in range(n)]    # Shortest distance from `0` to each node
        res = [0] * len(queries)
        for i, [u, v] in enumerate(queries):
            graph[u].append(v)  # Add edge, `v` is now reachable from `u`.
            if shortestDist[u] + 1 < shortestDist[v]:   # If `v` has a shorter distance from `0`, it could lead to a shorter distance to `n - 1`. BFS to update shortest distance for all nodes reachable from `v`.
                shortestDist[v] = shortestDist[u] + 1
                bfs(start=v)
            res[i] = shortestDist[n - 1]
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()