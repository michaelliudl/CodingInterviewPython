from typing import List,Deque

'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''
class Solution:

    # Similar to 994 rotting orages
    # BFS by enqueue all starting points first
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        # This problem uses this value instead of math.inf
        EMPTY = 2 ** 31 - 1
        rows, cols = len(rooms), len(rooms[0])
        queue = Deque()
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))    # Enqueue all starting points
        while queue:
            row, col = queue.popleft()
            for dRow, dCol in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nRow, nCol = row + dRow, col + dCol
                # Only check current empty cells. If a cell value (distance to gate) is not EMPTY, it's already set to closer to another gate
                if 0 <= nRow < rows and 0 <= nCol < cols and rooms[nRow][nCol] == EMPTY:
                    rooms[nRow][nCol] = rooms[row][col] + 1
                    queue.append((nRow, nCol))
        

import unittest

class TestSolution(unittest.TestCase):
    def testWallsAndGates(self):
        s = Solution()
        rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        s.wallsAndGates(rooms)
        self.assertEqual(rooms, [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]])
        rooms = [[-1]]
        s.wallsAndGates(rooms)
        self.assertEqual(rooms, [[-1]])
        


if __name__ == '__main__':
    unittest.main()