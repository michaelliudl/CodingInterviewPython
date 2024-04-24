from typing import List

'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.
'''
class Solution:

    # DFS each island in fixed order, save each cells relative position to the first cell to dedup
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(x, y, startX, startY, relative):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if grid[x][y] != 1:
                return
            grid[x][y] = 2
            relative.append((x - startX, y - startY))
            dfs(x - 1, y, startX, startY, relative)
            dfs(x + 1, y, startX, startY, relative)
            dfs(x, y - 1, startX, startY, relative)
            dfs(x, y + 1, startX, startY, relative)

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dedup = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, startX = i, startY = j, relative = island)
                    if tuple(island) not in dedup:
                        dedup.add(tuple(island))
        return len(dedup)
        
import unittest

class TestSolution(unittest.TestCase):
    def testNumDistinctIslands(self):
        s = Solution()
        self.assertEqual(s.numDistinctIslands(grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]), 1)
        self.assertEqual(s.numDistinctIslands(grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]), 3)


if __name__ == '__main__':
    unittest.main()