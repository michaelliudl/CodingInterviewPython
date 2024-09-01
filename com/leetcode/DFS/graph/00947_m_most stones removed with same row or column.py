from typing import List

class Solution:

    # TODO Solve with Union Find

    # Graph built for each column and rows as elements
    # DFS to find number of islands and substract from total columns
    def removeStones(self, stones: List[List[int]]) -> int:

        def dfs(node):
            visited[node] = 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        n = len(stones)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = [0] * n
        numIslands = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                numIslands += 1
        return n - numIslands

import unittest

class TestSolution(unittest.TestCase):
    def testRemoveStones(self):
        s = Solution()
        self.assertEqual(s.removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]), 5)
        self.assertEqual(s.removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]), 3)
        self.assertEqual(s.removeStones(stones = [[0,0]]), 0)


if __name__ == '__main__':
    unittest.main()