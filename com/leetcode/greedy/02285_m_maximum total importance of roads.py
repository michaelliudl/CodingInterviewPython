from typing import List, DefaultDict
import heapq

class Solution:

    # Greedy, nodes with more edges got higher score
    # Single nodes 0 score
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edges = [0] * n
        for start, end in roads:
            edges[start] += 1
            edges[end] += 1
        edges.sort()
        return sum((index + 1) * edgeCount for index, edgeCount in enumerate(edges))    # `index + 1` is score

    def maximumImportanceHeap(self, n: int, roads: List[List[int]]) -> int:
        graph = DefaultDict(list)
        for start, end in roads:
            graph[start].append(end)
            graph[end].append(start)
        heap = []
        for _, neighbors in graph.items():
            heapq.heappush(heap, -len(neighbors))
        res = 0
        for score in range(n, 0, -1):
            if not heap:
                break
            res += score * (-heapq.heappop(heap))
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinOperations(self):
        s = Solution()
        self.assertEqual(s.minOperations(k = 11), 5)
        self.assertEqual(s.minOperations(k = 1), 0)


if __name__ == '__main__':
    unittest.main()