from typing import List
import heapq

class Solution:

    # Dijkstra to track min effort to reach each cell
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return -1
        rows, cols = len(heights), len(heights[0])
        minEffort = [[float('inf')] * cols for _ in range(rows)]
        minEffort[0][0] = 0

        heap = [(0, 0, 0)]      # (effort, row, col)
        while heap:
            curEffort, row, col = heapq.heappop(heap)
            if row == rows - 1 and col == cols - 1:
                return curEffort

            for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextRow, nextCol = row + dRow, col + dCol
                if 0 <= nextRow < rows and 0 <= nextCol < cols:
                    nextEffort = max(curEffort, abs(heights[nextRow][nextCol] - heights[row][col]))
                    if nextEffort < minEffort[nextRow][nextCol]:
                        minEffort[nextRow][nextCol] = nextEffort
                        heapq.heappush(heap, (nextEffort, nextRow, nextCol))
        



import unittest

class TestSolution(unittest.TestCase):
    def testMinimumEffortPath(self):
        s = Solution()
        self.assertEqual(s.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]), 2)
        self.assertEqual(s.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]), 1)
        self.assertEqual(s.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]), 0)


if __name__ == '__main__':
    unittest.main()