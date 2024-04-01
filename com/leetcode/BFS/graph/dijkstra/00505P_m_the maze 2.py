from typing import List
import heapq
import math

'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''

class Solution:

    # Dijkstra to find min distance
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        def valid(x, y):
            return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

        if not maze or not start or not destination:
            return -1
        rows, cols = len(maze), len(maze[0])

        # Track min distances of each cell from start
        distances = {(row, col): math.inf for row in range(rows) for col in range(cols)}
        distances[tuple(start)] = 0

        heap = [(0, tuple(start))]
        while heap:
            dist, (x, y) = heapq.heappop(heap)
            if [x, y] == destination:
                return dist
            for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
                iterX, iterY = x, y
                # Keep moving until hit wall
                while valid(iterX + dx, iterY + dy):
                    iterX += dx
                    iterY += dy
                # Distance from start of this round
                iterDist = dist + abs(iterX - x) + abs(iterY - y)
                # Dijkastra, if new distance is smaller, update distance and queue this location
                if iterDist < distances[(iterX, iterY)]:
                    distances[(iterX, iterY)] = iterDist
                    heapq.heappush(heap, (iterDist, (iterX, iterY)))
        return -1


import unittest

class TestSolution(unittest.TestCase):
    def testShortestDistance(self):
        s = Solution()
        self.assertEqual(s.shortestDistance(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]), 12)
        self.assertEqual(s.shortestDistance(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]), -1)
        self.assertEqual(s.shortestDistance(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]), -1)


if __name__ == '__main__':
    unittest.main()