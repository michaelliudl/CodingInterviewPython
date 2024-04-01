from typing import List,Deque
import math

'''
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''

class Solution:

    # Similar to 296. Use BFS due to obstacles
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
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
                    if grid[x][y] == 0:
                        # Update reachable from all building flag and distance for all buildings to this empty space
                        buildingDist[x][y][0] |= (1 << seq)
                        buildingDist[x][y][1] += dist
                    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                        nx, ny = x + dx, y + dy
                        # Only include grid[x][y] == 0 since only empty land is allowed to choose
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                dist += 1

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        buildings = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    buildings.append((row, col))
        buildingDist = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        buildingNum = 0
        for row, col in buildings:
            bfs(row, col, buildingNum)
            buildingNum += 1
        mask = 1
        for i in range(len(buildings)):
            mask |= 1 << i
        result = math.inf
        for row in range(rows):
            for col in range(cols):
                if (buildingDist[row][col][0] & mask) == mask:
                    result = min(result, buildingDist[row][col][1])
        return result if result < math.inf else -1

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return -1
        left = 0
        result = math.inf
        orValue = 0
        prefix = nums[:]
        for i in range(1, len(prefix)):
            prefix[i] |= prefix[i - 1]
        for i, num in enumerate(nums):
            orValue |= num
            while left <= i and orValue >= k:
                result = min(result, i - left + 1)
                out = nums[left]
                orValue ^= out
                left += 1
        return result if result < math.inf else -1


import unittest

class TestSolution(unittest.TestCase):
    def testShortestDistance(self):
        s = Solution()
        self.assertEqual(s.shortestDistance(grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]), 7)
        self.assertEqual(s.shortestDistance(grid = [[1,0]]), 1)
        self.assertEqual(s.shortestDistance(grid = [[1]]), -1)

    def testMinimumSubarrayLength(self):
        s = Solution()
        self.assertEqual(s.minimumSubarrayLength(nums = [16,1,2,20,32], k = 45), 2)
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2,3], k = 2), 1)
        self.assertEqual(s.minimumSubarrayLength(nums = [2,1,8], k = 10), 3)
        self.assertEqual(s.minimumSubarrayLength(nums = [1,2], k = 0), 1)
        


if __name__ == '__main__':
    unittest.main()