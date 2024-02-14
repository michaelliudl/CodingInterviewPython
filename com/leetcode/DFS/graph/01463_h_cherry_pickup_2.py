from typing import List

class Solution:

    # Bottom-up, DP
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m,n = len(grid), len(grid[0])
        dp = [[[0] * n for _ in range(n)] for _ in range(m+1)]      # dp is max number collected when robots are on row i and columns j1 and j2

        for row in range(m-1, -1, -1):
            for col1 in range(n):
                for col2 in range(n):
                    numberInCurRow = grid[row][col1] + grid[row][col2] if col1 != col2 else 0
                    nextRow = row + 1
                    for diff1 in range(-1, 2, 1):
                        for diff2 in range(-1, 2, 1):
                            nextCol1, nextCol2 = col1 + diff1, col2 + diff2
                            if nextCol1 >=0 and nextCol1 < n and nextCol2 >= 0 and nextCol2 < n:
                                dp[row][col1][col2] = max(dp[row][col1][col2], numberInCurRow + dp[nextRow][nextCol1][nextCol2])
        return dp[0][0][n-1]


    # Top-down, DFS + memoization
    def cherryPickupDFS(self, grid: List[List[int]]) -> int:

        def dfs(row, col1, col2):
            if row == m: return 0
            if col1 < 0 or col2 < 0 or col1 == n or col2 == n: return 0
            if mem[row][col1][col2] > -1:
                return mem[row][col1][col2]
            numberInCurRow = grid[row][col1] + grid[row][col2] if col1 != col2 else 0
            nextRow = row + 1
            for diff1 in range(-1,2,1):
                for diff2 in range(-1,2,1):
                    nextCol1, nextCol2 = col1 + diff1, col2 + diff2
                    numberInNextRow = dfs(nextRow, nextCol1, nextCol2)
                    mem[row][col1][col2] = max(mem[row][col1][col2], numberInCurRow + numberInNextRow)
            return mem[row][col1][col2]

        if not grid: return 0
        m,n = len(grid), len(grid[0])
        mem = [[[-1] * n for _ in range(n)] for _ in range(m)]  # Memoization for max number of cherries when robots are at row i and column j1 and j2
        return dfs(row=0, col1=0, col2=n-1)

import unittest

class TestSolution(unittest.TestCase):
    def testCherryPickup(self):
        s = Solution()
        self.assertEqual(s.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]), 24)
        self.assertEqual(s.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]), 28)

if __name__ == '__main__':
    unittest.main()