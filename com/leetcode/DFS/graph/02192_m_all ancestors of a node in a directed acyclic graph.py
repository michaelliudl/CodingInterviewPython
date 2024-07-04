from typing import List,Deque

class Solution:

    # DFS each node and track its ancestors that were not visited
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def dfs(node, ancestor, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                res[neighbor].append(ancestor)
                dfs(neighbor, ancestor, visited)

        graph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
        res = [[] for _ in range(n)]
        for i in range(n):
            dfs(i, i, set())
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testNumIslands(self):
        s = Solution()
        self.assertEqual(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]), False)
        self.assertEqual(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]), True)
        self.assertEqual(s.hasPath(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]), False)


if __name__ == '__main__':
    unittest.main()