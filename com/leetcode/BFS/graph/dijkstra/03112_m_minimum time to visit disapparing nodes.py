from typing import List
import heapq

class Solution:

    # Dijkstra to visit nodes with minimum time
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))
        heap = [(0, 0)]
        ret = [-1] * n
        used = set()
        while heap:
            time, node = heapq.heappop(heap)
            # Skip nodes already traversed
            if node in used:
                continue
            used.add(node)
            # Node can be visited only `time` is less than its disappearing time
            if time < disappear[node]:
                ret[node] = time
                # Only visit neighbors of non-dissappeared nodes
                for other, otherTime in graph[node]:
                    if other not in used:
                        heapq.heappush(heap, (time + otherTime, other))     # Dijkstra for time to visit nodes
        return ret
        



import unittest

class TestSolution(unittest.TestCase):
    def testMinimumEffortPath(self):
        s = Solution()
        self.assertEqual(s.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]), 2)
        self.assertEqual(s.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]), 1)
        self.assertEqual(s.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]), 0)


if __name__ == '__main__':
    unittest.main()