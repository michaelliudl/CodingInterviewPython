from typing import List,Deque

'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Notice that you can pass through the destination but you cannot stop there.
'''
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(startX, startY):
            if startX == destination[0] and startY == destination[1]:
                return True
            if (startX, startY) in visited:
                return False
            visited.add((startX, startY))

            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                # Copy start position when beginning dfs
                iterX, iterY = startX, startY
                # Move continuous in one direction until last valid position
                while 0 <= iterX + dx < rows and 0 <= iterY + dy < cols and maze[iterX + dx][iterY + dy] == 0:
                    iterX += dx
                    iterY += dy
                # dfs from last valid position
                if dfs(iterX, iterY):
                    return True
            return False

        if not maze or not start or not destination:
            return False
        rows, cols = len(maze), len(maze[0])
        visited = set()
        result = dfs(start[0], start[1])
        return result
        

import unittest

class TestSolution(unittest.TestCase):
    def testNumIslands(self):
        s = Solution()
        self.assertEqual(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]), False)
        self.assertEqual(s.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]), True)
        self.assertEqual(s.hasPath(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]), False)


if __name__ == '__main__':
    unittest.main()