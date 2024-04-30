from typing import List

class Solution:

    # Use graph coloring by starting with color 0
    # DFS and color each node to 1 or -1
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:   # Should not have same color due to dislike graph
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):     # Try to change 0 neighbor to negative color
                    return False
            return True

        graph = [[] for _ in range(n + 1)]
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        colors = [0] * (n + 1)
        for i in range(1, n + 1):
            if colors[i] == 0 and not dfs(i, color = 1):    # Try to color 1 to a 0 node, and dfs to color opposite of its neighbors
                return False
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testPossibleBipartition(self):
        s = Solution()
        self.assertEqual(s.possibleBipartition(n = 4, dislikes = [[1,2],[1,3],[2,4]]), True)
        self.assertEqual(s.possibleBipartition(n = 3, dislikes = [[1,2],[1,3],[2,3]]), False)


if __name__ == '__main__':
    unittest.main()