from typing import List
import heapq

class Solution:

    # Dijkstra to find min height neighbor to continue after some time
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        time = 0
        heap = [(grid[0][0], (0, 0))]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        while heap:
            elev = heap[0][0]
            if elev > time:
                time += 1
                continue
            elev, (x, y) = heapq.heappop(heap)
            visited.add((x, y))
            if (x, y) == (rows - 1, cols - 1):
                return time
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    heapq.heappush(heap, (grid[nx][ny], (nx, ny)))
                    visited.add((nx, ny))



import unittest

class TestSolution(unittest.TestCase):
    def testSwimInWater(self):
        s = Solution()
        self.assertEqual(s.swimInWater(grid = [[3,2],[0,1]]), 3)
        self.assertEqual(s.swimInWater(grid = [[0,2],[1,3]]), 3)
        self.assertEqual(s.swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]), 16)


if __name__ == '__main__':
    unittest.main()