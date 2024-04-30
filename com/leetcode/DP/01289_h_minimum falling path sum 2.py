from typing import List
import math

class Solution:

    # DP, update original `grid` per DP rule
    # Top - down, find `min` and `second min` value and column from prev row
    # Update each column on current row plus `min` if current column is not `min` column, else plus `second min`
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) != len(grid[0]):
            return 0
        n = len(grid)
        minV = secMinV = math.inf
        minCol = -1             # Second min value's column no need to consider
        for i in range(n):
            if grid[0][i] < minV:
                secMinV = minV      # Update second min value to prev min value
                minV = grid[0][i]
                minCol = i
            elif grid[0][i] < secMinV:
                secMinV = grid[0][i]
        for i in range(1, n):
            curMinV = curSecMinV = math.inf
            curMinCol = -1
            for j in range(n):          # Save current rows `min` and `second min` values
                grid[i][j] += (minV if j != minCol else secMinV)
                if grid[i][j] < curMinV:
                    curSecMinV = curMinV
                    curMinV = grid[i][j]
                    curMinCol = j
                elif grid[i][j] < curSecMinV:
                    curSecMinV = grid[i][j]
            minV = curMinV              # Update `min` and `second min` to use for calculating next row
            secMinV = curSecMinV
            minCol = curMinCol
        return min(grid[-1])

    # DFS with memoization, still TLE for large case
    def minFallingPathSumDFS(self, grid: List[List[int]]) -> int:

        def dfs(row, col):
            if row == n - 1:
                return grid[row][col]
            if (row, col) in memo:
                return memo[(row, col)]
            minSum = math.inf
            for newCol in range(n):
                if newCol != col:
                    minSum = min(minSum, grid[row][col] + dfs(row + 1, newCol))
            memo[(row, col)] = minSum
            return minSum

        if not grid or len(grid) != len(grid[0]):
            return 0
        res = math.inf
        n = len(grid)
        memo = {}
        for startCol in range(n):
            res = min(res, dfs(row = 0, col = startCol))
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinFallingPathSum(self):
        s = Solution()
        self.assertEqual(s.minFallingPathSum(grid = [[50,-18,-38,39,-20,-37,-61,72,22,79],[82,26,30,-96,-1,28,87,94,34,-89],[55,-50,20,76,-50,59,-58,85,83,-83],[39,65,-68,89,-62,-53,74,2,-70,-90],[1,57,-70,83,-91,-32,-13,49,-11,58],[-55,83,60,-12,-90,-37,-36,-27,-19,-6],[76,-53,78,90,70,62,-81,-94,-32,-57],[-32,-85,81,25,80,90,-24,10,27,-55],[39,54,39,34,-45,17,-2,-61,-81,85],[-77,65,76,92,21,68,78,-13,39,22]]), -807)
        # self.assertEqual(s.minFallingPathSum(grid = [[7]]), 7)
        # self.assertEqual(s.minFallingPathSum(grid = [[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-62,-73]]), -268)
        # self.assertEqual(s.minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]]), 13)
        # self.assertEqual(s.minFallingPathSum(grid = [[-2,-18,31,-10,-71,82,47,56,-14,42],[-95,3,65,-7,64,75,-51,97,-66,-28],[36,3,-62,38,15,51,-58,-90,-23,-63],[58,-26,-42,-66,21,99,-94,-95,-90,89],[83,-66,-42,-45,43,85,51,-86,65,-39],[56,9,9,95,-56,-77,-2,20,78,17],[78,-13,-55,55,-7,43,-98,-89,38,90],[32,44,-47,81,-1,-55,-5,16,-81,17],[-87,82,2,86,-88,-58,-91,-79,44,-9],[-96,-14,-52,-8,12,38,84,77,-51,52]]), -879)
        


if __name__ == '__main__':
    unittest.main()