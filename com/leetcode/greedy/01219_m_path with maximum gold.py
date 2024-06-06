from typing import List

class Solution:

    # Backtrack from each possible starting location
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(x, y, val):
            nonlocal res
            res = max(res, val)
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    nVal = grid[nx][ny]
                    grid[nx][ny] = 0
                    dfs(nx, ny, val + nVal)
                    grid[nx][ny] = nVal

        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    val = grid[i][j]
                    grid[i][j] = 0
                    dfs(i, j, val = val)
                    grid[i][j] = val
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testCanJump(self):
        s = Solution()
        self.assertEqual(s.canJump(nums = [2,3,1,1,4]), True)
        self.assertEqual(s.canJump(nums = [3,2,1,0,4]), False)
        


if __name__ == '__main__':
    unittest.main()