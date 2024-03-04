from typing import List,Deque,Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        if grid[0][0] == 1:
            return -1
        ans, steps = float('inf'), 1
        queue = Deque()
        queue.append((0, 0))
        visited[0][0] = True
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                row, col = queue.popleft()
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    ans = min(ans, steps)
                for dRow, dCol in ((-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)):
                    nRow, nCol = row + dRow, col + dCol
                    if (0 <= nRow < len(grid)) and (0 <= nCol < len(grid[0])) and grid[nRow][nCol] == 0 and not visited[nRow][nCol]:
                        visited[nRow][nCol] = True
                        queue.append((nRow,nCol))
            steps += 1
        return ans if ans < float('inf') else -1

import unittest

class TestSolution(unittest.TestCase):
    def testShortestPathBinaryMatrix(self):
        s = Solution()
        self.assertEqual(s.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,1]]), -1)
        self.assertEqual(s.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]), 2)
        self.assertEqual(s.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]), 4)
        self.assertEqual(s.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]), -1)


if __name__ == '__main__':
    unittest.main()