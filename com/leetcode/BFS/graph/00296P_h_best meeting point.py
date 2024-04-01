from typing import List,Deque
import math

'''
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''

class Solution:

    # Mathimatically for Manhattan distance, on one dimension, min total distance is sum of each location's distance to one of medians on that dimension
    # This applies to any dimensions
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        # `dim` contains indices from original `grid` of `1`s
        def minDistOneDim(dim):
            # `low` `high` are index in `dim`
            dist = low = 0
            high = len(dim) - 1
            while low < high:
                dist += dim[high] - dim[low]
                low += 1
                high -= 1
            return dist

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        # Index of `1`s in each dimension should be in ascending order
        # Iterate through the dimension to collect index first
        rowIndexOfTargets, colIndexOfTargets = [], []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    rowIndexOfTargets.append(row)
        for col in range(cols):
            for row in range(rows):
                if grid[row][col] == 1:
                    colIndexOfTargets.append(col)

        # sum(row - median(row)) + sum(col - median(col))
        return minDistOneDim(rowIndexOfTargets) + minDistOneDim(colIndexOfTargets)


    # BFS from each `1`s to check if reachable from all `1`s and calculate distance
    # Calculate all since both `0` and `1` are valid options
    # Time out on large `1`s array
    def minTotalDistanceBFS(self, grid: List[List[int]]) -> int:
        
        def bfs(row, col, seq):
            queue = Deque()
            queue.append((row, col))
            visited = set()
            visited.add((row, col))
            dist = 0
            while queue:
                curLen = len(queue)
                for _ in range(curLen):
                    x, y = queue.popleft()
                    # Update reachable from all homes flag and distance for all homes and spaces
                    homeDist[x][y][0] |= (1 << seq)
                    homeDist[x][y][1] += dist
                    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                        nx, ny = x + dx, y + dy
                        # Don't exclude grid[x][y] == 1 as homes can also be meeting point
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                dist += 1

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        homes = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    homes.append((row, col))
        homeDist = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        homeNum = 0
        for row, col in homes:
            bfs(row, col, homeNum)
            homeNum += 1
        mask = 1
        for i in range(len(homes)):
            mask |= 1 << i
        result = math.inf
        for row in range(rows):
            for col in range(cols):
                if (homeDist[row][col][0] & mask) == mask:
                    result = min(result, homeDist[row][col][1])
        return result if result < math.inf else 0

        

import unittest

class TestSolution(unittest.TestCase):
    def testMinTotalDistance(self):
        s = Solution()
        self.assertEqual(s.minTotalDistance(grid = [[1,0,1,0,1]]), 4)
        self.assertEqual(s.minTotalDistance(grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]), 6)
        self.assertEqual(s.minTotalDistance(grid = [[1,1]]), 1)
        


if __name__ == '__main__':
    unittest.main()