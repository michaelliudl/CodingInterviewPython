from typing import List
import heapq, math

class Solution:

    # Similar to Dijkstra, use 2D array and min heap to find shortest distance with possible removal to destination
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        removals = [[math.inf] * n for _ in range(m)]
        removals[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]     # (min removal to reach x y, x, y)

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            removal, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                break
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nRemoval = removal + grid[nx][ny]
                    if nRemoval < removals[nx][ny]:
                        removals[nx][ny] = nRemoval
                        heapq.heappush(heap, (nRemoval, nx, ny))
        return removals[m - 1][n - 1]



import unittest

class TestSolution(unittest.TestCase):
    def testModifiedGraphEdges(self):
        s = Solution()
        self.assertEqual(s.modifiedGraphEdges(n = 5, edges = [[3,0,1],[2,1,-1],[2,3,6],[4,2,6],[1,3,2],[2,0,7],[0,4,10],[0,1,6]], source = 1, destination = 4, target = 14), 
                         [])
        self.assertEqual(s.modifiedGraphEdges(n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5), 
                         [[4,1,1],[2,0,1],[0,3,1],[4,3,3]])
        self.assertEqual(s.modifiedGraphEdges(n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6), 
                         [])
        self.assertEqual(s.modifiedGraphEdges(n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6), 
                         [[1,0,4],[1,2,3],[2,3,5],[0,3,1]])


if __name__ == '__main__':
    unittest.main()