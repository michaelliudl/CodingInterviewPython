from typing import List

class Solution:
    
    # Simulate, change directions, move 1 step at a time and check if next step will meet obstacle
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set()
        for x, y in obstacles:
            obs.add((x, y))
        direction = x = y = 0   # x, y is current location, `direction`: 0 - N, 1 - E, 2 - S, 3 - W
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # dx, dy corresponding to `direction`
        res = 0
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction + 3) % 4
            else:
                for _ in range(command):
                    if ((x + dirs[direction][0]), (y + dirs[direction][1])) in obs:
                        break
                    x += dirs[direction][0]
                    y += dirs[direction][1]
            res = max(res, x * x + y * y)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testRotate(self):
        s = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if __name__ == '__main__':
    unittest.main()