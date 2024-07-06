from typing import List, Deque
import heapq

class Solution:

    # 1. Refer to 286 (Wall and gates). Use multi-start point BFS to find minimum distance to thieves for each cell
    # 2. Refer to 778 (Swim in rising water). Use Dijkstra to track maximum safety score along the paths
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        def valid(row, col):
            return 0 <= row < n and 0 <= col < n

        def bfs():
            queue = Deque()
            for row in range(n):
                for col in range(n):
                    if grid[row][col] == 1:
                        queue.append((row, col, 0))     # Enqueue row, col and distance
                        distances[(row, col)] = 0
            while queue:
                row, col, dist = queue.popleft()        # No need to check queue length since distance is part of queue element. Need to loop current queue length if external parameter is used to track distance
                for dRow, dCol in dirs:
                    nRow, nCol = row + dRow, col + dCol
                    if valid(nRow, nCol) and (nRow, nCol) not in distances:
                        nDist = dist + 1
                        queue.append((nRow, nCol, nDist))
                        distances[(nRow, nCol)] = nDist

        n = len(grid)
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        distances = {}      # Distances of each cell for step 1
        bfs()               # Multi-start BFS from thieves
        # Dijkstra with max heap
        heap = [(-distances[(0, 0)], 0, 0)]
        visited = set()
        visited.add((0, 0))
        while heap:
            val, row, col = heapq.heappop(heap)
            dist = -val
            if row == col == (n - 1):
                return dist
            for dRow, dCol in dirs:
                nRow, nCol = row + dRow, col + dCol
                if valid(nRow, nCol) and (nRow, nCol) not in visited:
                    visited.add((nRow, nCol))
                    nDist = min(dist, distances[(nRow, nCol)])
                    heapq.heappush(heap, (-nDist, nRow, nCol))

import unittest

class TestSolution(unittest.TestCase):
    def testMaximumSafenessFactor(self):
        s = Solution()
        self.assertEqual(s.maximumSafenessFactor(grid = [[1,0,0],[0,0,0],[0,0,1]]), 0)
        self.assertEqual(s.maximumSafenessFactor(grid = [[0,0,1],[0,0,0],[0,0,0]]), 2)
        self.assertEqual(s.maximumSafenessFactor(grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]), 2)


if __name__ == '__main__':
    unittest.main()