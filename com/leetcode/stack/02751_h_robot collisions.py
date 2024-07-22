from typing import List

class Solution:

    # Group robots and sort by positions. Use stack to track robots and calculate collisions.
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        robots.sort()

        stack = []
        for pos, health, direction, index in robots:
            if direction == 'R':     # Stack push going right ones
                stack.append([pos, health, direction, index])
            else:
                # Check potential collision
                while stack and stack[-1][2] == 'R' and health > 0:    # This one is going left and has health to collide with going right ones in the stack
                    if stack[-1][1] == health:  # Both eliminated
                        stack.pop()
                        health = 0
                    elif stack[-1][1] > health: # Stack top remaining
                        stack[-1][1] -= 1
                        health = 0
                    else:
                        stack.pop()             # Stack top eliminated
                        health -= 1
                if health > 0:                  # Going left one remaining after all collisions
                    stack.append([pos, health, direction, index])
        stack.sort(key=lambda robot: robot[3])  # Sort by original index
        return [robot[1] for robot in stack]

import unittest

class TestSolution(unittest.TestCase):
    def testSurvivedRobotsHealths(self):
        s = Solution()
        self.assertEqual(s.survivedRobotsHealths(positions = [2,19,46], healths = [42,45,2], directions = "LRL"), [42,44])
        self.assertEqual(s.survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"), [2,17,9,15,10])
        self.assertEqual(s.survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"), [14])
        self.assertEqual(s.survivedRobotsHealths(positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"), [])
        self.assertEqual(s.survivedRobotsHealths(positions = [3,47], healths = [46,26], directions = "LR"), [46,26])


if __name__ == '__main__':
    unittest.main()