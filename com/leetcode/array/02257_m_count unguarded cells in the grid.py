from typing import List

class Solution:
    
    # Simulate and optimize
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        # Mark all walls and guards first to avoid redundant iterations
        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 2
        # Mark cells seen, stop at wall or other guards
        for r, c in guards:
            for i in range(r + 1, m):
                if grid[i][c] in (1, 2):
                    break
                grid[i][c] = 3
            for i in range(r - 1, -1, -1):
                if grid[i][c] in (1, 2):
                    break
                grid[i][c] = 3
            for j in range(c + 1, n):
                if grid[r][j] in (1, 2):
                    break
                grid[r][j] = 3
            for j in range(c - 1, -1, -1):
                if grid[r][j] in (1, 2):
                    break
                grid[r][j] = 3
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testCountUnguarded(self):
        s = Solution()
        self.assertEqual(s.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]), 7)
        self.assertEqual(s.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]), 4)

if __name__ == '__main__':
    unittest.main()