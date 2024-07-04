from typing import List, DefaultDict

class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        graph = DefaultDict(list)
        n = len(edges) + 1
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for u, neighbors in graph.items():
            if len(neighbors) == n - 1:
                return u
        return -1

import unittest

class TestSolution(unittest.TestCase):
    def testRotate(self):
        s = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if __name__ == '__main__':
    unittest.main()