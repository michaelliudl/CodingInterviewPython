from typing import List,Deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        queue = Deque()
        queue.append(source)
        visited = set()
        visited.add(source)
        while queue:
            cur = queue.popleft()
            if cur == destination:
                return True
            if cur in graph:
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testNumEnclaves(self):
        s = Solution()
        self.assertEqual(s.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(s.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()