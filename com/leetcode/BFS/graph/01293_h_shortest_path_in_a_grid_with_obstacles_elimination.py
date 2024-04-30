from typing import List,Deque

class Solution:

    # BFS with 3 dimensions, 3rd dimension for up to `k` eliminations
    # Each grid cell can be visited up to `k` times
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or k < 0:
            return 0
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        queue = Deque()
        queue.append((0, 0, 0))
        visited = set()
        visited.add((0, 0, 0))
        steps = 0
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                x, y, elemination = queue.popleft()
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx, ny = x + dx, y + dy
                    if nx == m - 1 and ny == n - 1:
                        return steps + 1
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1 and elemination == k:
                            continue
                        newElemination = elemination + grid[nx][ny]
                        if (nx, ny, newElemination) not in visited:
                            queue.append((nx, ny, newElemination))
                            visited.add((nx, ny, newElemination))
            steps += 1
        return -1
        

import unittest

class TestSolution(unittest.TestCase):
    def testShortestPath(self):
        s = Solution()
        self.assertEqual(s.shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1), 6)
        self.assertEqual(s.shortestPath(grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1), -1)
        self.assertEqual(s.shortestPath(grid = [[0]], k = 1), 0)


if __name__ == '__main__':
    unittest.main()